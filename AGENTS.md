# Research Radar 운영 지침

보고서 작성 전 `docs/automation-system.md`, `config/radar-jobs.json` 및 해당 job의 requirements를 읽고 필수 항목을 모두 따른다. 원문 간 충돌은 automation-system.md의 조정 규칙을 적용한다. 보고서는 한국어로 작성한다. `docs/research-radar-workflow.md`는 기존 세 일간 및 오픈소스 보고서의 상세 기준이다.

전체 본문을 먼저 채팅 commentary로 전달한 뒤 기존 Issue → Actions 아카이브를 수행한다. 파일 링크만으로 채팅 전달을 대체하지 않는다. 정상 GitHub 앱 연결은 `mcp__codex_apps__github_*`이며 다른 연결의 인증 실패를 전체 GitHub 권한 부재로 해석하지 않는다. Issue 생성, 파일 생성, commit, close를 각각 확인한다. CV archive 장애 시 아래 직접 Git 절차를 fallback으로 사용한다. AI Tool Radar는 원문의 Issue write 범위를 유지한다.

## 저장과 중복 방지

- 날짜와 조사 범위는 Asia/Seoul 기준으로 계산한다. 일간은 최근 24~72시간, 주간은 최근 7일이다.
- 기존 `daily/YYYY/MM`, `ideas`, `trends`, `japan-labs`, `opensource` 아카이브를 보존한다. 새 일간 보고서는 `daily/benchmarks`, `daily/failures`, `daily/questions` 아래에 저장한다.
- 최근 보고서와 같은 날짜의 파일을 먼저 읽는다. 중복이면 새 commit을 만들지 않는다. 수정이면 기존의 유효한 내용을 보존하고 수정 이유와 새 근거를 남긴다.
- 웹 검색과 원문 확인은 매 실행 필수다. 게시/업데이트 시각과 실제 변경 발생 시각을 구분하고 직접 근거 링크를 기록한다. 검색 결과 제목만으로 결론을 내리지 않는다.
- 확인한 사실, 저자 주장, 커뮤니티 제보, 추론을 구분한다. 점수는 평가자의 판단이며 실측치가 아님을 명시한다. 재현을 실행하지 않았으면 실행했다고 쓰지 않는다.
- 비교 조건이 다르면 `not strictly apples-to-apples`로 표시한다. 미확인 조건은 미확인으로 남긴다.
- 의미 있는 근거가 부족하면 개수를 억지로 채우지 말고 부족한 이유와 검색 범위를 기록한다. 근거 없는 연구 질문이나 fallback placeholder를 완성 보고서로 commit하지 않는다.

## Git 작업

1. 정확한 저장소인지 `git remote -v`, branch, `git status`로 확인한다. 사용자 변경은 덮어쓰거나 임의로 stash하지 않는다. 다른 실행이 진행 중이면 Git 변경 작업이 겹치지 않게 한다.
2. 깨끗한 작업 트리에서 `git pull --rebase`를 실행한 뒤 파일을 작성한다. 네트워크 실패 시에도 검증 가능한 보고서는 로컬에 보존하고 실패를 알린다.
3. 기존 repository-local user.name이 있으면 유지한다. 없으면 Woojin Jung을 사용한다. user.email은 repository-local로 wojin010629@gmail.com을 사용한다.
4. `git diff`로 내용/출처/중복을 검토한다. 이번 실행에서 작성한 파일만 명시적으로 stage한다.
5. commit 전과 push 전에 `git status`와 `git diff --cached`를 확인한다. 변경이 없으면 commit하지 않는다.
6. `research: add daily benchmark radar YYYY-MM-DD`, `research: add daily failure watch YYYY-MM-DD`, `research: add daily research questions YYYY-MM-DD`, `research: add weekly open-source radar YYYY-MM-DD` 중 적절한 메시지를 사용한다.
7. 현재 추적 branch에 commit/push한다. force push하지 않는다. push가 거절되면 사용자 변경을 보존하며 원인을 확인한다. 인증은 시스템 credential helper를 우선하며 token을 출력하거나 저장소에 기록하지 않는다.
8. 전체 본문을 먼저 전달하고 archive 후 commit hash/파일 경로/branch를 보고한다. 실패 시 로컬 파일 위치와 실패 원인을 알린다. 실행 ledger는 automation-system.md에 따라 기록한다. 변경도 실패도 없는 점검은 반복 알림을 보내지 않는다.

## 선호 일정

Asia/Seoul 일정 전체는 config/radar-jobs.json을 따른다. 기존 세 일간과 월요일 08:00 Open-Source를 유지하며 Daily Brief, Paper Ideas, Japan Lab, Trend Map, AI Tools와 매일 09:30 Health Check를 포함한다. 오전 9시 전 보고서 준비를 목표로 하되 완료 시각은 보장하지 않는다.
