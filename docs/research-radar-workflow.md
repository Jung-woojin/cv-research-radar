나는 `Jung-woojin/cv-research-radar` GitHub 저장소에 Computer Vision 연구 레이더를 자동으로 축적하고 있다.

현재 목표는 ChatGPT가 매일/주기적으로 조사한 CV·VLM·multimodal 연구 보고서를 생성한 뒤, 로컬 Git 저장소 또는 GitHub 원격 저장소에 직접 Markdown 파일로 저장하고 commit/push까지 수행하는 것이다.

GitHub 작업 시 가능하면 `wojin010629@gmail.com`을 commit author email로 사용한다.

## 대상 저장소

Repository:
`Jung-woojin/cv-research-radar`

가능하면 기존 repository를 clone하거나 이미 clone되어 있다면 해당 working tree를 사용한다.

Git 설정이 필요하면 다음을 사용한다.

```bash
git config user.name "Woojin Jung"
git config user.email "wojin010629@gmail.com"
```

단, 기존 repository에 별도의 user.name 설정이 이미 있다면 이름은 유지해도 된다. 이메일은 가능하면 위 주소를 사용한다.

---

# 현재 운영 중인 Research Radar

## 1. Daily Benchmark Movement

목적:
최근 24~72시간 동안 Computer Vision, VLM, multimodal 분야에서 발생한 benchmark, leaderboard, dataset split, evaluation protocol, metric, challenge 결과 변화를 추적한다.

우선 분야:
- object detection
- segmentation
- open-vocabulary detection
- small/tiny object detection
- grounding
- VQA
- video VLM
- aerial/UAV
- remote sensing
- maritime vision

단순 SOTA 숫자 나열이 아니라 다음을 분석한다.

1. 무엇이 실제로 바뀌었는가
2. 같은 조건 비교인가
3. backbone / pretraining / input resolution / TTA / external data 차이
4. dataset split 또는 metric 변경의 영향
5. apples-to-apples comparison 가능 여부
6. 논문 주장과 official code/leaderboard가 일치하는가
7. 실제 연구자가 따라갈 변화인지 leaderboard noise인지

1차 출처를 우선한다.
- official GitHub
- official project page
- arXiv/OpenReview/CVF
- official leaderboard
- Hugging Face model/dataset card

매일 의미 있는 변화 3~7개만 선택한다. 억지로 수를 채우지 않는다.

마지막에 반드시 포함:
- 오늘의 benchmark signal 3개
- 내 연구에 바로 연결되는 포인트

저장 경로:

```text
daily/benchmarks/YYYY/MM/YYYY-MM-DD.md
```

---

## 2. Daily Failure / Negative Result Watch

목적:
최근 24~72시간 동안 공개된 CV/VLM/multimodal 연구, 코드, GitHub issue/PR, benchmark에서 성공 사례보다 실패 사례를 집중적으로 추적한다.

우선적으로 찾을 것:
- negative result
- reproduction failure
- domain shift
- seed variance
- pretraining dependence
- small-object failure
- hallucination / grounding mismatch
- latency / VRAM explosion
- benchmark leakage
- annotation/evaluator bugs
- runtime/serving bugs
- metric artifacts

각 항목에서 반드시 분석:
1. 실패 조건
2. 모델 / dataset / configuration
3. 저자 또는 maintainer 공식 인정 여부
4. community reproduction인지 여부
5. 재현 근거
6. 의심 원인
7. 기존 주장과 충돌 여부
8. 후속 검증 실험

각 항목에 다음 점수 포함:
- 심각도 /5
- 재현 신뢰도 /5
- 연구 아이디어 가치 /5

마지막에 반드시 포함:
- 오늘의 실패 패턴 3개
- 논문 아이디어로 연결 가능한 빈틈
- 직접 재현해볼 최소 실험

저장 경로:

```text
daily/failures/YYYY/MM/YYYY-MM-DD.md
```

---

## 3. Daily Research Question Generator

목적:
최근 24~72시간의 새로운 논문, 코드, benchmark, dataset, issue/PR에서 발견된 contradiction, unexplained gain, failure mode, evaluation artifact 등을 연구 질문으로 변환한다.

우선 분야:
- object detection
- open-vocabulary / open-world detection
- small/tiny object detection
- segmentation
- CNN architecture
- inductive bias
- effective receptive field
- vision encoder
- grounding
- VQA / video VLM
- aerial/UAV
- remote sensing
- maritime vision

매일 5~8개 연구 질문을 만든다.

각 질문마다 반드시 포함:

1. 문제 정의
2. 왜 지금 가치가 있는가
3. 직접 근거가 되는 최신 논문/코드/issue
4. 핵심 가설
5. 최소 실험(MVP)
6. baseline과 dataset
7. 성공/실패 판정 metric
8. compute 난이도
9. novelty 위험요인
10. 4~8주 내 논문화 가능성
11. negative result여도 얻을 수 있는 결론

각 질문에 다음 점수를 5점 척도로 평가:
- novelty
- feasibility
- compute efficiency
- publication potential

마지막에 반드시 선정:
- 오늘 가장 먼저 테스트할 질문 1개
- RTX 5060 Ti 8GB에서도 가능한 질문
- 장기 박사주제로 키울 수 있는 질문

저장 경로:

```text
daily/questions/YYYY/MM/YYYY-MM-DD.md
```

---

## 4. Weekly CV Open-Source Radar

최근 7일 동안 공개되거나 크게 업데이트된 다음을 조사한다.

- GitHub repository
- official implementation
- model weights
- dataset
- training/inference framework

우선 분야:
- detection
- segmentation
- OVD
- small object
- CNN architecture
- vision encoder
- grounding
- VQA
- video VLM
- aerial/UAV
- maritime vision

