---
title: "FREE Face Dataset generation workflow for lora training (Qwen edit 2509)"
author: "acekiube"
platform: Reddit
source: agent-reach reddit
source_type: aggregator_discovery
source_platform: reddit
subreddit: "r/StableDiffusion"
score: 995
comments: 120
url: "https://www.reddit.com/r/StableDiffusion/comments/1o6xjwu/free_face_dataset_generation_workflow_for_lora/"
published: "2025-10-15"
query_track: "赛道2-AI创作"
collected: "2026-07-09"
---

# FREE Face Dataset generation workflow for lora training (Qwen edit 2509)

**作者**：acekiube（r/StableDiffusion）｜ **赞**：995 ｜ **评论**：120

Whats up yall - Releasing this dataset workflow I made for my patreon subs on here... just giving back to the community since I see a lot of people on here asking how to generate a dataset from scratch for the ai influencer grift and don't get clear answers or don't know where to start

Before you start typing "it's free but I need to join your patreon to get it so it's not really free"  
No here's the google drive[ link](https://drive.google.com/drive/folders/1sb2qas9F7pU-xFGb3M21CaFPif8J9Drn?usp=sharing)

The workflow works with a base face image. That image can be generated from whatever model you want qwen, WAN, sdxl, flux you name it. Just make sure it's an upper body headshot similar in composition to the image in the showcase.

The node with all the prompts doesn't need to be changed. It contains 20 prompts to generate different angle of the face based on the image we feed in the workflow. You can change to prompts to what you want just make sure you separate each prompt by returning to the next line (press enter)

Then we use qwen image edit 2509 fp8 and the 4 step qwen image lora to generate the dataset.

You might need to use GGUFs versions of the model depending on the amount of VRAM you have

For reference my slightly undervolted 5090 generates the 20 images in 130 seconds.

For the last part, you have 2 thing to do, add the path to where you want the images saved and add the name of your character. This section does 3 things:

* Create a folder with the name of your character
* Save the images in that folder
* Generate .txt files for every image containing the name of the character

Over the dozens of loras I've trained on FLUX, QWEN and WAN, it seems that you can train loras with a minimal 1 word caption (being the name of your character) and get good results.

In other words verbose captioning doesn't seem to be necessary to get good likeness using those models (Happy to be proven wrong)

From that point on, you should have a folder containing 20 images of the face of your character and 20 caption text files. You can then use your training platform of choice (Musubi-tuner, AItoolkit, Kohya-ss ect) to train your lora.

I won't be going into details on the training stuff but I made a youtube tutorial and written explanations on how to install musubi-tuner and train a Qwen lora with it. Can do a WAN variant if there is interest

Enjoy :) Will be answering questions for a while if there is any

Also added a face generation workflow using qwen if you don't already have a face locked in

[Link to workflow](https://drive.google.com/drive/folders/1sb2qas9F7pU-xFGb3M21CaFPif8J9Drn?usp=sharing)s  
Youtube vid for this workflow: [https://youtu.be/jtwzVMV1quc](https://youtu.be/jtwzVMV1quc)  
[Link to patreon](https://www.patreon.com/IceKiub) for lora training vid & post

Links to all required models

CLIP/Text Encoder

[https://huggingface.co/Comfy-Org/Qwen-Image\_ComfyUI/resolve/main/split\_files/text\_encoders/qwen\_2.5\_vl\_7b\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors)

VAE

[https://huggingface.co/Comfy-Org/Qwen-Image\_ComfyUI/resolve/main/split\_files/vae/qwen\_image\_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors)

UNET/Diffusion Model

[https://huggingface.co/aidiffuser/Qwen-Image-Edit-2509/blob/main/Qwen-Image-Edit-2509\_fp8\_e4m3fn.safetensors](https://huggingface.co/aidiffuser/Qwen-Image-Edit-2509/blob/main/Qwen-Image-Edit-2509_fp8_e4m3fn.safetensors)

**Qwen FP8:** [**https://huggingface.co/Comfy-Org/Qwen-Image\_ComfyUI/blob/main/split\_files/diffusion\_models/qwen\_image\_fp8\_e4m3fn.safetensors**](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors)

LoRA - Qwen Lightning

[https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-4steps-V1.0.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-4steps-V1.0.safetensors)

Samsung ultrareal  
[https://civitai.com/models/1551668/samsungcam-ultrareal](https://civitai.com/models/1551668/samsungcam-ultrareal)
