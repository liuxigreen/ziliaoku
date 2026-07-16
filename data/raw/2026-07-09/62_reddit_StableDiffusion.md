---
title: "Krea 2 Turbo — Native ComfyUI Workflow + FP8 Weights (12GB, Drag & Drop)"
author: "LightAppropriate624"
platform: Reddit
source: agent-reach reddit
source_type: aggregator_discovery
source_platform: reddit
subreddit: "r/StableDiffusion"
score: 458
comments: 189
url: "https://www.reddit.com/r/StableDiffusion/comments/1ud2nyq/krea_2_turbo_native_comfyui_workflow_fp8_weights/"
published: "2026-06-23"
query_track: "赛道2-AI创作"
collected: "2026-07-09"
---

# Krea 2 Turbo — Native ComfyUI Workflow + FP8 Weights (12GB, Drag & Drop)

**作者**：LightAppropriate624（r/StableDiffusion）｜ **赞**：458 ｜ **评论**：189

ComfyUI 0.25.0 shipped with native Krea2 support, so here's everything you need in one place.

ComfyUI 0.25.0 now has native Krea2 support built-in — no custom nodes needed. Here's everything in one place so you don't have to chase files across three different HF repos.

What you get:

FP8 model — 24.76 GB BF16 → 12.01 GB. Not a blind "quant everything" conversion. Only 2D weight matrices went to `float8_e4m3fn` — all biases, norms, and modulation layers stay in native precision. 266 tensors quantized, 166 preserved. Fits on 16-24GB cards.

Drag & drop workflow — uses ComfyUI's stock `CLIPLoader (type: krea2)` \+ `UNETLoader`. Open ComfyUI, drag the JSON onto the canvas, queue. That's it.

20 sample generations in the README gallery covering 3D, anime, photorealism, stylized.

3 files you need:

|File|Size|Place in|
|:-|:-|:-|
|[AlperKTS/Krea2\_FP8 · Hugging Face](https://huggingface.co/AlperKTS/Krea2_FP8)|12 GB|`ComfyUI/models/unet/`|
|[Comfy-Org/Qwen3-VL at main](https://huggingface.co/Comfy-Org/Qwen3-VL/tree/main/text_encoders)|\~8 GB|`ComfyUI/models/text_encoders/`|
|[Comfy-Org/Qwen-Image\_ComfyUI at main](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/tree/main/split_files/vae)|\~250 MB|`ComfyUI/models/vae/`|

Recommended settings (Turbo):

* 1024×1024, 8 steps, CFG 1.0
* Sampler: `er_sde`, Scheduler: `simple`
* \~5-6 seconds on RTX 5090, runs fine on 3090/4090

Links:

* 🤗 FP8 model + workflow: [AlperKTS/Krea2\_FP8 · Hugging Face](https://huggingface.co/AlperKTS/Krea2_FP8)
* Original model: [KREA.ai](http://KREA.ai) — [Krea 2 Community License Agreement](https://www.krea.ai/krea-2-licensing)