각 항목에서 평가:
1. 새로 나온 내용
2. 논문/프로젝트 연결
3. 코드 품질과 재현성
4. 라이선스
5. pretrained weights/checkpoints
6. 설치 난이도/의존성
7. GPU/VRAM 요구량
8. 바로 실험에 붙이기 좋은지
9. MMDetection / Ultralytics / timm / Hugging Face 호환성
10. maintenance 가능성 / issue·PR 활동성

특히 매주:
`이번 주 바로 clone해서 돌려볼 가치가 있는 것` 3~5개를 선정한다.

각 후보에:
- 실험 가치 /5
- 재현성 /5
- 신규성 /5
- 실용성 /5

저장 경로:

```text
opensource/YYYY/MM/YYYY-MM-DD.md
```

---

# 전체 저장소 권장 구조

```text
cv-research-radar/
├── daily/
│   ├── benchmarks/
│   │   └── YYYY/MM/YYYY-MM-DD.md
│   ├── failures/
│   │   └── YYYY/MM/YYYY-MM-DD.md
│   └── questions/
│       └── YYYY/MM/YYYY-MM-DD.md
│
├── opensource/
│   └── YYYY/MM/YYYY-MM-DD.md
│
├── ideas/
├── trends/
├── japan-labs/
└── README.md
```

기존 구조가 이미 존재하면 임의로 깨지 말고 현재 구조를 먼저 확인한 뒤 호환되게 작업한다.

---

# 실행 시간

한국시간 기준 새벽에 조사해 오전 9시 전에 결과가 모두 준비되는 것을 목표로 한다.

현재 선호 스케줄:

```text
05:30 Daily Benchmark Movement
06:30 Daily Failure / Negative Result Watch
07:30 Daily Research Question Generator
```

각 결과는:
1. 채팅에 핵심 요약
2. 전체 보고서
3. GitHub Markdown 저장

순으로 제공한다.

---

# 파일 작업 원칙

GitHub Issue를 중간 매개체로 쓰는 것보다 로컬 filesystem/Git repository 접근 권한이 있다면 직접 Markdown 파일을 작성하는 방식을 우선한다.

작업 순서:

```text
git pull --rebase
→ 필요한 디렉터리 생성
→ Markdown 파일 작성
→ git diff 확인
→ git add
→ git commit
→ git push
```

commit message 예시:

```text
research: add daily benchmark radar 2026-10-06
research: add daily failure watch 2026-10-06
research: add daily research questions 2026-10-06
research: add weekly open-source radar 2026-10-06
```

여러 보고서를 한 번에 올리면:

```text
research: update CV research radar for 2026-10-06
```

를 사용해도 된다.

이미 같은 날짜의 파일이 있으면 무조건 덮어쓰지 말고:
- 기존 내용을 읽고
- 이번 결과가 신규인지
- 중복인지
- 수정본인지

확인한 뒤 필요한 경우만 업데이트한다.

push 전에 반드시:
- `git status`
- `git diff --cached`

를 확인한다.

---

# 중요한 조사 원칙

최근 정보가 필요한 작업이므로 항상 웹 검색을 사용한다.

우선순위:
1. 공식 GitHub
2. 공식 project page
3. arXiv/OpenReview/CVF
4. Hugging Face official model/dataset card
5. 공식 benchmark/leaderboard
6. GitHub issue/PR
7. 기타 커뮤니티 출처

가능하면 논문 제목만 보고 판단하지 말고:
- paper
- repo
- model card
- issue
- evaluation script

를 교차검증한다.

논문은 흥미롭지만 코드가 없거나 reproduction이 어려운 경우 반드시 명시한다.

숫자 비교에서는 항상 다음을 확인한다.

```text
dataset revision
train/val/test split
backbone
pretraining
external data
input resolution
TTA
inference tools
reasoning effort
context/frame budget
compute budget
evaluator version/commit
```

하나라도 크게 다르면 `not strictly apples-to-apples`라고 표시한다.

---

# 사용자 연구 관심사를 반영한 우선순위

특히 다음 연구 질문과 연결되는 항목을 우선적으로 강조한다.

- small/tiny-object detection
- P2 / high-resolution feature
- effective receptive field
- CNN/ViT inductive bias
- open-vocabulary detection negative transfer
- domain adaptation / forgetting
- VLM Answer–Region Gap
- evidence-grounded VQA
- temporal reasoning failure
- video memory
- aerial/UAV vision
- remote sensing
- maritime vision
- CCTV
- fog / maritime safety VQA

단, 매일 같은 아이디어를 반복하지 않는다.

새로운 논문/실패/benchmark 변화가 이전 연구 아이디어와 실제로 연결될 때만 연결한다.

---

# GitHub 처리 원칙

가능하면 직접 repository 파일을 수정하고 commit/push한다.

GitHub 인증이 필요한 경우 이미 연결된 GitHub credential 또는 시스템 credential helper를 우선 사용한다.

PAT가 필요해도 채팅에 token 값을 출력하거나 로그에 남기지 않는다.

Push 성공 후:
- commit hash
- 변경된 파일 경로
- push된 branch

를 사용자에게 짧게 알려준다.

Push가 실패하면:
- 보고서 생성은 취소하지 않는다.
- 생성한 Markdown 파일은 로컬에 남긴다.
- 실패 원인을 마지막에 짧게 설명한다.

---

이제 먼저 현재 환경에서 `Jung-woojin/cv-research-radar` 저장소가 존재하는지 확인하고, 없다면 clone 가능한지 확인해라. 기존 파일과 최근 commit을 확인한 뒤 중복 작업을 피하고, 이후부터 위 워크플로에 따라 리서치 결과를 직접 파일로 저장하고 push해라.