---
title: "Emily2040/seedance-2.0"
author: "Emily2040"
platform: github
source: github_watchlist
source_type: github_curated
source_platform: github
stars: 3297
forks: 515
language: "Python"
description: "Comprehensive production pipeline for quad-modal AI filmmaking with Seedance 2.0"
pushed_at: "2026-07-07T00:51:54Z"
curated_note: "AI 四模态 filmmaking 流水线（Seedance 2.0），3297★，昨天刚更新，视频赛道强相关"
url: "https://github.com/Emily2040/seedance-2.0"
collected: "2026-07-08"
---

# Emily2040/seedance-2.0

> Comprehensive production pipeline for quad-modal AI filmmaking with Seedance 2.0

**Stars**: 3297 ｜ **Forks**: 515 ｜ **Language**: Python ｜ **最近活跃**: 2026-07-07T00:51:54Z

**用户收藏备注**: AI 四模态 filmmaking 流水线（Seedance 2.0），3297★，昨天刚更新，视频赛道强相关

## README

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg">
  <img alt="Seedance 2.0 Skill OS — intent-first AI filmmaking. Route, verify, direct, deliver." src="assets/hero-dark.svg" width="100%">
</picture>

# Seedance 2.0 Skill OS

**Direct the model. Don't micro-manage the frame.**

An agent that directs Seedance 2.0 like a filmmaker — reading each scene before it writes the prompt.<br>Text, image, video, and reference to video with native audio, IP-safe rewrites, source-dated platform facts, and native reader paths for English, 中文, 日本語, and 한국어.

