"""Local evidence audit; never equates enabled scheduling with delivered reports."""
import argparse
import datetime as dt
import json
import pathlib
import re
import subprocess

KST = dt.timezone(dt.timedelta(hours=9))
ROOT = pathlib.Path(__file__).resolve().parents[1]


def scheduler_status(path):
    if not path.exists():
        return 'unknown'
    match = re.search(r'^status\s*=\s*"([^"]+)"', path.read_text(encoding='utf-8'), re.M)
    return match.group(1) if match else 'unknown'


def due(job, day):
    if day.weekday() not in job['days']:
        return False
    return not job.get('anchor') or (
        day - dt.date.fromisoformat(job['anchor'])).days % job['intervalDays'] == 0


def report_path(job, day):
    return f"{job['path']}/{day:%Y/%m/%Y-%m-%d}.md"


def quality(path):
    if not path.exists():
        return 'missing'
    text = path.read_text(encoding='utf-8-sig')
    if re.search(r'fallback placeholder|pipeline verification|^\s*TODO\s*$', text, re.I | re.M):
        return 'placeholder'
    if not re.search(r'https?://', text):
        return 'needs_source_review'
    return 'present_needs_semantic_validation'


def audit(config, workspace, automation_root, runtime, today):
    start = dt.date.fromisoformat(config['expectedFrom'])
    jobs = []
    for job in config['jobs']:
        repo = workspace / job['repo']
        automation = automation_root / job['id'] / 'automation.toml'
        missing = []
        for n in range(max(0, (today - start).days + 1)):
            day = start + dt.timedelta(days=n)
            if due(job, day):
                state = quality(repo / report_path(job, day))
                if state in ['missing', 'placeholder', 'needs_source_review']:
                    missing.append({'date': str(day), 'path': report_path(job, day), 'state': state})
        historical = []
        historical_gaps = []
        dated = []
        # Only exact dated paths in this report category; do not mix daily subcategories.
        for path in sorted((repo / job['path']).glob('????/??/????-??-??.md')):
            dated.append(dt.date.fromisoformat(path.stem))
            state = quality(path)
            if state in ['placeholder', 'needs_source_review']:
                historical.append({'path': path.relative_to(repo).as_posix(), 'state': state})
        if dated:
            # A newer report must not hide older gaps inside the archive.
            first = min(dated)
            end = min(today, start - dt.timedelta(days=1))
            for n in range(max(0, (end - first).days + 1)):
                day = first + dt.timedelta(days=n)
                if due(job, day) and quality(repo / report_path(job, day)) == 'missing':
                    historical_gaps.append({'date': str(day), 'path': report_path(job, day),
                                            'state': 'historical_gap_candidate'})
        ledger_dir = runtime / 'runs' / job['id']
        ledger = []
        for path in sorted(ledger_dir.glob('*.json')):
            try:
                ledger.append(json.loads(path.read_text(encoding='utf-8')))
            except (OSError, ValueError):
                ledger.append({'error': 'unreadable ledger', 'path': str(path)})
        git = subprocess.run(['git', '-c', f'safe.directory={repo.as_posix()}',
                              '-C', str(repo), 'log', '-1', '--format=%H %cI'],
                             capture_output=True, text=True)
        jobs.append({'id': job['id'], 'scheduler_status': scheduler_status(automation),
                     'scheduler_last_run': 'unknown: app execution history not exposed here',
                     'latest_recorded_run': ledger[-1] if ledger else None,
                     'latest_repo_commit': git.stdout.strip() or None,
                     'missing_due_reports': missing, 'historical_review': historical,
                     'historical_gap_candidates': historical_gaps})
    health_file = automation_root / config['health']['id'] / 'automation.toml'
    return {'as_of': str(today), 'timezone': 'Asia/Seoul',
            'deadline_note': 'Due reports evaluated only through dates whose 09:00 deadline passed.',
            'health_scheduler_status': scheduler_status(health_file), 'jobs': jobs}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--as-of', type=dt.date.fromisoformat)
    parser.add_argument('--workspace', type=pathlib.Path)
    parser.add_argument('--automation-root', type=pathlib.Path,
                        default=pathlib.Path.home() / '.codex' / 'automations')
    args = parser.parse_args()
    config = json.loads((ROOT / 'config/radar-jobs.json').read_text(encoding='utf-8'))
    now = dt.datetime.now(KST)
    today = args.as_of or (now.date() if now.hour >= 9 else now.date() - dt.timedelta(days=1))
    result = audit(config, args.workspace or pathlib.Path(config['workspace']),
                   args.automation_root, pathlib.Path(config['runtime']), today)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
