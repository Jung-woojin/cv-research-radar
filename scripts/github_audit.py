"""Read-only audit for direct GitHub file archiving.

Credentials stay in memory and are never logged. Legacy archive Issues are listed only
for recovery; scheduled runs must never create them.
"""
import base64
import json
import subprocess
import urllib.error
import urllib.request


def request_json(url, headers):
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def legacy_issue_trigger(repo, headers):
    url = f'https://api.github.com/repos/Jung-woojin/{repo}/contents/.github/workflows/archive-report.yml'
    data = request_json(url, headers)
    text = base64.b64decode(data['content']).decode('utf-8')
    return {
        'path': '.github/workflows/archive-report.yml',
        'sha': data.get('sha'),
        'has_issue_trigger': 'issues:' in text,
        'has_manual_trigger': 'workflow_dispatch:' in text,
    }


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
        endpoints = {
            'repository': '',
            'latest_commits': 'commits?per_page=10',
            'workflows': 'actions/workflows',
            'legacy_open_archive_issues': 'issues?state=open&per_page=100',
        }
        for key, endpoint in endpoints.items():
            url = f'https://api.github.com/repos/Jung-woojin/{repo}'
            if endpoint:
                url += '/' + endpoint
            try:
                data = request_json(url, headers)
                if key == 'repository':
                    output[repo][key] = {
                        k: data.get(k) for k in ['full_name', 'default_branch', 'pushed_at']}
                elif key == 'latest_commits':
                    output[repo][key] = [{
                        'sha': item.get('sha'),
                        'message': (item.get('commit') or {}).get('message'),
                        'html_url': item.get('html_url'),
                    } for item in data]
                elif key == 'workflows':
                    output[repo][key] = [
                        {k: item.get(k) for k in ['id', 'path', 'state']}
                        for item in data['workflows']]
                else:
                    output[repo][key] = [
                        {k: item.get(k) for k in ['number', 'title', 'html_url']}
                        for item in data if item['title'].startswith('[archive] ')]
            except urllib.error.HTTPError as exc:
                output[repo][key] = {'error': f'HTTP {exc.code}'}
            except (OSError, TimeoutError):
                output[repo][key] = {'error': 'network unavailable or request timed out'}
        try:
            output[repo]['legacy_workflow_trigger'] = legacy_issue_trigger(repo, headers)
        except urllib.error.HTTPError as exc:
            output[repo]['legacy_workflow_trigger'] = {'error': f'HTTP {exc.code}'}
        except (OSError, TimeoutError, ValueError, KeyError):
            output[repo]['legacy_workflow_trigger'] = {
                'error': 'network unavailable, malformed response, or request timed out'}
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