[![Version](https://img.shields.io/badge/version-6.6.0-E2A75E?style=flat-square&labelColor=14110B)](#changelog)
[![Sub-skills](https://img.shields.io/badge/sub--skills-28-4A4438?style=flat-square&labelColor=14110B)](#skill-map)
[![References](https://img.shields.io/badge/references-60-4A4438?style=flat-square&labelColor=14110B)](#reference-library)
[![Evals](https://img.shields.io/badge/evals-126-4A4438?style=flat-square&labelColor=14110B)](#validation)
[![License](https://img.shields.io/badge/license-MIT-4A4438?style=flat-square&labelColor=14110B)](LICENSE)

[Start here](#start-here) · [Skill map](#skill-map) · [Reference library](#reference-library) · [Visual gallery](#visual-gallery) · [Install](#install)

English · [中文](docs/README.zh.md) · [日本語](docs/README.ja.md) · [한국어](docs/README.ko.md)

</div>

Author: [Iamemily2050 (@iamemily2050)](https://github.com/Emily2040) · [Instagram](https://instagram.com/iamemily2050) · [X](https://x.com/iamemily2050) · [Website](https://iamemily2050.com)

Platform context: [ByteDance Seedance 2.0](https://seed.bytedance.com/en/seedance2_0) · Dreamina · Jimeng · Doubao · [Volcengine Ark](https://www.volcengine.com/docs/82379/2291680?lang=zh) · [BytePlus ModelArk](https://docs.byteplus.com/en/docs/ModelArk/2291680) · [Runway Seedance 2](https://docs.dev.runwayml.com/guides/models/) · fal · provider/router surfaces tracked in [`platform-surface-matrix.md`](references/platform-surface-matrix.md)

Updated: **2026-07-06** · **v6.6.0 the loop closes: frame-extraction observation tooling, state lifecycle for long projects, and the worked end-to-end trace** · plus native quickstarts in six languages, a security policy, and an expanded agent-install matrix

---

## Direct the scene, don't decorate it

Most tools ask the model for a "cinematic look." A director asks what the scene is *doing* — then makes the camera, lens, light, blocking, performance, and sound all serve one intention, in a single recognizable voice, across an entire story.

The [**directing engine**](references/directing-engine.md) encodes that judgment. It reads a scene's dramatic function — the turn, the point of view, the power, the subtext — names one intention, and derives a coherent setup instead of stacking adjectives.

**Ask for "cinematic":** `epic cinematic shot of a woman reading a letter, emotional, beautiful lighting`

**Direct it:** `Medium close-up, eye-level; she lowers the letter and her hands go still as a slow push-in arrives; soft window light behind her keeps her face plain; near-silence with one chair scrape — the realization lands in the stilled hands, not a word.`

It then holds one directorial voice across every short clip of a long story, and ships with **33 worked derivations** — product, music video, horror, anime, action, comedy, documentary, high fashion, sci-fi, and more — each shown end to end.

> A reveal is not lit, framed, blocked, or performed like a goodbye. The engine refuses the generic answer and derives the specific one.

## Native Language Start / 多语言入门 / 多言語スタート / 다국어 시작

Seedance 2.0 Skill OS is English-readable, but the v6 line gives Chinese, Japanese, and Korean readers first-class entry points, active example skills, and native prompt guidance. Keep reference tags exactly as written (`@Image1`, `@Video1`, `@Audio1`, `@图片1`, `@视频1`) in every language.

| Language | Start path | Native reader note |
|---|---|---|
| English | [`seedance-prompt`](skills/seedance-prompt/SKILL.md), [`seedance-sequence`](skills/seedance-sequence/SKILL.md), [`references/vocab/en.md`](references/vocab/en.md) | Use precise production English: one visible beat, one camera move, real light, and clear reference roles. |
| 中文 | [`中文指南`](docs/README.zh.md), [`seedance-vocab-zh`](skills/seedance-vocab-zh/SKILL.md), [`seedance-examples-zh`](skills/seedance-examples-zh/SKILL.md), [`references/vocab/zh.md`](references/vocab/zh.md) | 中文用户可从角色锁定、首尾帧、运镜、动作节奏开始；提示词要短、具体、保留参考标签，不把字幕交给模型生成。 |
| 日本語 | [`日本語ガイド`](docs/README.ja.md), [`seedance-vocab-ja`](skills/seedance-vocab-ja/SKILL.md), [`seedance-examples-ja`](skills/seedance-examples-ja/SKILL.md), [`references/vocab/ja.md`](references/vocab/ja.md) | 日本語では、人物の同一性、衣装、構図、動きの終点を明確に書き、字幕や広告コピーは後処理で追加します。 |
| 한국어 | [`한국어 가이드`](docs/README.ko.md), [`seedance-vocab-ko`](skills/seedance-vocab-ko/SKILL.md), [`seedance-examples-ko`](skills/seedance-examples-ko/SKILL.md), [`references/vocab/ko.md`](references/vocab/ko.md) | 한국어 프롬프트는 인물 고정, 카메라 움직임, 조명, 사운드를 짧게 분리하고 자막과 문구는 편집 단계에서 넣습니다. |

New here? Each language also has a 5-minute quickstart: [English](docs/QUICKSTART.md) · [中文](docs/QUICKSTART.zh.md) · [日本語](docs/QUICKSTART.ja.md) · [한국어](docs/QUICKSTART.ko.md) · [Español](docs/QUICKSTART.es.md) · [Русский](docs/QUICKSTART.ru.md).

For longer stories in any language, start with [`seedance-sequence`](skills/seedance-sequence/SKILL.md). For the next part of an accepted clip, use [`seedance-continuation`](skills/seedance-continuation/SKILL.md) and update the observed final state before writing the next prompt.

## Why this repository exists

Seedance 2.0 Skill OS is a modular agent-skill package for directing Seedance 2.0 video generations. It is built around a simple principle: **direct the model, do not micro-manage the frame**.

The repository gives an AI assistant a public, auditable operating system for Seedance work. It defines when to interview, when to write a compact prompt, when to load a technical reference, when to rewrite unsafe IP content, and when to troubleshoot a bad generation.

## What This Skill Does

This skill package turns Seedance 2.0 work into a repeatable assistant workflow:

- Routes vague ideas into short creative interviews instead of premature prompt dumps.
- Directs each scene before drafting: reads its dramatic function, sets one directorial voice, and makes camera, light, blocking, performance, and sound serve a single intention instead of a generic "cinematic" look - and holds that voice across every clip of a long story.
- Writes full or compressed prompts for T2V, I2V, V2V, R2V, FLF2V, edit, extend, audio-aware, and first/last-frame workflows.
- Separates every reference asset by role: identity, environment, motion, camera rhythm, audio tempo, style, or endpoint.
- Keeps model and platform claims source-dated so API, pricing, region, quota, and model-ID details are not guessed.
- Plans into model strengths before drafting: a capability map, a fidelity-allocation model, and a working model of the generator's mechanics that explains why every rule works.
- Runs the shoot like a producer after generation: five-verdict take triage, one-variable retakes, attempt budgets, and cost-aware drafting.
- Provides native-reader front-page paths plus deeper multilingual cinematic vocabulary in English, 中文, 日本語, 한국어, Spanish, and Russian, including role binding, first/last-frame phrasing, edit/extend wording, safety wording, audio cues, continuation wording, and post-production text handling.
- Adds original community-informed examples for Chinese, Japanese, Korean, Russian-English, and Spanish-English prompt structures.
- Adds professional filmmaker workflows for treatment-to-shot-list planning, shot contracts, continuity ledgers, ACES/color handoff, audio post, subtitles/localization, aspect-ratio variants, campaign cutdowns, delivery/QC, and client review packets.
- Handles safe false-positive repairs by clarifying benign production context, not by hiding unsafe intent.
- Rewrites unsafe celebrity, protected IP, private-person, brand, logo, song, or voice requests into safer creative equivalents.
- Diagnoses failed outputs with concrete repair levers: camera, lighting, motion, reference role, duration, framing, audio, or safety wording.
- Ships validation scripts, eval cases, source data, and design checks so maintainers can review changes before release.

## Making Videos Longer Than One Generation

Do not blindly ask the skill to extend the original prompt. A continuation must be based on accepted generated footage because Seedance may not end exactly where the original prompt expected.

1. Describe the complete idea and how it ends.
2. The skill divides it into connected clips.
3. Generate Clip 01.
4. Return the generated clip or its final frame.
5. The skill records what actually happe
