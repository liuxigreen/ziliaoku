---
title: "PaddlePaddle/PaddleOCR"
author: "PaddlePaddle"
platform: github
source: github_api
source_type: github_discovery
source_platform: github
stars: 85150
forks: 10995
language: "Python"
topics: "ai4science, chineseocr, document-parsing, document-translation, kie, ocr, paddleocr-vl, pdf-extractor-rag, pdf-parser, pdf2markdown"
description: "Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages."
pushed_at: "2026-06-26T09:31:42Z"
url: "https://github.com/PaddlePaddle/PaddleOCR"
collected: "2026-07-10"
---

# PaddlePaddle/PaddleOCR

> Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

**Stars**: 85150 ｜ **Forks**: 10995 ｜ **Language**: Python ｜ **最近活跃**: 2026-06-26T09:31:42Z

## README


<div align="center">
  <p>
      <img width="800" src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/paddleocr/README/Banner.png" alt="Star-history">
  </p>



<h3>Global Leading OCR Toolkit & Document AI Engine</h3>

English | [简体中文](./readme/README_cn.md) | [繁體中文](./readme/README_tcn.md) | [日本語](./readme/README_ja.md) | [한국어](./readme/README_ko.md) | [Français](./readme/README_fr.md) | [Русский](./readme/README_ru.md) | [Español](./readme/README_es.md) | [العربية](./readme/README_ar.md)

<!-- icon -->

[![PyPI Downloads](https://static.pepy.tech/badge/paddleocr)](https://pepy.tech/projects/paddleocr)
[![Used by](https://img.shields.io/badge/Used%20by-6k%2B%20repositories-blue)](https://github.com/PaddlePaddle/PaddleOCR/network/dependents)
![python](https://img.shields.io/badge/python-3.8~3.12-aff.svg)
![os](https://img.shields.io/badge/os-linux%2C%20win%2C%20mac-pink.svg)
![hardware](https://img.shields.io/badge/hardware-cpu%2C%20gpu%2C%20xpu%2C%20npu-yellow.svg)

[![AI Studio](https://img.shields.io/badge/PaddleOCR-_Offiical_Website-1927BA?logo=data:image/png;base64,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&labelColor=white)](https://www.paddleocr.com)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/PaddlePaddle/PaddleOCR)
[![License](https://img.shields.io/badge/license-Apache_2.0-green)](../LICENSE)

</div>






**PaddleOCR converts PDF documents and images into structured, LLM-ready data (JSON/Markdown) with industry-leading accuracy. With 70k+ Stars and trusted by top-tier projects like Dify, RAGFlow, and Cherry Studio, PaddleOCR is the bedrock for building intelligent RAG and Agentic applications.**


## 🚀 Key Features

### 📄 Intelligent Document Parsing (LLM-Ready)
> *Transforming messy visuals into structured data for the LLM era.*

* **SOTA Document VLM**: Featuring **PaddleOCR-VL-1.6 (0.9B)**, the industry's leading lightweight vision-language model for document parsing. It achieves 96.3% accuracy on OmniDocBench v1.6, leads in text, formula, and table recognition, and shows significantly enhanced capabilities in ancient documents, rare characters, seals, and charts, with structured outputs in **Markdown** and **JSON** formats.
* **Structure-Aware Conversion**: Powered by **PP-StructureV3**, seamlessly convert complex PDFs and images into **Markdown** or **JSON**. Unlike the PaddleOCR-VL series models, it provides more fine-grained coordinate information, including table cell coordinates, text coordinates, and more.
* **Production-Ready Efficiency**: Achieve commercial-grade accuracy with an ultra-small footprint. Outperforms numerous closed-source solutions in public benchmarks while remaining resource-efficient for edge/cloud deployment.

### 🔍 Universal Text Recognition (Scene OCR)
> *The global gold standard for high-speed, multilingual text spotting.*

* **100+ Languages Supported**: Native recognition for a vast global library. **PP-OCRv6** supports 50 languages with a single unified model (Chinese, English, Japanese, and 46 Latin-script languages) — no model switching needed for multilingual documents.
* **Complex Element Mastery**: Beyond standard text recognition, we support **natural scene text spotting** across a wide range of environments, including IDs, street views, books, and industrial components
* **Performance Leap**: PP-OCRv6 achieves **+4.6% detection** and **+5.1% recognition** accuracy over PP-OCRv5, surpassing mainstream Vision-Language Models. 5.2× CPU inference speedup end-to-end.

<div align="center">
  <p>
      <img width="100%" src="https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/paddleocr/README/Arch.jpg" alt="PaddleOCR Architecture">
  </p>
</div>

### 🛠️ Developer-Centric Ecosystem
* **Seamless Integration**: The premier choice for the AI Agent ecosystem—deeply integrated with **Dify, RAGFlow, Pathway, and Cherry Studio**.
* **LLM Data Flywheel**: A complete pipeline to build high-quality datasets, providing a sustainable "Data Engine" for fine-tuning Large Language Models.
* **One-Click Deployment**: Supports various hardware backends (NVIDIA GPU, Intel CPU, Kunlunxin XPU, and diverse AI Accelerators).


## 📣 Recent updates

### 🔥 2026.06.11: Release of PaddleOCR 3.7.0
- PP-OCRv6 highlights:

    - **Accuracy boost**: Medium tier achieves +4.6% detection and +5.1% recognition over PP-OCRv5_server, surpassing mainstream VLMs (Qwen3-VL-235B, GPT-5.5) with only 34.5M parameters.
    - **50 languages unified**: Single model covers Chinese, English, Japanese, and 46 Latin-script languages — no model switching needed.
    - **Specialized scenarios**: Major improvements in digital displays, dot-matrix characters, tire prints, and industrial text recognition.
    - **Faster inference**: 5.2× CPU speedup (OpenVINO), 6.1× on Apple M4 (tiny), 0.13s on A100 GPU.
    - **Three tiers for all scenarios**: tiny (1.5M) / small (7.7M) / medium (34.5M) for edge, mobile, and server deployment.
    - **Model availability**: All models are available on [HuggingFace](https://huggingface.co/collections/PaddlePaddle/pp-ocrv6) and [ModelScope](https://www.modelscope.cn/collections/PaddlePaddle/PP-OCRv6).

<details>
<summary><strong>2026.05.28: Release of PaddleOCR 3.6.0</strong></summary>

- PaddleOCR-VL-1.6 highlights:

    - **New SOTA Accuracy**: Achieves over 96.3% on OmniDocBench v1.6, also sets new SOTA on OmniDocBench v1.5 and Real5-OmniDocBench, leading both open-source and proprietary solutions in text, formula, and table recognition.
    - **Comprehensive Capability Upgrade**: Significant improvements in table, ancient document, and rare character recognition, with notably enhanced seal recognition, spotting, and chart understanding across multiple scenarios.
    - **Seamless Migration**: Model architecture is fully consistent with PaddleOCR-VL-1.5, enabling zero-cost adaptation—swap and go.
    - **Try it now**: Available on [HuggingFace](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6) or our [Official Website](https://www.paddleocr.com).

</details>

<details>
<summary><strong>2026.04.21: Release of PaddleOCR 3.5.0</strong></summary>

* **Flexible inference backends**: Seamlessly switch between Paddle static graph, Paddle dynamic graph, or Transformers. PaddleOCR is now deeply integrated with the Hugging Face ecosystem, and 20 major models support Transformers as the inference backend.
* **Office documents to Markdown**: Convert common document formats 
