"""Read-only GitHub archive audit. Credentials stay in memory and are never logged."""
import json
import subprocess
import urllib.error
import urllib.request


def main():
    result = subprocess.run(
        ['git', 'credential', 'fill'], input='protocol=https\nhost=github.com\n\n',
        text=True, capture_output=True, timeout=30)
    fields = dict(line.split('=', 1) for line in result.stdout.splitlines() if '=' in line)
    token = fields.get('password')
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'research-radar-audit'}
    if token:
        headers['Authorization'] = 'Bearer ' + token
    output = {}
    for repo in ['cv-research-radar', 'agent-tool-radar']:
        output[repo] = {}
        for key, endpoint in [('workflows', 'actions/workflows'),
                              ('runs', 'actions/runs?per_page=10'),
                              ('open_archive_issues', 'issues?state=open&per_page=100')]:
            request = urllib.request.Request(
                f'https://api.github.com/repos/Jung-woojin/{repo}/{endpoint}', headers=headers)
            try:
                with urllib.request.urlopen(request, timeout=30) as response:
                    data = json.load(response)
                if key == 'workflows':
                    output[repo][key] = [{k: w.get(k) for k in ['id', 'path', 'state']}
                                        for w in data['workflows']]
                elif key == 'runs':
                    output[repo][key] = [{k: r.get(k) for k in
                        ['id', 'event', 'status', 'conclusion', 'created_at', 'html_url']}
                        for r in data['workflow_runs']]
                else:
                    output[repo][key] = [{k: i.get(k) for k in ['number', 'title', 'html_url']}
                        for i in data if i['title'].startswith('[archive] ')]
            except urllib.error.HTTPError as exc:
                output[repo][key] = {'error': f'HTTP {exc.code}'}
            except (OSError, TimeoutError):
                output[repo][key] = {'error': 'network unavailable or request timed out'}
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
