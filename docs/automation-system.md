# AI/CV Research Intelligence 자동화 운영

## 적용 우선순위

사용자 첨부 원문은 `docs/requirements/`에 보존한다. intelligence-agent 원문 두 첨부는 SHA256이 같아 하나로 저장했다. 이 문서가 원문 간 저장 방식·시간·경로 충돌을 조정한다. 내용의 깊이와 필수 분석 항목은 각 원문을 모두 따른다. `config/radar-jobs.json`은 작업 목록·경로·요일·시각의 기준이며 앱의 실제 예약 설정과 매일 대조한다.

- 기존 구조를 보존한다. benchmark/failures/questions는 기존 복수형 경로를 유지한다.
- 사용자가 이 채팅에서 선택한 Weekly Open-Source 월요일 08:00을 유지한다. 원문의 금요일 제안 때문에 동일 작업을 추가하지 않는다.
- Daily Brief는 평일 08:30, Paper Ideas는 월/금 06:00, Japan Lab은 금요일 08:00, AI Tools는 매일 08:10이다.
- Trend Map은 월요일 04:30에 확인하되 2026-10-05를 기준으로 14일 간격 날짜에만 발행한다. 다음 정규 발행일은 2026-10-19이다. 사이 주에는 조사/발행 없이 종료한다.
- 기존 Benchmark 05:30, Failure 06:30, Question 07:30을 유지한다. Health Check는 매일 09:30이다. 오전 09:00 전달은 목표이며 조사 지연·동일 채팅 실행 대기로 인해 보장하지 않는다.

## 조사와 전달

매 실행 해당 원문과 최근 보고서를 읽고 날짜·v1·revision·실제 release를 공식 원문으로 확인한다. 주장/검증 사실/해석/전망을 분리하고, 동일 조건 비교·실패 원인·후속 최소 실험을 중시한다. 후보 검토 수와 최종 수는 목표이며 증거 부족 시 억지로 채우지 않는다. 후보 검토 내역은 보고서에 압축해 기록한다. raw URL 검색 결과나 placeholder는 완료 보고서가 아니다.

진단 연구의 기본 흐름은 Observation → Diagnosis → Mechanism → Hypothesis → Minimal Intervention → Experiment이다. 아이디어 proposal은 원문 필수 항목, 첫 실험, GO/KILL 기준을 포함한다. Compute cost /5는 1이 가볍고 5가 무거우며 compute efficiency /5와 방향을 혼동하지 않는다. 일본 모집/교수 소속/영어 환경은 공식 확인된 사실만 쓴다. 도구는 25개 확인 항목과 권한/보안/유지보수/측정 가능한 trial을 포함하며 실제 설치는 별도 사용자 요청이 있을 때만 한다.

보고서 첫 부분에 5~10줄 핵심 요약을 두고 **전체 본문을 먼저 채팅에 전달**한다. 작업을 계속할 수 있도록 commentary로 본문을 전달한 뒤 archive 도구를 호출한다. 링크만 제공하거나 GitHub 실패로 본문을 생략하지 않는다. GitHub에는 동일 본문과 일반 Markdown 출처 링크를 사용한다.

## 기존 Issue 아카이브 사용

두 저장소의 `.github/workflows/archive-report.yml`은 존재하며 점검 시 active였다. 기본은 기존 Issue → Actions → Markdown → commit → close 경로다. 정상 연결은 `mcp__codex_apps__github_*` GitHub 앱 도구이며 별도의 `mcp__github__*` 연결은 현재 Bad credentials를 반환했다. 인증 상황은 매 실행 실제로 확인한다.

