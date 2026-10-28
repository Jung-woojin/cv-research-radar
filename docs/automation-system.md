# AI/CV Research Intelligence 자동화 운영

## 적용 우선순위

사용자 첨부 원문은 `docs/requirements/`에 보존한다. intelligence-agent 원문 두 첨부는 SHA256이 같아 하나로 저장했다. 이 문서가 원문 간 저장 방식·시간·경로 충돌을 조정한다. 내용의 깊이와 필수 분석 항목은 각 원문을 모두 따른다. `config/radar-jobs.json`은 작업 목록·경로·요일·시각의 기준이며 앱의 실제 예약 설정과 매일 대조한다.

- 기존 구조를 보존한다. benchmark/failures/questions는 기존 복수형 경로를 유지한다.
- GitHub 기여와 실행 부하가 월·금에 몰리지 않도록 Weekly Open-Source는 수요일 03:00에 실행한다. 원문의 금요일 제안 때문에 동일 작업을 추가하지 않는다.
- Daily Brief는 평일 08:30, Paper Ideas는 화/목 03:00, Japan Lab은 수요일 04:30, AI Tools는 매일 08:10이다.
- Trend Map은 화요일 04:30에 확인하되 2026-10-06을 기준으로 14일 간격 날짜에만 발행한다. 다음 정규 발행일은 2026-11-03이다. 사이 주에는 조사/발행 없이 종료한다.
- 기존 Benchmark 05:30, Failure 06:30, Question 07:30을 유지한다. Health Check는 매일 09:30이다. 오전 09:00 전달은 목표이며 조사 지연·동일 채팅 실행 대기로 인해 보장하지 않는다.
- 일일 최소 10개 의미 있는 보고서를 목표로 Dataset/Annotation 10:30, Reproducibility 12:00, Efficiency/Edge 13:30, Robustness/Shift 15:00, Paper Code/Weight Release 16:30을 매일 실행한다. 빈 파일이나 근거 없는 잔디용 commit은 만들지 않는다.
- 요일 변경은 `scheduleHistory`에 효력 시작일과 이전 일정을 함께 기록한다. 2026-10-29부터 화·수·목의 주간 작업은 03:00~04:30에 먼저 실행해 05:30 이후 일간 작업과의 경합을 줄인다. Health Check는 당시 유효한 일정으로 과거 누락을 계산하며 현재 요일을 과거에 소급하지 않는다.

## 조사와 전달

매 실행 해당 원문과 최근 보고서를 읽고 날짜·v1·revision·실제 release를 공식 원문으로 확인한다. 주장/검증 사실/해석/전망을 분리하고, 동일 조건 비교·실패 원인·후속 최소 실험을 중시한다. 후보 검토 수와 최종 수는 목표이며 증거 부족 시 억지로 채우지 않는다. 후보 검토 내역은 보고서에 압축해 기록한다. raw URL 검색 결과나 placeholder는 완료 보고서가 아니다.

진단 연구의 기본 흐름은 Observation → Diagnosis → Mechanism → Hypothesis → Minimal Intervention → Experiment이다. 아이디어 proposal은 원문 필수 항목, 첫 실험, GO/KILL 기준을 포함한다. Compute cost /5는 1이 가볍고 5가 무거우며 compute efficiency /5와 방향을 혼동하지 않는다. 일본 모집/교수 소속/영어 환경은 공식 확인된 사실만 쓴다. 도구는 25개 확인 항목과 권한/보안/유지보수/측정 가능한 trial을 포함하며 실제 설치는 별도 사용자 요청이 있을 때만 한다.

보고서 첫 부분에 5~10줄 핵심 요약을 두고 **전체 본문을 먼저 채팅에 전달**한다. 작업을 계속할 수 있도록 commentary로 본문을 전달한 뒤 archive 도구를 호출한다. 링크만 제공하거나 GitHub 실패로 본문을 생략하지 않는다. GitHub에는 동일 본문과 일반 Markdown 출처 링크를 사용한다.

## GitHub 파일 API 직접 저장

2026-10-19부터 Issue → Actions 아카이브를 사용하지 않는다. 두 저장소 모두 연결된 GitHub 앱의 파일 API로 Markdown을 직접 생성·갱신한다. 정상 연결은 `mcp__codex_apps__github_*`이며 별도의 연결 실패를 전체 GitHub 권한 부재로 해석하지 않는다.

