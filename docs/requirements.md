# Design

## Problem statement

**Task**: image denoising for astrophotography (deep-sky). Given a noisy astrophotography image,
produce a denoised version that preserves fine astronomical details (granulation, prominences, faint nebulae, stars).

- Input:
  - Noisy image
  - Image types: (e.g. mono/color, narrowband, broadband) - **TBD**
  - File formats: (e.g. .fits, .tif, .png, .jpg etc) - **TBD**
  - Resolution limit: (e.g. up to 4k 3840x2160) - **TBD**
 
- Output:
  - Denoised image with preserved fine structures (granulation, prominences, faint nebulae, stars)
  - Whether dynamic range / bit depth must be preserved (e.g., 16-bit) – TBD
  - Color space requirements (linear vs sRGB) – TBD

- Constraints & out-of-scope:
  - In-scope: denoising only / no deconvolution / no color calibration – or adjust later
  - Out-of-scope for v1 (e.g., star removal, upscaling, stacking, etc.) – TBD

## Data Requirements

- Training dataset sources:
  - Public datasets (Hubble, ESO, etc) - **TBD**
  - Personal dataset - **TBD**
  - Scrape Astrobin? - No. Too complex.
  - What metadata is required if any? (exposure time, gain, filter, telescope, camera, etc.) - **TBD**
  - Dataset size (number of images, total GB) - **TBD**
- Data quality requirements:
  - Minimum resolution - **TBD**
  - Maximum allowed compression artifacts - **TBD**
  - Handling of bad frames (clouds, tracking errors) - **No, assuming good quality inputs only**
- Data splits:
  - Train/val/test split - **TBD**


## Model requirements

- Model family / architecture candidates
  - Architecture - **TBD**
  - Pretrained vs from scratch - **TBD**

- List similar implementations:
  - **TBD**

- Export / interoperability
  - Model must be exportable to ONNX - **Yes**
  - Target runtime(s) for inference - **TBD**
  - 

_Open questions:_
- Q: What architectures can be used for denoising?
- Q: Are there any existing implementations?

## Performance & quality requirements (non-functional)

- Prediction quality:
  - Visual quality criteria:
    - stars not bloated / not eaten
    - model should not hallucinate artifacts (double start, weird edges, vigneting)
- Runtime performance:
  - Support for CPU-only inference - **Yes**  
  - Target latency on CPU - **TBD**
  - Max memory usage - **TBD**
  - Minimum GPU VRASM needed to train/infer - GTX 2070, 8GB
  - Optimized for mobiles - **Yes**
  
## Training design

- Framework: PyTorch Lightning
- Experiment tracking: MLflow
- Hyperparameter optimization: Optuna

## Evaluation

## Inference & deployment

- Export:
  - ONNX export from trained model
  - Optional: TensorRT in a later phase

## Risks & future experiments

- Risk: over-smoothing faint structures
- Risk: poor generalization across sensors/filters
