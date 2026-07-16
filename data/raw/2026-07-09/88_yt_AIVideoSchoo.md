---
title: "Timestamp Prompts: Narrative Control for AI Video (Runway, Veo, Sora, Kling)"
author: "AI Video School"
platform: YouTube
source: yt-dlp + cookies
source_type: aggregator_discovery
source_platform: youtube
channel: "AI Video School"
views: "收看次數：10,012 次"
likes: ""
duration: "10:34"
published: "6 個月前"
video_id: ""
url: "https://www.youtube.com/watch?v=t_QLoXw8hDU"
keywords: ""
subtitle_language: "N/A"
subtitle_available: true
origin_flag: "english_source"
lang_hint: "en"
query_track: "赛道2-AI视频"
collected: "2026-07-09"
subtitle_source: "opencli-transcript"
---

# 字幕正文（来源：opencli transcript）

[Chapter] Intro to timestamped prompting and the models we'll be testing
One thing about AI video that frustrates both experienced [music] professionals and new AI filmmakers is the lack of control. For me, AI would lose a little bit of magic if it were too predictable, but sometimes timing is [music] everything when you're trying to tell a story. Enter timestamped prompts.
[music] I used a timestamp prompt in my movie The Album where I performed a rack focus between characters as they performed dialogue. Even a few years ago, I remember using timestamped [music] prompts for stable diffusion to forum videos like this one that changes decades every 10 seconds. The reason I'm thinking about timestamp prompts now is because Runway just released their 4.5 model. [music] In the documentation under advanced prompting, they specifically mention timestamped prompts. So, I'm going to try out a few
using runway and then I'm also going to use Leonardo AI to compare those same prompts with other models like VO, Clling, Seance, LTX, Sora, uh just to give you a sense of which models currently work best with timestamps.
[music] Here is Runway's example prompt. I'm more of a cat person. So, I'm going to copy that prompt, but change the corgi to a cat.
[Chapter] Modified Runway Example
[music] I want to try another timed prompt that includes a camera movement and two things that are hard for AI. A person eating and a bird flying. We'll use this prompt of an elderly woman in Paris eating a croissant. A little sparrow flies in. She tries to feed it, but it flies away. Let's try this in runway.
[Chapter] Testing: Camera Motion, People Eating, Birds Flying -- all at once!
Now, let's go to Leonardo and try some other models.
[Chapter] Dramatic turn of events (private investigator scene)
Let's try one of those classic movie scenes where a private investigator goes to a home to interview someone, but it's too late. In this first version, let's have her knock, wait, peek inside, then recoil in horror.
Cling 01 is a really great model, but I noticed it's doing terrible with these timestamped prompts. This is why it's important to ensure that we're prompting for the model we're using. Uh the timestamps work better in runway vio and sea dance because cling doesn't understand timestamps. It wants natural language like suddenly or immediately.
So we're not necessarily getting bad results from cling. We're just giving it bad prompts that it doesn't know what to do with.
[Chapter] Using a start image with timestamped prompts
As of this recording, [music] runway 4.5 is text to video only. So we have a different private investigator each time. So I used Leonardo to make an image with Flux. So now we'll use this start image of our Snoopy investigator uh for the models that support a start frame.
Can I help you with something?
Evening. Just checking to see if you're home before I knocked. Hi, I'm Maya Walker. Hey, how's it going? I was just passing by and thought I'd stop in. [sighs and gasps] Oh, hi. I was just admiring your lovely treat. So, last here I wish you prick.
Hey.
Hey.
How are you doing?
[Chapter] Stylized clips sometimes work better than cinematic in Runway?
In some of my initial tests, timestamped prompts in Runway work better with stylized videos than realistic or cinematic video. For instance, all I did was add pixel art style to the front of this prompt. Let's examine the timing here.
[music] So depending on the kind of content you're creating, the model may do better or worse with the timed prompt. As I often do, I trained a GPT on the runway documentation and asked for a prompt that showcases the best use for timestamps. Um, it gave me this one, which is a good technical example, but the results aren't my favorite. AI is always going to love Cyberpunk and steampunk. Like, I get what they're trying to do.
[Chapter] Prompts from a Gemini Gem trained on Runway
We start with a macro lens, we go to a midshot, and then we go to the really wide shot. All based on timings. But I would rather go back to the beetle and watch the beetle fly away. He knows it's going to work. And then we get to see it actually working. Then I asked my GPT sidekick for what is sometimes called a Spielberg warner optimized for runway. And it gave me this jungle scene. It's okay.
And then I wanted A suspenseful domestic scene.
[Chapter] Prompt structure: use a natural language prompt, then append timestamps
One thing I want to highlight about the timestamped prompt is Runway's recommendation to frontload all of the action like a normal text prompt and then you provide the timestamped breakdown. It's kind of how you would explain it to anyone. Like this is what this scene is about. And then here's the blocking and the camera motion and the sequence of timing to make that happen. Just to be clear, timestamps [music] aren't needed in every prompt you write.
[Chapter] Which are the best models for timestamped prompts?
I'd actually encourage you not to do that. If you find you need a little more control, just make sure the model you're using understands them. Vio C dance runway Sora
LTX2 Pro.
You're leaving.
They all seem to do well with timestamps. All right, hopefully this was helpful. Subscribe to my Substack where I write the occasional newsletter. [music] And if you're still watching, here are some outtakes.
[Chapter] Watch some funny outtakes!
Oh, you're home.
Oh, hey there. I was [music] just admiring the window.