1. `config/radar-jobs.json`에서 저장소와 `path/YYYY/MM/YYYY-MM-DD.md`를 계산하고, 기본 branch의 현재 파일을 먼저 조회한다.
2. 파일이 없으면 `mcp__codex_apps__github_create_file`을 사용한다. 파일이 있으면 원격 content와 blob SHA를 읽고, 본문이 달라질 때만 해당 SHA를 넘겨 `mcp__codex_apps__github_update_file`을 사용한다.
3. GitHub에 저장하는 Markdown 본문은 채팅에서 전달한 본문과 출처 URL을 그대로 보존한다. Issue path marker나 `[archive]` 제목은 사용하지 않는다.
4. commit 메시지는 `config/radar-jobs.json`의 `title`과 Asia/Seoul 날짜를 결합한다. commit author email은 `wojin010629@gmail.com`을 사용한다.
5. 저장 후 같은 branch에서 파일을 다시 읽어 본문, blob SHA, commit SHA를 확인한다. 생성·갱신 요청만으로 성공 처리하지 않는다.
6. 같은 본문이 이미 존재하면 중복 commit을 만들지 않고 기존 commit을 기록한다.
7. 파일 API 저장 실패 시 Issue를 생성하지 않는다. 전체 채팅 보고서와 로컬 초안을 보존하고 오류 코드·대상 path·실패 단계를 ledger와 채팅에 기록한다.
8. 연결된 파일 API를 사용할 수 없는 CV 복구 작업에 한해, clean local clone에서 pull --rebase → 해당 Markdown만 stage → commit/push를 사용할 수 있다. AI Tool Radar는 파일 API write 범위를 유지한다. 어떤 fallback도 Issue를 만들지 않는다.

두 저장소의 `.github/workflows/archive-report.yml`은 legacy Issue 이벤트를 더 이상 수신하지 않는 수동 no-op workflow로 유지한다. Health Check는 workflow에 `issues` 트리거가 다시 추가되지 않았는지 점검한다.

Git commit author email은 wojin010629@gmail.com을 사용하고 기존 이름은 보존할 수 있다. token을 채팅·로그·저장소에 남기지 않는다. 앱 API/credential helper를 사용하며 새 PAT를 생성하지 않는다.

## 실행 기록과 장애 복구

`scripts/radar_health.py`는 로컬 예약 enabled 상태, 예상 보고서 날짜, 파일 누락/placeholder/출처 링크, 파일의 Git 기록, 실행 ledger를 점검한다. `scripts/github_audit.py`는 원격 기본 branch, 최근 commit, legacy workflow 트리거와 남아 있는 과거 `[archive]` Issue를 읽기 전용으로 확인한다. 로컬 상태만으로 원격 저장 성공을 단정하지 않는다.

실행마다 `C:/Users/ust21/github/radar-runtime/runs/<job-id>/<YYYY-MM-DD>.json`에 job_id, report_date, started_at, completed_at, chat_delivered, archive_status, write_method, report_path, file_url, file_sha, commit_sha, branch, error를 기록한다. `write_method`는 `github_create_file`, `github_update_file`, `unchanged` 또는 허용된 `git_fallback`이다. 과거 호환용 `issue_url` 필드는 읽을 수 있지만 새 실행에서는 `null`로 둔다. chat_delivered는 본문을 실제로 보낸 뒤에만 true다. archive_status는 pending/success/failed이며 success는 원격 내용과 commit 확인 뒤에만 쓴다.

매일 09:30 Health Check는 15개 예약의 실제 상태와 ledger, 해당 날짜 원격 파일·SHA·commit, 두 legacy workflow의 trigger를 대조한다. `issues` trigger가 다시 나타나면 장애로 알리되 새 Issue를 만들지 않는다. 원래 돌아야 하는 예약이 의도치 않게 비활성화되었으면 기존 ID를 활성화하고 새로 중복 생성하지 않는다. 사용자가 직접 pause한 예약은 재개하지 않는다.

열린 과거 Issue의 본문은 읽기 전용 복구 근거로만 사용할 수 있다. 새 Issue는 만들지 않고, 검증된 본문은 파일 API로 직접 복구한다. 새 웹 조사로 backfill할 때는 해당 날짜까지 공개된 근거만 쓴다. 당시 시각에 공개됐다는 증거가 없으면 백필 불가로 표시한다. 최신 지식으로 과거 보고서를 꾸미거나 기존 placeholder를 완료로 처리하지 않는다. 신규 작업의 정규 누락 판정은 2026-10-07부터 시작하며, 기존 아카이브의 과거 누락은 별도 history 후보로 다룬다.

GitHub 최근 성공 commit만으로 스케줄러 last_run을 추정하지 않는다. 당일 09:00 전 실행 완료를 판정하지 않는다. 성공한 정규 보고서는 매회 전달하고, 점검은 새로운 장애·복구·필요한 사용자 조치에만 알린다. 변경 없는 점검은 조용히 종료한다.

## 로컬 실행 조건

컴퓨터와 Codex 앱이 켜져 있고 로컬 프로젝트·네트워크·GitHub 인증이 사용 가능해야 한다. 앱이 꺼진 동안 실행되는 서버형 스케줄러는 이 구성에 포함되지 않는다. 외부 ChatGPT 웹 예약 이력은 이 로컬 앱에서 확인되지 않은 경우 unknown으로 남긴다.
