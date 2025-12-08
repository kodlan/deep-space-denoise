# Design

## 1. Problem statement

- Task: image denoising for astrophotography (deep-sky).
- Input:
  - Noisy image (8/16-bit, RGB or mono)
  - Resolutions up to 4K (e.g. 3840×2160)
- Output:
  - Denoised image with preserved fine structures (granulation, prominences, faint nebulae, stars).

_Open questions:_

- Q: What input formats should be supported? RGB? Mono?

## 2. Model design


_Open questions:_
- Q: What architectures can be used for denoising?
- Q: Are there any existing implementations?

## 3. Training design

- Framework: PyTorch Lightning
- Experiment tracking: MLflow
- Hyperparameter optimization: Optuna

- Defaults:
  - Optimizer: AdamW
  - Scheduler: cosine or step LR
  - Batch size: TBD per GPU
  - Mixed precision: enabled (where supported)

_Open questions:_
- Q: What optimizer can be used?
- Q: How can accuracy be calculated?

## 4. Evaluation

## 5. Inference & deployment


- Export:
  - ONNX export from trained model
  - Optional: TensorRT in a later phase

## 6. Risks & future experiments

- Risk: over-smoothing faint structures
- Risk: poor generalization across sensors/filters

- Planned experiments:
  
