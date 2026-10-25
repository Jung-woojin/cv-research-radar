# CV Paper Idea Radar — 2026-10-26

## 요약

- 최근 7일의 공식 원문 후보 10편을 검토하고, 2026-10-22 공개 논문을 중심으로 연구 질문으로 전환할 근거가 충분한 7편을 선정했다.
- 가장 강한 공통 신호는 **평균 점수 향상보다 실패가 발생하는 시점과 원인을 분리해 측정해야 한다**는 점이다.
- DISTRACT는 다섯 추적기 중 일부만 언어를 방향성 있게 사용했고, 14개 clean-text 효과 중 열화 시 유의하게 수축한 효과는 4개뿐이라고 보고한다.
- Ask About the Right Moment는 추적과 정체성 결박을 분리해 VET-Bench 두 과제에서 100%를 보고했지만, 질문당 약 11회의 VLM 호출과 추적기 오류 의존성을 남긴다.
- BrickWright는 형식 검증으로 100% 유효 출력을 만들었지만 중력 안정성·하중·조립 순서는 검증 범위 밖이다. 이 간극은 독립 물리 검사로 반증 가능한 연구 문제가 된다.
- 이번 주 최우선 제안은 **CausalTextGate**다. 언어 융합의 유용성 부호를 사전에 예측해 도움이 될 때만 텍스트를 쓰는 선택적 추적기를 검증한다.
- 첫 실험은 DISTRACT의 고정된 모델 출력에서 시작한다. 새 대형 모델 학습 전에 oracle gate의 상한과 utility-sign 예측 가능성을 확인해 2일 안에 GO/KILL을 결정한다.

## 범위와 판정 규칙

- 조사 시점: 2026-10-26 05:55 KST.
- 조사 범위: 2026-10-20~2026-10-26 공개·갱신 신호. 주말 동안 arXiv의 더 최신 정규 배치가 없으므로 10월 22일 v1 원문이 핵심이다.
- 중복 제거: 직전 2026-10-23 보고서의 UtilityGate-TTA, StartStop-Mem, AtmosShift-OVS와 같은 문제 정의는 제외했다.
- 표기: **[사실]**은 원문·공식 저장소에서 확인한 내용, **[저자 주장]**은 논문의 해석, **[추론]**은 이 보고서의 연구 판단이다.

## 선정 논문 7편

### 1. AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark

