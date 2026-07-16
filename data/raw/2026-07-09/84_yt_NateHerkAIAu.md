---
title: "32 Tricks to Level Up Claude Code in 16 Mins"
author: "Nate Herk | AI Automation"
platform: YouTube
source: yt-dlp + cookies
source_type: aggregator_discovery
source_platform: youtube
channel: "Nate Herk | AI Automation"
views: "收看次數：371,250 次"
likes: ""
duration: "16:16"
published: "2 個月前"
video_id: ""
url: "https://www.youtube.com/watch?v=jqoFP9QapXI"
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

[Chapter] Intro
These are the Cloudcode hacks that took me from a complete beginner to mass producing workflows and building websites, apps, and AI agents in real time. So today we're going to be going from beginner hacks all the way to advanced power user stuff, and the best ones are saved at the end. All right, so starting off with our beginner hacks, number one is to run {slash} init on every project. So if you've already got an existing project with files already in there, the first thing you should do is open it up and type {slash} init.
[Chapter] Beginner Hacks
Cloudcode will then scan your entire code base, your folders, your files, and it will generate a cloud.md file, which is basically like a cheat sheet for that project. It'll map out your architecture, your conventions, and any key files that you have in there. So instead of having to re-explain your project every session, Cloud will basically just contextualize everything and initialize everything and know what you're working with. And if you're starting a new project from scratch, then you can have Cloudcode help you create that cloud.md file yourself just by explaining what's the goal of this project, what tech stack you want to use, or any rules or key folders and files. All right, number two is to set
up a status line. So if you're working in the terminal, you can type {slash} status line and tell Cloudcode what you want to see. Your model, your context percentage, cost, whatever. It basically generates a little script that sits at the bottom of the terminal, so as you're talking every single time, you can just see that status line. It's kind of like a mini dashboard for your session. So it's really helpful to always be able to see how much context you have left, so you can avoid context rot. Hack number three is using voice input. So Cloudcode just shipped a native {slash} voice command, which means you can literally just talk to your terminal and have it code for you now. So it's still rolling
out, it will be out for everyone soon, but another good hack would just be to use an app to actually be able to voice tate anywhere. So if you want to see the tool that I use, you can check out the description. Now I can just talk and words will appear anywhere. Hack number four is to keep your context small. So don't dump your entire code base into a conversation, only give Cloud what it needs for the current task. So try to break big problems into small focused steps. The less noise in the context window, the better Cloud performs. It's simple, but a lot of people ignore this.
Hack number five is to use {slash} context to find your token bloat. So if you do {slash} context, you'll see exactly what's eating your tokens, whether that's system prompts or file contents, MCP servers, whatever it is.
All of that gets broken down into percentages. So if your session feels a little bloated, you can actually investigate it, diagnose where the problem is, and then restructure. Hack number six is to compact at 60% and also clear between tasks. So when your context hits around 60%, then type {slash} compact and Cloudcode will compress your conversation history so you can keep going without losing important stuff. And something interesting is that you can actually do a {slash} compact, but you can tell it to keep certain things. Like, "Hey, {slash} compact, but keep all of the API integration decisions and database schema." So Cloud will automatically
shrink everything down and preserve the stuff that you need to keep in there.
And if you're actually going to switch to a completely different task and you don't need that conversation history, then use {slash} clear to just wipe the slate clean and you're starting from a new conversation. But luckily you still have your cloud.md, you still have all the other files, so it's not like you're actually starting from scratch. So hack number seven is to always start in plan mode. So that means you can hit shift tab to cycle between modes or you just choose it manually. And once Cloud's in plan mode, it can still read, it can still research, but it won't actually change anything. So Cloud will outline the steps, it will ask clarifying questions, and it will map out the approach before writing a single line of code, which has been shown to improve
the quality. Now once you like the plan, you switch out of plan mode, tell it to execute, and this alone will dramatically reduce how many times that you have to go back and correct Cloud.
Hack number eight, we have to treat Cloud like a junior developer, which means don't always give it direct commands like, "Write me a function that does X," but try to understand how you can give it problems. So saying, "How should we handle growth tracking?" and let it think through the approach, because when it makes its own assumptions and it thinks through decisions, you can ask it to explain those. And this has also been shown to get better outputs when Cloud reasons through the problem first. So it's like plan mode, but now you're having it think a little bit deeper. Okay, hack number nine is to make Cloud ask questions. So a lot of times in plan mode, it will do this natively, but you can actually tell it to invoke its ask
user question tool. You can tell it, "Continuously ask me questions until you're 95% confident that you understand exactly what I need and exactly what you need to do." And once again, this alignment helps you from having to go back and forth with, you know, three or four rounds of revisions. All right, hack number 10 is build self-checking into the to-do lists. So you know how Cloud makes a to-do list when it starts building? Well, you can actually build verification steps right into that list.
So let's say one to-do is to build a website. The very next to-do could be take a screenshot of the website and check that everything looks right. And then maybe the next step is to open Chrome DevTools to use the browser and make sure that there are no actual errors in functionality. So you're now baking quality checks directly into the execution plan, so Cloud isn't just building stuff and handing it to you for feedback, but now it's building something, checking it, making sure everything's good, and then getting your feedback. And another cool thing that I like to do here is say, "Don't move on to your next to-do until you're 95% confident that that to-do is good."
Because it's AI, it's really hard to one-shot what you're looking for, but you'd rather have it one-shot 90% of the way there rather than one-shot 60 or 65%. Okay, so those were our beginner hacks. Now let's step it up a little bit. These next ones are for the people who are already kind of using Cloudcode a little bit and want to move faster.
[Chapter] Intermediate Hacks
All right, so hack number 11 is to deploy sub-agents for parallel work. Try telling the main session to use sub-agents in your prompt when you're working on complex problems. Cloud will spin up isolated sub-agents that each have their own context window. They can each be using their own model, and each agent works in parallel, which means the main thread stays clean while the sub-agents go to research, write tests, or explore different approaches. When they're done, they all report back to that main agent with their findings. So it's like having a team of developers instead of just having one. And you can even pair this with the model hack for cheaper tokens, which means you can have all the sub-agents running on Haiku for
simpler stuff and your main thread can stay on Opus. All right, hack number 12 is to build custom skills. This means you can create reusable prompt files in your {dot}cloud/skills directory. So for example, you can have one skill called techdebt.md, which tells Cloud exactly how to scan for technical debt. Or you can have one called codereview.md, which knows exactly how to review your code base. And then all you have to do is invoke that skill in natural language or