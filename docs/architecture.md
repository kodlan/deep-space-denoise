# Model architecture considerations

## DnCNN (Denoising CNN)

A seminal lightweight architecture for image denoisoing. DnCNN employs residual learning.
Is trained to predict the noise given the noisy input, which is then substracted from the input to produce 
the denoised result. DnCNN demonstrated that a relatively shallow CNN can outperform classic methods
like BM3D on Gaussian noise removal. It's fast and lightweight but it's trained on specific noise 
level or distribution. If the noise in input differs (e.g. brighter background or different camera), performance may drop.

## FFDNet
An extension of DnCNN that introduces a tunable noise map. FFDNet takes a concatenated input
of the noisy image and a user-provided noise-level map (a constant or per-pixel estimate of
noise std). This allows a single CNN to handle multiple noise levels by adjusting the
noise map

Architecturally it’s similar to DnCNN (convolutional layers with residual output) and remains
lightweight. It’s useful when noise variance is not uniform or known - for instance, to denoise
an image where different regions have different noise (common if, say, parts of the
image had varying integration times or overlaps of calibration). FFDNet and similar 
noise-agnostic models can generalize across noise levels at a slight cost of complexity.

## Small U-nets / Autonencoders
U-Net is more commonly a larger model, but one can design a shallow U-Net with fewer
feature channels as a lightweight option. A U-Net architecture has an encoder path that
progressively downsamples the image to learn coarse features and a decoder path that
upsamples and reconstructs the output, with skip connections linking corresponding levels.

Even a slim U-Net can leverage multi-scale information: for example, 
recognizing a star versus random noise by looking at a slightly larger context.
Some astrophotography-specific tools (like NoiseXTerminator, a commercial AI denoiser for astro
images) likely use a U-Net under the hood but optimized for speed. A lightweight 
U-Net might use fewer layers or smaller convolution kernels to reduce computation.

## U-net

U-Net stands as a popular high-capacity architecture for denoising and image restoration.
Its strength is capturing both fine details and global context via the encoder-decoder
structure with skip connections. A full U-Net (with 4–5 levels of down/upsampling and doubling
feature channels at each level) can have millions of parameters and hence greater ability
to model complex noise distributions and subtle details. For astrophotography, a U-Net
can learn to distinguish stars from noise by context: e.g., a star will appear in
the same position across color channels or in multiple frames, whereas hot-pixel noise
might not. A U-Net was used in the Noise2Noise approach for denoising images without clean
targets, showing its effectiveness in capturing structure from just noisy inputs

U-Nets are implemented easily in PyTorch and can be scaled depending on memory – one must 
often reduce the depth or number of feature maps to fit large astro images.
Models like HORUS (Hyper-effective nOise Removal U-net Software),
developed to denoise lunar crater images, suggest that U-Net architectures are
indeed being applied in astro-image denoising scenarios

## Deep Residual Networks
Inspired by ResNet-style architectures, these models stack many convolutional layers
with skip connections every few layers (not just one skip at the end as in DnCNN).
An example is a ResNet-based denoiser or ResUNet (which combines U-Net structure with internal
residual blocks). These very deep networks (often 20+ layers) tend to yield higher peak
signal-to-noise ratio (PSNR) on benchmarks

They benefit from residual connections by mitigating vanishing gradients and allowing easier
training of deeper models. For instance, VDNet (Variational Denoising Network) integrates noise
estimation and removal, employing a deep CNN with residual and dense connections to
handle spatially varying noise

Similarly, RIDNet (Residual Image Denoise Net with attention) and MIRNet (Multi-Scale Information \
Retrieval Net) are advanced models that include attention mechanisms and multi-scale
feature fusion for state-of-the-art denoising on natural images. 
These tend to be heavier (~5–10 million parameters or more) but can more aggressively 
clean noise while preserving detail.


## Links
- [Identity Enhandced Residual Image Denoising](https://openaccess.thecvf.com/content_CVPRW_2020/papers/w31/Anwar_Identity_Enhanced_Residual_Image_Denoising_CVPRW_2020_paper.pdf)
- https://britastro.org/journal_contents_ite/image-denoising-in-astrophotography-an-approach-using-recent-network-denoising-models
- https://viso.ai/deep-learning/u-net-a-comprehensive-guide-to-its-architecture-and-applications
- [Noise2Noise: Learning Image Restoration without Clean Data](https://arxiv.org/pdf/1803.04189) - https://arxiv.org/pdf/1803.04189


