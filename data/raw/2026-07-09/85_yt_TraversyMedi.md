---
title: "Claude Code Crash Course For Developers"
author: "Traversy Media"
platform: YouTube
source: yt-dlp + cookies
source_type: aggregator_discovery
source_platform: youtube
channel: "Traversy Media"
views: "收看次數：91,369 次"
likes: ""
duration: "1:03:23"
published: "2 星期前"
video_id: ""
url: "https://www.youtube.com/watch?v=C2GpeepcmYs"
keywords: ""
subtitle_language: "N/A"
subtitle_available: true
origin_flag: "english_source"
lang_hint: "en"
query_track: "赛道1-AI工具"
collected: "2026-07-09"
subtitle_source: "opencli-transcript"
---

# 字幕正文（来源：opencli transcript）

[Chapter] intro
Hey, what's going on, guys? Welcome to my Claude Code Crash Course for developers. Now, I want to explain what this video is and what it's not. So, it is an overall introduction to the Claude Code agentic coding tool, and when it comes to coding with AI in general, the process is very subjective and individualized. And it's kind of like the wild west right now. Everybody does things their own way, and I will share my way, my process, but that'll be in a separate coding with AI crash course dedicated to showing you how to build decent-sized project using things like
feature specs and testing and context management and so on. Now, before I do that, I want to create this overview of Claude Code, and I know that there's a lot of guides out there on YouTube.
However, a lot of them are focused on vibe coding and just prompting from, you know, from the terminal. I want to show you the basics, but also get you set up in VS Code, and not only prompt, but do a little bit of refactoring, look at the diffs and exactly what Claude's doing, some of the internal tools that it runs, and so on. And we'll create a very simple terminal interface, as well as use Claude with Git to clone an existing repo and add some features to it. Now, along the way, I'll walk you through the features that you're going to use day-to-day. We'll talk about setup,
prompting, models. I'll explain how context and tokens work, skills, MCP, sub-agents, and so on. And I'm going to try to keep it short, but I always have a hard time doing that and and getting out all I want to say. But, after this, you should have a pretty good handle on using Claude Code, and in the next crash course I release, we'll be creating, basically creating a a project start to finish and my entire process.
[music] Hey guys, real quick, since you're learning about Claude Code, I wanted to mention my latest course, Coding with AI. It's a 16-hour course where I show you how to build an app from start to finish using context management, spec files, skills, agents, and more. And I know some people are skeptical about AI in software development and and trust me, I get it. I have a lot of the same opinions, but the fact is it's here to stay and all the top companies are requiring AI skills. So, I wanted to give you a a process and a workflow that
you can easily follow. And I also want to thank Neon for making this course possible. We use Neon Postgres database in the main project and I constantly use them in my own projects. They even gave us a link for a $100 credit and I'll put that in the description. Okay, so I'm sure that a lot of you have an idea of what Claude Code is. It's Anthropic's agentic coding tool and it runs in your terminal, although there's also a desktop app. There's also extensions for editors and I'll get to that, but for the most part, if you're a developer, you're going to be running it in your
[Chapter] What Is Claude Code
integrated terminal within your editor or with an editor extension. Now, unlike something like ChatGPT or the Claude AI website, it actually runs on your machine and works in your code base. It reads files, writes files, it runs commands and tooling and so on. And there's other tools like it such as Code X, Cursor, although Cursor is an editor, it has the same agentic capabilities.
But if you have any experience with these other tools, then you already have a leg up. Now, I I do want to quickly talk about pricing. I feel like not enough guides actually mention pricing because it's not free for the most part.
There is a free tier, but it's basically just to try it out and that's definitely what I would suggest starting with. But if you start to use it with a real project, you're going to hit caps really quickly. The next step up is Pro, which is $20 a month or 17 if you pay annually, and then there's a Max plan, which is $100 and that's five times the usage of the Pro plan, and a $200 Max plan plan that's 20 times the usage of the Pro plan. I personally use the the $200 Max, but I use it all day, every day, not just for coding, but I use the
desktop co-work tool for planning and and specking out projects and all types of stuff. And I'll I'll talk about that as well. Now, when it comes to installing Claude, there's a couple like I said, there's a few environments. You have the desktop app, which is what you see here, and it seems like they're really pushing the desktop app because they used to have the curl command to ins- you know, to set up the terminal here as the main call to action, but now it's a download button for the desktop app. However, for the terminal, you simply click here,
[Chapter] Installing Claude
terminal, and then you have your your curl command. Now, I do want to just cover the desktop app real quick. So, basically, there's three parts to it.
You have the chat tab, the co-work tab, and the code tab. So, the chat tab is basically the Claude AI website. It's it's a chatbot. It doesn't It doesn't um you know, it doesn't run on your file system, or I shouldn't say that, it doesn't have access to your file system. It does have some integrations with like Google Drive and calendar and so on.
But, for the most part, it's just chat GPT. Now, this the second tab is what I use this for, and that's co-work. So, co-work is basically like a virtual assistant, and it could does connect to your file system. You can see I have it connected to my Traversi Labs folder, which is actually my Obsidian vault.
Obsidian is like a markdown database, and I literally track my entire life in Obsidian. So, from business to my calendar to personal stuff, YouTube courses, just everything. And co-work, basically, I'll run a skill, a good morning skill, every morning, and it tells me what's on my schedule, my to-do's, what I should be working on, and so on. And then I'll use it to to plan out and speck out projects and stuff. So, I really like co-work. And then you can choose the model here. Now,
Fable 5 was just released 2 days ago, and I've used it a little bit, and I do like it, but I don't really I haven't used it enough to have a real opinion on it. I was using for Opus 4.8 for whatever a month or however long it was released, and I really like Opus, but uh I'm giving Fable a a chance. Now, the third tab here is code. It's Claude Code, and I don't use this because it's more like vibe coding. I mean, you can prompt here, and I can say build me whatever, but I don't have act direct access to
the code. So, you're going to if unless you're vibe coding, you're going to want it in your editor where you can see your entire project structure, and you can watch what it does. You can edit code yourself. So, I personally don't use this, but if you want to, that's that's absolutely fine. To install it in your terminal, you're going to copy this curl command, and you're going to open up your terminal, you're going to paste that in, and run it, and then just go through the process. I already have it installed, so I'm not going to run that, but that's what you would do to get set
up. And then, you can just do Claude Claude {dash} {dash} version, and it'll show you if it's installed. It'll show you the current version. Now, the working directory is really important because that's where it's going to run. That's where it's going to have access.
[Chapter] First Launch
So, I'm in my code folder. What I'm going to do is make a directory called coin CLI, and this will be the simple project that we work with in this tutorial. So, um what I'll do is open up Actually, let's CD into coin CLI, and then that's where I'm going to run Claude. Now, if it's your first time log um running Claude, you're probably going to have to authenticate, so you do need an account at claude.ai. You don't need a paid subscription. You can use the free tier, but you do need an account, and it will ask you to to validate. And at any time,
you can do {slash} login to authenticate, and you can also do {slash} logout.
[Chap