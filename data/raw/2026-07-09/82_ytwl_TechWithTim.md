---
title: "How to Build an App With Claude Code - Full Tutorial for Beginners"
author: "Tech With Tim"
platform: YouTube
source: youtube_watchlist
source_type: watchlist
source_platform: youtube
channel: "Tech With Tim"
url: "https://www.youtube.com/watch?v=GUgxx6fMiR8"
origin_flag: "english_source"
lang_hint: "en"
query_track: "Claude Code 教程源头（英语原创）"
collected: "2026-07-09"
subtitle_available: true
subtitle_source: "opencli-transcript"
---

# 字幕正文（来源：opencli transcript）

[Chapter] Overview
Today, I'll show you not only how to build, but also how to deploy a full web application using Claude code.
I'll walk through every step as if you're a complete beginner.
By the end of this video, you can have a fully functioning application.
This deployed on your own domain that other people can actually access.
Let's dive in.
[Chapter] Installing Claude Code
So to get started here, there's a few things that we should download and install.
Now. First of course is client code.
In order to use Claude code you do need a premium subscription.
With Claude’s, you are going to have to pay for this, just like really any of these AI tools, but you can download it once you have that subscription by going to the website, which I'll leave a link to down below.
You can download the desktop application or run this command, which is going to install the terminal application for you that you want the terminal application.
This is what we'll be using in this video, because it's going to be better for the deployment process.
And what I mean by that is that Claude has its own desktop application.
Right. So you can download Claude and open it.
You could see I was brainstorming some video ideas here.
And you can switch over to this code tab where you can start using it from this view.
Now this is fine, but it's a lot easier to use Claude code directly from the terminal where what you do is you open up a terminal like so and you type the command Claude.
This will then run Claude code for you directly inside of the terminal.
Now, I know a lot of you already have this downloaded, but if you don't, what you're going to do is open up your terminal.
Whether you're on Mac, Linux, or Windows, and you're going to paste that command that you found from this website.
So curl F XL, whatever, and then just run it.
When you do that, it's going to download and install Claude code for you.
And then once that's finished you can invoke Claude code by typing the command clod.
When you do that it's going to bring you inside of here.
You'll likely need to authenticate to sign into your account, and then you're good to go.
Now, once you've got Claude code installed, the next thing that you're going to want is download some type of code editor or ID now I recommend cursor, but you can really use anything that you want as long as there's a VS code fork.
[Chapter] Installing Cursor
Because to deploy the project we're going to use a cool extension, which we'll have a look at in a second.
Anyways, for now I'm just going to go to the cursor website.
This is a place where you can write code and you can view all of the files.
This is free to download.
You can simply press the button and download it for windows, Mac or Linux.
Again, I'll leave a link to it in the description free.
Just download it, install it and then you are good to go.
Now at this point, assume that you've installed Claude code and you have some type of code editor for it.
Now, in case you're wondering, once we build the application, we're going to use a platform called hosting or to deploy it.
There are a long term partner of mine, but anyways we'll talk about that later.
Okay.
So for now, once we've got that all installed, what we're going to do is just open up cursor on our computer. So just find that application.
I'm just going to search for it in the spotlight search.
[Chapter] Cursor Setup & Walkthrough
And what we're going to do is just make a new folder where we can put our application.
So we're going to go file.
We're going to go to open folder from cursor.
We're going to go to our desktop or any location that you can remember.
And what I'm going to do is just make a new folder.
And I'm going to call this my site code.
Anything that you want.
If you have an idea of what it is that you want to build.
Okay.
So now what we've done is we've opened up a new folder inside.
Of course, they really don't need to know too much about this.
This is just a tool that we're going to use to be able to view the different code that we're generating, and it makes it a little bit easier for us to understand what's going on, to add an image and to eventually deploy the site.
Now we're going to use Claude code directly inside of cursor.
So there's no need to worry about this kind of agent tab that's going to appear when you get into the editor.
So we can just go ahead and close that.
Now, this is what's called a fork of a popular editor known as Visual Studio Code.
So if you've ever used that before this is effectively the exact same thing.
It just has some AI features built in.
You're going to see a ton of stuff here.
Again, don't confuse yourself.
Literally all you want to do is just look for this little file menu on the left hand side.
You can see that it kind of looks like two files.
You should see that my site is open.
And now when we start generating code, we're going to see all of it appear on the left hand side.
Here you can move windows around.
You can reorganize it if you want.
You can collapse the sidebar.
But that's really all that you need to know okay.
So from here what we're going to do is we're going to look for this little extensions icon.
It might have moved, it might go somewhere else.
But we're looking for something called extensions which looks like these kind of little puzzle pieces.
You also might have to find it by expanding this right here to see all of the different options.
Now, what we're going to start by doing is installing the clawed code extension inside of this editor.
So you'll see we have Claude code.
Mine's already installed.
But all we're going to do is search for it and then press install okay.
And that should install Claude code for us.
Now the next extension we're going to install while we're here is the hosting or extension, which we're going to use later to actually deploy our site.
So you can go to Hostinger.
Just search for it again find this hosting or connector.
And then just go ahead and press on install.
We're going to trust the publisher and then install that inside of our editor.
That's it. We have the extensions.
And now we can start building our app.
So what we're going to do now is open up Claude code inside of this editor.
Remember I told you that you could open it in the terminal.
You also can open it directly inside of these editor so you can view the files.
So to do that you can press this little down arrow and you can find this clod code icon.
You'll see I have some icons here you don't have because I have other extensions.
So I'm just going to press on Claude code.
And you'll notice that it's going to open for us kind of a new session view right here.
And we should see we have web.
We have local.
And we can press this button new session.
Then when we press new session it's going to open a new Claude code session for us hopefully in the big view.
If you want to move it around, you can drag this window and kind of change the size of it.
And here we can start prompting Claude to actually generate stuff for us.
Now I'm also just going to go back to the file view.
So we have the files on the left hand side and Claude code on the right.
Now you'll notice here that there's an option that says prefer the terminal experience which is back in the settings.
[Chapter] Setting up Claude Code
So if you've used Claude code before, you know that you can use it from kind of this really terminal environment where it's not very pretty.
There's not like a graphical user interface.
But right now we're inside of this clean UI that it's created for us.
So if you want to go back to the terminal, you could press this button.
Right.
And we can change it so that we're launching it in the terminal rather than in the native UI.
Now, for most of you, especially if you're a beginner, I'd recommend you just keep it in the default view.
But if you want to change that, you can directly from the settings here in cursor.
Okay, so from here just a few quick options to go over.
You'll notice that there