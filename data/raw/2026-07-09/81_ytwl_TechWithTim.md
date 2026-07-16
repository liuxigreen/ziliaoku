---
title: "Claude Code - Full Tutorial for Beginners"
author: "Tech With Tim"
platform: YouTube
source: youtube_watchlist
source_type: watchlist
source_platform: youtube
channel: "Tech With Tim"
url: "https://www.youtube.com/watch?v=ntDIxaeo3Wg"
origin_flag: "english_source"
lang_hint: "en"
query_track: "Claude Code 教程源头（英语原创）"
collected: "2026-07-09"
subtitle_available: true
subtitle_source: "opencli-transcript"
---

# 字幕正文（来源：opencli transcript）

[Chapter] Overview
This video will teach you Claude code.
I'll go over everything and assume no prior knowledge.
I'll walk you through the setup and installation.
Step by step.
I'll show you how to utilize the tool, the best practices, multiple features, and by the end of the video, you'll be comfortable using this tool to generate some pretty insane outputs and awesome coding projects.
So with that said, let's get into it.
[Chapter] What is Claude Code?
So without getting into too many details, cloud Code is effectively a command line or terminal application that allows you to generate code, debug projects, make websites, create applications, whatever it is that you want.
It is effectively anthropic version of, you know, cursor or something, right?
Where you can generate a bunch of code using the terminal.
Now this is prompt based coding, which means you don't need to actually write any of the code yourself.
You simply type to an AI agent, you tell it what your desired output is and then goes ahead and starts coding.
Now, oftentimes cloud code will be used in combination with other developer tools, and I'll show you a few of them in this video.
But generally speaking, you do not need to be an expert to use this.
And even as a complete beginner, you can create some really cool projects.
So with that said, let's look at how we set it up.
Now, in order to get cloud code working, you are going to need a cloud subscription which is paid.
[Chapter] Claude Code Setup
So you're going to need a Pro Max teams or enterprise subscription or an API key with some tokens or credits from the cloud console.
Now, I would suggest that if you're just looking to mess around with this, get the cheapest plan from cloud.
You will run out of credits pretty quickly if you are using this for very heavy work.
But of course, test it first before you start going and buying a bunch of different credits.
It also matters what model you're using, which we'll talk about later, which will determine what the overall price for all of the prompts that you send is going to be.
Now, generally, you're not going to be overbuild.
You'll just run out of credits, then you would have to buy more.
So don't worry about that.
Okay.
Now to install this is going to require that we work directly inside of the terminal.
So what we're going to do is we're going to open up a terminal or a command prompt or a PowerShell instance, depending on the operating system that you're working on.
Now, if you are on windows, then I'm going to suggest that you open up PowerShell so you can go to the windows search bar, search for PowerShell, and then open up a terminal like this.
And I'll just put it on the right hand side of my screen.
Now if you're on Mac or Linux then open up a normal terminal.
So just type terminal in the spotlight search.
And then you'll be in an environment where you can start using cloud code.
Now in order to install this I'm going to leave this documentation in the description which gives you the commands that you can simply copy depending on your operating system.
So if you were on Mac or Linux then you can copy this curl command right here.
Just paste it into your terminal and run it.
If you are on windows and you're using PowerShell as I suggested, then you can copy this IRM command.
You can paste it, hit enter, and it should install cloud code for you.
If you're using the command prompt, maybe you're on an older version of windows.
Then you can copy this version right here.
Paste it in the command prompt.
Again, it will install the tool.
Cloud code is not a desktop application.
It actually runs directly inside of your shell or your terminal.
So in order to use this in the future, you will need to open up PowerShell again or terminal again, or use this from some kind of tool in order to actually interact with cloud and generate code.
Now, once it says it's installed, the way that you can test this is by simply typing Claude in your terminal.
So if you type Claude, you should get some kind of output here.
Now when you first run this, it will ask you to authenticate with your anthropic or cloud account.
So just do that.
Go into your browser, sign into your account and then you'll be good to go.
Now also whenever you run this for the first time and you type that command, it's going to ask you to trust the current folder that you're inside of.
So we're going to go ahead and press on. Yes I trust the folder.
And then it's going to bring up the Claude Code UI.
Now at this point you should have got cloud code installed and just remember, if you were to close the terminal or the PowerShell you would have to reopen this.
Right?
I'm just going to zoom in and then again type Claude and then you can press enter.
And again you get back into that user interface.
So don't worry if you lose it.
Now for some of you that are complete beginners and already this is a little bit intimidating.
Anthropic actually did create an easier way to write code using Claude.
It is not the same thing as Claude code, but it is very similar and you can access that by downloading the desktop app for Claude.
[Chapter] Desktop App
So if you have an account with them, you can just download the desktop app.
If you do that, the app will look something like this.
From here, what you'll be able to do is switch between this chat and this code mode.
And if you go into the coding mode here, you'll be able to select a project.
You can write a prompt directly inside of here you can change the mode like coding, asking, planning, right. You can add different files.
You can connect it to GitHub, you can choose your model and it's a lot simpler and easier to use.
So again, if you're a beginner you can just use this.
But if you want to get any serious work done, the CLI or the command line tool which I'm showing you is what you're going to want to set up and have on your machine.
Now, if you've been programing for a while, you probably know the job market is tough recently and you may feel like traditional resumes just don't show who you really are as a creator or a technologist.
Now that's where dinked me comes in.
It's a brand new AI native career network built for the real era of real work, real projects, real impact.
Not just job titles.
Now, instead of a static resume, Dink gives you a living identity card your Dink card that automatically showcases your code, papers, citations, and measurable impact across platforms like GitHub and Google Scholar.
Recruiters, professors, and startups can discover what you've actually done, not just what you wrote on paper.
Now that's what dink does for you, but for companies.
Dink is an AI powered talent engine that analyzes and compares researchers and engineers in seconds.
It helps teams spot the best fits faster than traditional recruiting tools.
Now, the best part of all of this is that you can claim your Dink card for free.
Start building your personal identity in minutes and let your work speak for itself.
In a world where resumes get screened for six seconds before a decision.
Now here you can even see my dink card.
Right here has all of my details, information that you wouldn't see on a resume, my whole career trajectory, my GitHub, the number of stars, my YouTube channel, Instagram, all of that stuff is here.
As well as networks career trajectory, Twitter, and anything else that you want to include.
Now you can get started with Dink today for free by clicking the link in the description, and a massive thanks to them for sponsoring today's video.
Let's get back into it.
Now, with that in mind, before you just go crazy here with Claude, what I'm going to suggest that you do is installed git on your computer.
[Chapter] Other Dependencies
Now, git is a tool that's going to allow you to essentially kind of checkpoint what Claude is doing and revert back to a previous version of your code base in case it makes any mistakes.
You won't have it by default on your machines.
You do need to install.
Now.