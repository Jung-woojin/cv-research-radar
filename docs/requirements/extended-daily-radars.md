# Extended Daily Radars

이 문서는 일일 커밋 수를 늘리기 위해 추가된 다섯 보고서가 단순한 잔디용 파일이 되지 않도록 조사 범위와 품질 기준을 정의한다.

## 공통 규칙

- Asia/Seoul 날짜와 최근 24~72시간의 공식 원문을 사용한다.
- 후보 6~10개를 검토하고 근거가 충분한 3~5개만 남긴다. 근거가 부족하면 수를 채우지 않는다.
- 직전 7일 보고서와 중복되는 항목은 실제 revision, release, dataset 변경이 있을 때만 다시 포함한다.
- 사실, 저자 주장, 커뮤니티 재현, 평가자의 추론을 명시적으로 구분한다.
- 수치를 비교할 때 backbone, data, split, resolution, pretraining, hardware, precision, batch, TTA와 evaluator가 다른지 확인한다.
- 보고서는 5~10줄 요약, 후보 검토표, 핵심 사례, 진단→가설→최소 실험, 오늘의 GO/KILL 판단, 공식 출처를 포함한다.
- placeholder, 가짜 수치, 검색 결과 제목만으로 만든 결론은 저장하지 않는다.
- 동일 본문이면 새 commit을 만들지 않는다. 보고서 본문과 URL을 채팅과 GitHub에 동일하게 보존한다.

## Daily Dataset & Annotation Watch

경로: `daily/datasets/YYYY/MM/YYYY-MM-DD.md`

우선 조사한다.

- 새 dataset 또는 versioned release
- annotation guideline, class taxonomy, label correction
- train/validation/test split 변경
- duplicate, leakage, near-duplicate, identity overlap
- class imbalance, geographic/sensor bias, missing label
- license, access, 개인정보, 상업 사용 제약
- benchmark migration 또는 evaluator 변경

각 핵심 항목에는 dataset 규모, task, split, license, 공개 artifact, 알려진 bias, 기존 benchmark와의 호환성, 검증 가능한 최소 audit를 포함한다.

## Daily Reproducibility Watch

경로: `daily/reproducibility/YYYY/MM/YYYY-MM-DD.md`

우선 조사한다.

- 공식 reproduction 또는 저자 correction
- seed variance, environment/CUDA/PyTorch mismatch
- checkpoint와 논문 표의 불일치
- 누락 hyperparameter, data preprocessing, evaluator version
- GitHub issue/PR에서 확인된 재현 실패
- 독립 구현과 official implementation의 차이

각 사례에는 claim, 재현 조건, observed gap, 가능한 mechanism, 반증 가능한 최소 실험, GO/KILL 기준을 포함한다.

## Daily Efficiency & Edge Radar

경로: `daily/efficiency/YYYY/MM/YYYY-MM-DD.md`

우선 조사한다.

- latency, throughput, peak VRAM, memory bandwidth, power
- FLOPs/parameter와 실제 wall-clock의 불일치
- quantization, pruning, distillation, compilation
- TensorRT, ONNX, OpenVINO, CoreML, TFLite, edge/NPU runtime
- batch, precision, hardware, input resolution 차이

모든 비교에 hardware, software version, precision, batch, warm-up, input shape를 확인한다. 조건이 다르면 `not strictly apples-to-apples`로 표시한다.

## Daily Robustness & Shift Watch

경로: `daily/robustness/YYYY/MM/YYYY-MM-DD.md`

우선 조사한다.

- 날씨, 시간, 카메라, 지리, 센서, 압축, 해상도 shift
- corruption, OOD, calibration, selective prediction
- hallucination, grounding mismatch, adversarial/prompt injection
- 평균 점수는 좋아지지만 특정 failure cell이 악화되는 경우

각 사례에는 shift cell, metric, baseline 대비 악화 cell 수, calibration/coverage, failure mechanism, 최소 intervention을 포함한다.

## Daily Paper Code & Weight Release Watch

경로: `daily/releases/YYYY/MM/YYYY-MM-DD.md`

우선 조사한다.

- 새 official code, checkpoint, model card, dataset artifact
- release tag, commit, package version, evaluator script
- 논문 주장과 공개 artifact의 차이
- license, checksum/attestation, install 조건, dependency pin
- 실제 10~30분 smoke test 가능성

각 항목에는 exact version/tag, source URL, license, weights/data availability, install surface, expected GPU/VRAM, issue activity, smoke-test plan을 포함한다. 설치나 실행은 사용자가 별도로 요청하지 않으면 수행하지 않는다.