1. 최신 원격 파일과 같은 path를 가진 기존 Issue를 확인한다. 본문과 날짜가 같으면 재생성하지 않는다. 수정 시 유효 내용을 보존하고 수정 이유를 기록한다.
2. Issue 제목은 `[archive] `와 작업별 title 및 날짜를 결합한다. body 첫 줄은 `<!-- path: <path>/YYYY/MM/YYYY-MM-DD.md -->`이며 다음 줄부터 채팅 본문 그대로다.
3. Issue는 한 개씩 처리한다. 기존 workflow concurrency에는 대기 Issue가 몰리면 취소될 수 있는 한계가 있어, 이전 Issue의 파일/commit/close 확인 후 다음 것을 생성한다.
4. Issue 생성만으로 성공이라고 보고하지 않는다. Actions 결과, Issue closed, 해당 원격 파일의 내용, commit과 author를 확인한다. 대기 중이면 상태를 기록하고 Health Check가 이어서 확인한다.
5. CV Issue 경로가 실패하면 사용자 변경이 없는 기존 로컬 저장소에서 pull --rebase → 해당 Markdown 작성 → 명시적 stage → diff/status 검토 → commit/push로 복구할 수 있다. force push는 금지다.
6. AI Tool Radar는 원문의 좁은 write 범위를 지켜 archive Issue를 우선하며, 기존 코드·workflow·settings는 변경하지 않는다. 저장 실패 시 본문과 로컬 초안을 보존하고 정확한 archive title/body를 제공한다.

Git commit author email은 wojin010629@gmail.com을 사용하고 기존 이름은 보존할 수 있다. token을 채팅·로그·저장소에 남기지 않는다. 앱 API/credential helper를 사용하며 새 PAT를 생성하지 않는다.

## 실행 기록과 장애 복구

`scripts/radar_health.py`는 로컬 예약 enabled 상태, 예상 보고서 날짜, 파일 누락/placeholder/출처 링크, 파일의 Git 기록, 실행 ledger를 점검한다. `scripts/github_audit.py`는 원격 Actions 상태·최근 실행·열린 archive Issue를 읽기 전용으로 확인한다. 로컬 상태만으로 원격 archive 성공을 단정하지 않는다.

실행마다 `C:/Users/ust21/github/radar-runtime/runs/<job-id>/<YYYY-MM-DD>.json`에 job_id, report_date, started_at, completed_at, chat_delivered, archive_status, report_path, issue_url, commit_sha, error를 기록한다. chat_delivered는 본문을 실제로 보낸 뒤에만 true다. archive_status는 pending/success/failed이며 success는 원격 내용과 commit 확인 뒤에만 쓴다. 앱에서 last_run 이력을 제공하지 않으면 unknown으로 남기고 이 ledger를 함께 사용한다. enabled와 실제 완료를 구분한다.

매일 09:30 Health Check는 10개 예약의 실제 상태와 ledger, 해당 날짜 파일, 원격 Actions/Issue를 대조한다. 원래 돌아야 하는 예약이 의도치 않게 비활성화되었으면 기존 ID를 활성화하고 새로 중복 생성하지 않는다. 사용자가 직접 pause한 예약은 재개하지 않는다.

열린 과거 Issue의 본문이 있으면 그 원문을 검증해 그대로 복구하고 복구 이력을 남긴다. 새 웹 조사로 backfill할 때는 해당 날짜까지 공개된 근거만 쓴다. 당시 시각에 공개됐다는 증거가 없으면 백필 불가로 표시한다. 최신 지식으로 과거 보고서를 꾸미거나 기존 placeholder를 완료로 처리하지 않는다. 신규 작업의 정규 누락 판정은 2026-10-07부터 시작하며, 기존 아카이브의 과거 누락은 별도 history 후보로 다룬다.

GitHub 최근 성공 commit만으로 스케줄러 last_run을 추정하지 않는다. 당일 09:00 전 실행 완료를 판정하지 않는다. 성공한 정규 보고서는 매회 전달하고, 점검은 새로운 장애·복구·필요한 사용자 조치에만 알린다. 변경 없는 점검은 조용히 종료한다.

## 로컬 실행 조건

컴퓨터와 Codex 앱이 켜져 있고 로컬 프로젝트·네트워크·GitHub 인증이 사용 가능해야 한다. 앱이 꺼진 동안 실행되는 서버형 스케줄러는 이 구성에 포함되지 않는다. 외부 ChatGPT 웹 예약 이력은 이 로컬 앱에서 확인되지 않은 경우 unknown으로 남긴다.