- **공개일 / 출처:** 2026-10-22 v1. [arXiv](https://arxiv.org/abs/2610.31466), [HTML](https://arxiv.org/html/2610.31466), [공식 코드](https://github.com/AlayaLab/AnyGameRenderer)
- **문제·방법 [사실]:** 게임 프레임 생성에서 장면 수준 화질이 가리는 객체 누락·환각·수량 변화 실패를 entity-level benchmark와 entity-aware 학습으로 다룬다. 평가는 59개 held-out 사례, 753개 객체를 사용한다.
- **주요 결과 [저자 주장]:** zero-shot 대비 temporal match 50.9→62.9, position match 57.1→61.9, unrendered 4.1→2.9, hallucination 52.1→46.0, missed count change 34.7→21.3을 보고한다.
- **중요 한계 [사실/추론]:** 동일 검출·매칭 파이프라인을 GT에 적용해도 temporal 80.9, hallucination 34.1이어서 측정기 자체의 천장과 잡음이 크다. real-game split의 missed count는 20.0으로 개선되지 않았다.
- **자원 상태 [사실]:** Apache-2.0 코드, 추론 코드와 가중치가 공개돼 있다.
- **연결:** 생성 모델의 평균 화질 대신 객체 생존·수량·시점 실패를 별도 지표로 보는 평가 설계에 직접 연결된다.

### 2. BrickWright: Agentic Creation of Physically Feasible Brick Builds

- **공개일 / 출처:** 2026-10-22 v1. [arXiv](https://arxiv.org/abs/2610.31651), [HTML](https://arxiv.org/html/2610.31651), [프로젝트·코드](https://avalovelace1.github.io/brickwright/)
- **문제·방법 [사실]:** LLM이 만든 브릭 구조를 실제 부품, 충돌, 부유 부품, 연결성 검사와 조립 API로 반복 수정한다. BrickNet-512 프롬프트를 사용한다.
- **주요 결과 [저자 주장]:** vanilla 유효율은 Luna 0.086, Sol 0.641, Astra 0.693이고, 전체 BrickWright는 세 모델과 Haiku에서 1.0을 보고한다. validator-off는 Luna 0.529, Sol 0.779다.
- **중요 한계 [사실]:** 검증기는 중력 안정성, 하중, 실제 조립 순서를 검사하지 않는다. 따라서 100%는 정의된 형식 제약의 통과율이다.
- **자원 상태 [사실]:** 프로젝트 페이지에 코드와 벤치마크 자원이 연결돼 있다.
- **연결:** 형식 검증 통과와 실제 물리 유효성의 불일치를 독립 시뮬레이션으로 측정하는 연구 문제를 제공한다.

### 3. Progress Probes P²: Lightweight Runtime Monitoring for Vision-Language-Action Models

- **공개일 / 출처:** 2026-10-22 v1. [arXiv](https://arxiv.org/abs/2610.31613), [HTML](https://arxiv.org/html/2610.31613)
- **문제·방법 [사실]:** 성공 demonstration의 은닉 표현만으로 약 2K 파라미터 선형 probe를 학습해 VLA 실행의 진행과 실패를 온라인 감시한다. 6개 과제, 600개 rollout을 평가한다.
- **주요 결과 [저자 주장]:** 전체 episode/state AUROC 0.909/0.788, unseen-task 평균 0.900/0.794, 5% FPR에서 평균 탐지 시점 0.60을 보고한다. 저자는 4B Robometer보다 10,000배 이상 빠르다고 주장한다.
- **중요 한계 [사실/추론]:** π0.5와 6개 과제로 제한되며, 늦고 급작스러운 실패나 느리지만 성공하는 실행을 진행 정체로 오인할 수 있다.
- **자원 상태:** 논문 원문은 확인했으나 이번 조사에서 독립적으로 실행 가능한 공식 코드 공개는 확인하지 못했다.
- **연결:** 성공-only probe를 객체 정체성 결박 시점과 재결박 트리거로 전환할 근거를 준다.

### 4. OpenTac: An Open Ecosystem for Customizable, Scalable, and Transferable 3D Tactile Sensing

- **공개일 / 출처:** 2026-10-22 v1. [arXiv](https://arxiv.org/abs/2610.31661), [HTML](https://arxiv.org/html/2610.31661), [프로젝트·코드](https://opentac.github.io/)
- **문제·방법 [사실]:** 31개 보드와 4개 로봇 형태에서 재구성 가능한 3D 촉각 센서·학습·제어 생태계를 제시한다.
- **주요 결과 [저자 주장]:** cross-sensor 5,290개 예측에서 median F1 0.750, common-support 0.788을 보고한다. 20회 하중 파지에서 OpenTac-3D는 16회 유지, 평균 미끄럼 2.6±1.2 cm였고 F/T는 9회, 5.5±1.3 cm였다.
- **중요 한계 [사실]:** 전이는 normal-contact shape에 집중하며 force magnitude와 sim-to-real policy transfer를 입증하지 않는다. 19.2배 판독 가속은 부분 공간 관측과 교환된다.
- **자원 상태 [사실]:** 공식 프로젝트에서 하드웨어·코드 자원을 공개한다.
- **연결:** 형식 검증기가 놓치는 접촉·하중 실패를 저비용 센서 신호로 선택적으로 검사하는 경로를 제시한다.

### 5. AgentVQA: A Unified Benchmark for Agentic Visual Understanding

- **공개일 / 출처:** 2026-10-22 v1. [arXiv](https://arxiv.org/abs/2610.31494), [HTML](https://arxiv.org/html/2610.31494)
- **문제·방법 [사실]:** Web, Robotics, Egocentric, Games, Spatial Planning의 23개 데이터셋에서 1,000개 예제를 모아 22개 모델의 agentic visual understanding을 평가한다.
- **주요 결과 [저자 주장]:** 최고 모델도 58.5%이며 도메인 평균은 Egocentric 59, Games 51.5, Spatial 46, Robotics 38, Web 29다. MMMU-Pro와 순위 상관은 0.67이다.
- **중요 한계 [사실/추론]:** Gemini 3.1 Pro 오류 분류는 반자동이며 수동 검토는 100개 assignment다. grounding·visual state·motion·spatial 오류가 주된 범주라는 결론은 더 큰 수동 표본에서 재검증해야 한다.
- **자원 상태 [사실]:** 원문에서 GitHub와 Hugging Face 자원을 연결한다.
- **연결:** 정적 QA 점수와 행동 가능한 시각 상태 추론 사이의 불일치를 보여주며, 제안별 범용성 확인용 외부 벤치마크가 된다.

### 6. DISTRACT: Degradation-Indexed Study of Textual Reference Across Competing Targets

- **공개일 / 출처:** 2026-10-20 v1. [arXiv](https://arxiv.org/abs/2610.28419), [HTML](https://arxiv.org/html/2610.28419)
- **문제·방법 [사실]:** 같은 비디오·표적·방해물에 correct/conflicting text와 네 열화 조건을 짝지어 언어가 tracking decision을 실제로 바꾸는지 검사한다. 5개 VLT와 4개 데이터셋을 평가한다.
- **주요 결과 [저자 주장]:** decision-near Text BA는 Molmo2 0.574(q=.015), JointNLT 0.695(q=.002)지만 UVLTrack 0.530(q=.174), MMTrack 0.488(q=.898), DUTrack 0.504(q=.506)다. 14개 clean target effect 중 열화에서 유의하게 수축한 효과는 4개뿐이다.
- **중요 한계 [사실]:** JointNLT SportsMOT clean effect는 -11.2%로 텍스트가 해로운 경우가 있다. causal donor control은 표적별 semantic rescue 자체를 입증하지 않으며 재현 패키지는 원본 미디어·체크포인트를 재배포하지 않는다.
- **자원 상태 [사실]:** 공식 재현 패키지가 연결되지만 전체 재현에는 upstream 자원이 필요하다.
- **연결:** 텍스트의 존재가 아니라 **조건부 인과 효용**을 예측하는 CausalTextGate의 직접 근거다.

### 7. Ask About the Right Moment: Training-Free Object Identity Reasoning for Video-Language Models

- **공개일 / 출처:** 2026-10-22 v1. [arXiv](https://arxiv.org/abs/2610.31471), [HTML](https://arxiv.org/html/2610.31471)
- **문제·방법 [사실]:** SAM2.1로 후보를 추적하고 정체성 근거가 보이는 순간 frozen VLM에 정적 질문을 던져 track과 identity를 결박한 뒤, 추적 상태에서 답을 읽는다.
- **주요 결과 [저자 주장]:** Qwen3-VL-32B direct는 VET cup/card 32/38, PT-65 33.8, TOC 37.1이고 Track, Then Bind는 100/100, 55.4, 48.6이다. 8B agent도 VET에서 100/100을 보고한다.
- **중요 한계 [사실]:** 작은 가림 객체는 추적되지 않을 수 있고 동일 컵이 교차하면 track swap이 생긴다. 단순 질문에도 약 11회 VLM 호출이 들며 skip gate가 없다.
- **자원 상태:** 논문·부록은 확인했으나 이번 조사에서 실행 가능한 공식 코드 공개는 확인하지 못했다.
- **연결:** 시각 추론을 `track → evidence-time bind → state readout`으로 분해하며, 언제 결박·재결박할지를 학습하는 연구 질문을 연다.

## 제안 1 — CausalTextGate: 언어를 믿어야 하는 순간을 예측하는 시각 추적

1. **문제와 지금 필요한 이유:** [사실] DISTRACT에서 일부 VLT는 conflicting text에도 방향성 반응을 보이지 않고, JointNLT는 한 clean 조건에서 -11.2% 악화됐다. [추론] 평균 융합 성능보다 각 clip/frame에서 언어가 이득인지 손해인지 먼저 판단해야 한다.
2. **연구 공백:** 기존 confidence gate는 모델의 확신을 측정하지만 `correct text를 넣었을 때 vision-only보다 실제로 좋아지는가`라는 반사실적 utility를 직접 학습하지 않는다.
3. **가설:** correct/conflicting/vision-only의 짝지어진 결과로 정의한 utility sign은 결박 전 시각·언어·distractor feature에서 예측 가능하며, 선택적 융합이 항상-융합보다 negative text transfer를 줄인다.
4. **아키텍처:** frozen visual tracker, text encoder, target–distractor margin extractor, 2층 utility-sign probe, 세 경로 router(vision-only/text-fused/re-ground), abstention threshold로 구성한다.
5. **베이스라인:** vision-only, always-text, confidence threshold, entropy threshold, oracle utility gate, DISTRACT의 Molmo2·JointNLT·UVLTrack 결과.
6. **데이터셋·지표:** DISTRACT 4개 데이터셋의 matched runs. tracking accuracy, target effect, distractor capture, negative-transfer rate, utility-sign AUROC/AUPRC, ECE, selective risk–coverage, latency를 측정한다.
7. **Ablation:** text feature 제거, degradation index 제거, distractor margin 제거, 3-way→binary router, calibration 제거, clip-level→frame-level label, 모델 간 transfer를 비교한다.
8. **실패·음성 결과:** oracle gate 이득이 작으면 gating 문제 자체가 무의미하다. correct/conflicting 차이가 feature에 남지 않으면 probe가 dataset artifact만 배울 수 있다. 모델별 utility sign이 반대면 공통 gate가 실패할 수 있다.
9. **참신성 위험과 방어:** “또 하나의 confidence gate”로 보일 위험이 크다. matched counterfactual text로 **융합 전 인과 효용의 부호**를 label로 정의하고, degradation·tracker 간 이동을 검증해 차별화한다.
10. **4–8주 MVP:** 1주 oracle 상한/label 생성, 2주 frozen feature probe, 3주 selective routing, 4주 degradation·cross-model 평가, 5–6주 frame-level/캘리브레이션, 7–8주 오류 분석과 논문화.
11. **기여 3개:** (i) counterfactual text utility label, (ii) selective language routing 모델, (iii) negative transfer와 coverage를 함께 보는 평가 프로토콜.
12. **제목 후보:** “CausalTextGate: Selective Language Fusion for Visual Tracking”; “When Should a Tracker Trust Language?”; “Predicting the Sign of Text Utility in Vision-Language Tracking”.
13. **초록 구성:** 언어 융합의 불안정성 → matched counterfactual 진단 → utility-sign router → 4개 데이터셋 결과 → failure boundary와 비용.
14. **서론 흐름:** 언어의 잠재 이점 → 평균 점수의 맹점 → DISTRACT의 상반 신호 → 연구 질문 → 방법과 기여.
15. **관련 연구 구조:** vision-language tracking / selective prediction·calibration / counterfactual multimodal evaluation / negative transfer.
16. **방법 구조:** utility 정의 → feature extraction → calibrated router → training objective → inference policy → complexity.
17. **표·그림 계획:** Table 1 항상-융합 대비 핵심 지표, Table 2 degradation·tracker transfer, Table 3 ablation, Fig. 1 causal routing, Fig. 2 risk–coverage, Fig. 3 frame별 utility와 switch 사례.

**점수:** Novelty 4.2/5 · Feasibility 4.6/5 · Compute cost 1.8/5 · Publication potential 4.1/5.

## 제안 2 — BindAtEvidence: 장기 비디오에서 객체 정체성을 언제 결박할 것인가

1. **문제와 지금 필요한 이유:** [사실] Track, Then Bind는 큰 정확도 향상을 보이지만 질문당 약 11회 VLM을 부르고 tracker 오류를 상속한다. [추론] 결박 시점을 고정 탐색하지 않고 정체성 근거가 충분한 순간만 선택해야 한다.
2. **연구 공백:** 기존 방법은 `무엇을 추적할지`와 `언제 identity를 확정·재확정할지`를 별도 calibration 문제로 다루지 않는다.
3. **가설:** 성공 trajectory의 frozen representation으로 학습한 identity-progress probe가 최적 bind/rebind 시점의 근사 신호가 되며, 정확도를 유지하면서 VLM 호출을 절반 이하로 줄인다.
4. **아키텍처:** SAM2.1 tracker, per-track appearance memory, success-only identity-progress probe, bind-time scheduler, uncertainty-triggered high-resolution crop, rebind detector, state readout 모듈.
5. **베이스라인:** direct VLM, uniform frame sampling, Track, Then Bind, entropy-min frame, oracle best-frame binding, no-rebind와 periodic-rebind.
6. **데이터셋·지표:** VET-Bench cup/card, Perception Test PT-65, TOC. 정확도, identity switch, bind-time regret, VLM calls/question, latency, progress AUROC, ECE를 측정한다.
7. **Ablation:** progress probe 제거, appearance memory 제거, rebind 제거, high-res crop 제거, success-only vs mixed labels, 8B/32B VLM, tracker 교체.
8. **실패·음성 결과:** 교차하는 동일 객체는 시각 feature만으로 identity를 복구하지 못할 수 있다. 최적 시점이 과제마다 다르면 transfer가 무너진다. oracle timing gap이 작으면 scheduler 연구 가치가 없다.
9. **참신성 위험과 방어:** keyframe selection으로 축소될 위험이 있다. identity 결박의 상태 전이, rebind, 호출 비용까지 공동 평가하고 success-only probe의 task transfer를 핵심으로 둔다.
10. **4–8주 MVP:** 1주 원 방법 재현/로그, 2주 oracle bind-time, 3주 probe, 4주 scheduler, 5주 rebind, 6주 8B/32B 비교, 7–8주 오류 유형과 효율 분석.
11. **기여 3개:** (i) identity-progress 신호 정의, (ii) adaptive bind/rebind policy, (iii) 정확도–호출비용–identity switch 공동 benchmark.
12. **제목 후보:** “BindAtEvidence: Adaptive Identity Commitment in Long Video”; “When to Name What You Track”; “Progress-Guided Object Identity Binding for Video-Language Models”.
13. **초록 구성:** 장기 비디오 identity 실패 → 추적/결박 분리 → progress-guided scheduler → 세 벤치마크 정확도·호출 절감 → 한계.
14. **서론 흐름:** VLM의 보이지 않는 시점 실패 → Track, Then Bind 성과와 비용 → 시점 선택 질문 → 제안과 기여.
15. **관련 연구 구조:** video object tracking / temporal VLM reasoning / active perception·keyframe selection / runtime progress monitoring.
16. **방법 구조:** track memory → progress target → bind scheduler → rebind logic → answer readout → compute analysis.
17. **표·그림 계획:** Table 1 정확도·호출·지연, Table 2 tracker/VLM transfer, Table 3 ablation, Fig. 1 state machine, Fig. 2 bind-time distribution, Fig. 3 track swap failure.

**점수:** Novelty 4.0/5 · Feasibility 3.8/5 · Compute cost 2.8/5 · Publication potential 4.0/5.

## 제안 3 — ValidatorGap: 형식 검증 통과와 물리적 유효성의 간극 측정

1. **문제와 지금 필요한 이유:** [사실] BrickWright는 정의된 validator에서 100% 통과하지만 중력·하중·조립 순서는 범위 밖이다. [추론] agentic 3D 생성의 핵심 위험은 생성기보다 validator의 blind spot일 수 있다.
2. **연구 공백:** collision/connectivity 같은 이산 제약을 통과한 결과가 동역학·하중·조립 가능성까지 만족하는지 독립적으로 측정하는 공개 protocol이 부족하다.
3. **가설:** symbolic-valid 빌드의 유의한 일부가 독립 물리 시험에서 실패하고, 구조 그래프·접촉·질량중심 특징으로 고비용 물리 검사를 선택적으로 호출할 수 있다.
4. **아키텍처:** BrickWright 출력 수집기, 기존 symbolic validator, 독립 physics harness, load/perturbation test, assembly-sequence checker, graph risk predictor, optional tactile/contact proxy.
5. **베이스라인:** symbolic pass only, 전수 physics test, 무작위 selective test, 규칙 기반 center-of-mass, graph MLP risk score, oracle risk selector.
6. **데이터셋·지표:** BrickNet-512에서 계층화한 최소 100개 프롬프트와 모델별 결과. symbolic pass, simulated stability, 최대 하중, assembly feasibility, validator disagreement, risk AUROC/AUPRC, 검사 시간과 coverage를 측정한다.
7. **Ablation:** 질량중심, 접촉 그래프, 부품 종류, 조립 순서 특징 제거; simulator seed·마찰 변화; 생성 모델별 transfer; tactile/contact feature 유무.
8. **실패·음성 결과:** 시뮬레이터 오류가 실제 불가능과 혼동될 수 있다. disagreement가 거의 없으면 문제 규모가 작다. 반대로 너무 많으면 생성기보다 validator 정의 수정이 우선이다.
9. **참신성 위험과 방어:** 단순 benchmark audit로 보일 수 있다. 최소 반례, validator coverage curve, 선택적 escalation 정책과 실제 소규모 조립 검증을 결합한다.
10. **4–8주 MVP:** 1주 출력/validator 재현, 2주 물리 harness, 3주 반례 생성, 4주 위험 probe, 5주 selective policy, 6주 소규모 실제 조립, 7–8주 robustness와 정리.
11. **기여 3개:** (i) validator blind-spot taxonomy, (ii) independent physical validity suite, (iii) 비용 대비 검출률을 최적화하는 selective escalation.
12. **제목 후보:** “ValidatorGap: When Physically Feasible Generations Only Pass the Checker”; “Beyond Collision-Free: Auditing Agentic 3D Build Validators”; “Selective Physical Verification for Agent-Generated Assemblies”.
13. **초록 구성:** 100% pass의 의미 제한 → 독립 검사 suite → blind-spot 측정 → 선택적 검증 결과 → 실제 적용 한계.
14. **서론 흐름:** executable validation의 가치 → 사양 외 실패 → 연구 질문 → audit와 selector → 기여.
15. **관련 연구 구조:** constrained 3D generation / program synthesis validation / physics simulation / selective verification / tactile validation.
16. **방법 구조:** threat model → independent tests → disagreement labels → risk model → escalation policy → real-build check.
17. **표·그림 계획:** Table 1 validator별 coverage, Table 2 모델별 disagreement, Table 3 risk ablation, Fig. 1 검증 계층, Fig. 2 비용–coverage 곡선, Fig. 3 최소 반례.

**점수:** Novelty 4.4/5 · Feasibility 3.5/5 · Compute cost 2.4/5 · Publication potential 4.2/5.

## 제안 비교와 이번 주 선택

| 제안 | 핵심 질문 | Novelty | Feasibility | Compute cost | Publication potential | 가장 빠른 반증 |
|---|---|---:|---:|---:|---:|---|
| CausalTextGate | 텍스트 융합의 효용 부호를 사전에 예측할 수 있는가 | 4.2 | 4.6 | 1.8 | 4.1 | 고정 출력의 oracle/probe 분석 |
| BindAtEvidence | identity를 언제 bind/rebind해야 하는가 | 4.0 | 3.8 | 2.8 | 4.0 | oracle bind-time gap |
| ValidatorGap | validator pass가 독립 물리 시험도 통과하는가 | 4.4 | 3.5 | 2.4 | 4.2 | 100개 구조의 disagreement rate |

**이번 주 선택: CausalTextGate.** 이유는 새 foundation model 학습 없이 기존 matched output과 frozen feature만으로 가장 중요한 전제 두 가지—(1) oracle gating 상한이 존재하는가, (2) utility sign이 예측 가능한가—를 빠르게 반증할 수 있기 때문이다. ValidatorGap은 더 높은 novelty 잠재력이 있지만 독립 physics harness의 측정 타당성 확보가 먼저 필요하다.

## 첫 최소 실험

- **모델:** DISTRACT에서 방향성 text effect가 확인된 Molmo2와 JointNLT. frozen feature를 사용한 logistic regression 및 2-layer MLP probe.
- **데이터:** DISTRACT 4개 데이터셋의 공개 matched run 중 공식 자원을 확보할 수 있는 전체 쌍. 첫 48시간에는 데이터셋별 최대 500 matched units로 제한하고 실제 가용 수를 그대로 보고한다.
- **예측 변수:** vision-only confidence/margin, text–target similarity, text–distractor similarity, degradation index, temporal consistency. 정답 label은 `metric(correct text) - metric(vision only)`의 부호다.
- **평가:** utility-sign AUROC/AUPRC, ECE, negative-transfer rate, tracking metric, risk–coverage. 데이터셋 단위 leave-one-dataset-out도 함께 본다.
- **곡선·상관·ablation:** oracle gate 상한, threshold별 risk–coverage, predicted utility와 실제 delta의 Spearman 상관, text feature/visual margin/degradation feature 제거 ablation.
- **GO:** oracle gate가 always-text 대비 tracking metric을 1.0 point 이상 높이고, probe AUROC ≥0.70이며, negative-transfer rate를 30% 이상 줄이되 clean target accuracy 하락이 0.5 point 이하일 때.
- **KILL:** oracle gate 이득이 1.0 point 미만이거나, 두 모델 모두 AUROC <0.60이거나, 개선이 degradation ID를 제거하면 사라질 때. 이 경우 모델 제안 대신 “text utility의 비예측성/benchmark artifact” 진단 논문으로 축소하거나 종료한다.

## 실행 우선순위

1. DISTRACT 자원에서 paired key와 metric delta를 재구성하고 누락·중복을 먼저 검사한다.
2. feature 학습 전에 oracle gate의 상한과 모델별 utility-sign 불균형을 계산한다.
3. 가장 단순한 logistic probe로 cross-dataset 결과를 확인한 뒤에만 MLP와 frame-level routing으로 확장한다.
4. 동시에 ValidatorGap용 BrickWright 20개 샘플에 중력·하중 검사를 수동 적용해 다음 주 투자 여부를 판단한다.

## 출처

- AnyGameRenderer: https://arxiv.org/abs/2610.31466
- AnyGameRenderer code: https://github.com/AlayaLab/AnyGameRenderer
- BrickWright: https://arxiv.org/abs/2610.31651
- BrickWright project: https://avalovelace1.github.io/brickwright/
- Progress Probes P²: https://arxiv.org/abs/2610.31613
- OpenTac: https://arxiv.org/abs/2610.31661
- OpenTac project: https://opentac.github.io/
- AgentVQA: https://arxiv.org/abs/2610.31494
- DISTRACT: https://arxiv.org/abs/2610.28419
- Ask About the Right Moment: https://arxiv.org/abs/2610.31471

