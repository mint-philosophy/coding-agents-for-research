# AI Agents for Philosophy

**Some first steps in using agents for philosophical research**

---

## Contents

1. [The Core Insight](#the-core-insight)
2. [First Steps: MacOS Fixes](#first-steps-macos-fixes)
3. [Linux](#linux)
4. [Context Engineering](#context-engineering)
5. [Project Structure](#project-structure)
6. [Initialization Protocol](#initialization-protocol)
7. [Session Management](#session-management)
8. [Skills System](#skills-system)
9. [What Agents Do For Me Now](#what-agents-do-for-me-now)
10. [Parallel Agents and Research at Scale](#parallel-agents-and-research-at-scale)
11. [Security Considerations](#security-considerations)
12. [Model Preferences](#model-preferences)
13. [Remote Access](#remote-access)
14. [Resources](#resources)

---

## The Core Insight

This is fundamentally about making computers do what you want them to do, without being constrained by bad or unfriendly software. It's not really about programming—I'm a philosopher, not a developer. It's about digital autonomy: escaping walled gardens, bypassing artificial constraints, and dramatically expanding what a solo researcher can accomplish in a day. I've been writing about this possibility ever since I first saw the "Toolformer" paper by Schick et al (e.g. [here](https://aeon.co/essays/can-philosophy-help-us-get-a-grip-on-the-consequences-of-ai), [here](https://onlinelibrary.wiley.com/doi/10.1111/papa.12279?af=R) and [here](https://arxiv.org/abs/2505.04345). But til recently it was just a prospect on the horizon. Now the horizon is here. 

Coding agents have the potential to make you dramatically more productive, not by automating your thinking but by removing friction from everything around it. Where I used to spend hours wrestling with platforms that didn't quite work how I wanted, or doing tedious data entry to make tools useful, or waiting for IT support that never comes—now I just describe what I want and an agent makes it happen... mostly.

---

## First Steps: MacOS Fixes

My entry point was trivial annoyances. Paste always inheriting formatting when I wanted plain text. Typo corrections requiring individual clicks when I wanted to accept them all at once and in general I hate going between keyboard and mouse. These are small things, but they compound. I asked Claude to figure out how to make "paste without formatting" the default behavior system-wide, and it worked. I asked for a keyboard shortcut that would accept all spelling corrections in the preceding paragraph, and that worked too.

The most satisfying early project was building an AppleTV-style screensaver from my processed drone videos. I wanted cross-fade transitions between videos, with selection governed by an exponential decay algorithm that prioritizes recent footage while still occasionally surfacing older material. This would have taken me hours of research, Stack Overflow archaeology, and trial-and-error. And honestly Claude didn't exactly one-shot it. But together we did eventually get something really effective working. A bunch of other little projects followed.

Each of these small victories revealed the same pattern: tasks that seemed to require specialized knowledge became accessible through natural language. The agent wasn't doing anything I couldn't have done myself with enough time—but "enough time" for these projects would have meant never doing them at all.

---

## Linux

The next step was setting up a new Linux system. I bought an Alienware Area51 with an RTX 5090 because I wanted serious GPU horsepower for local inference, but it came with Windows. Using coding agents on Windows still isn't great, and Windows itself is just viscerally unpleasant to use, so I installed Fedora 43 and basically used Claude to configure everything.

Linux has always felt completely inaccessible to me. The terminal commands, the weird off brand software packages, the dependency chains—it was a world I barely understood conceptually and definitely couldn't navigate practically. Claude Code changed that. I got the keyboard structured to feel like using a Mac, with all the same muscle memory and shortcuts. I installed, auditioned, and deleted applications rapidly, experimenting with alternatives in ways that would have been too tedious before. I changed the look, tweaked the behavior, and made it robust and unconstrained.

The most excessive project was building system-wide autocorrect running Qwen 3B on the GPU. This is complete overkill—a 3-billion parameter model for spell-checking—but it's a massive improvement over Espanso, which I found really frustrating to use (I tried a bunch of others too). More importantly, I love the fact that I have complete digital autonomy on this machine. No bossware, no telemetry I didn't consent to, maximal customization ability. I couldn't really justify the time I spent getting all this done (I have a couple of perfectly serviceable macs, that I can work fine on), but it was really fun, and it gave me some hope that I can maintain digital autonomy even as the primary operating systems become ever more locked down, even at the hardware level (eg InTune &c). 

---

## Context Engineering

The problem with CLI agents, though, is that it's easy to fall into a pattern where you don't cumulatively build from one conversation to the next. Each time you launch a new agent, you're basically starting afresh. Without careful attention, Claude might just rebuild something you've already set up, or reinvent a wheel you've already invented. There's no institutional memory (this is something lots of folks have talked about at length—I think Dwarkesh to the biggest audience).

This is where context engineering becomes crucial, and where switching to an IDE can really help. I experimented with Antigravity briefly but settled on Cursor because it allows access to a wider range of models. The nice thing is that since all these models are fluent in natural language, you can jump between them easily—it can be as simple as telling an agent to treat the `.cursor` folder the same way it treats `.claude`, or having it rewrite one configuration in another convention.

What I like about Cursor specifically is that it gives you clear panels for distinct purposes. One panel monitors multiple simultaneous agent conversations. Another is for focused conversation with one specific agent. A third shows file contents for viewing or editing, including PDFs. The fourth displays the project directory. These are all invaluable when you're progressing multiple projects simultaneously, because you can see at a glance what's happening across all of them and switch contexts without losing state. And it's useful for building the discipline of making all relevant context available to both you and your agent at all times.

---

## Project Structure

The foundation of making context engineering work is physical organization. I brought all of my work within one overarching folder, reorganizing things so that it would be relatively obvious to any new agent what was where. This folder lives on an external drive as a token gesture toward security—more on that later.

The folder hierarchy is straightforward. One folder holds active collaborations, with subfolders for each project. Another is for side-projects. I keep recent publications and work-in-progress papers accessible, as well as PDFs for papers I've been engaging with recently. Separate folders handle grant applications, meeting notes, and local copies of GitHub repositories we're working with.

The critical piece is the documentation protocol. Every project has three files that together define its state. The README describes static goals: what the project is, who's involved, what research questions we're pursuing. The LOG captures dynamic state—a session-by-session record of what's been done. The TODO lists immediate next steps. This triad ensures that any new agent can orient itself quickly, understand what's already happened, and know what needs to happen next.

---

## Initialization Protocol

The documentation protocol only works if agents actually follow it. This is where the initialization prompt comes in. Whenever I launch a new agent in Cursor—and I do the same when launching Claude Code in terminal—the first thing I do is run an `/init` command that tells the agent everything it needs to know.

The init covers several categories. First, metacognitive strategies: principles like "don't take shortcuts" and "evidence over claims" that shape how the agent approaches problems. Second, a strict documentation protocol: the rule that if it's not written down, it didn't happen. Third, clear prohibitions: things the agent should never do, boundaries it shouldn't cross. Fourth, skills scaffolding: pointers to capabilities the agent can draw on, with instructions for how to use them (if you don't know about skills, Simon Willison has a great [write-up](https://simonwillison.net/2025/Oct/10/claude-skills/)).

The key principles embedded in my init are worth stating explicitly. Evidence over claims means that "it should work" counts as failure—you have to actually verify. Document everything means no "I'll write this up later." Persistence over punt-backs means trying at least three genuine approaches before asking the user for help. Complete the checklist means all items, not just the comfortable ones. Think before acting means completing your reasoning before executing, especially for destructive operations.

---

## Session Management

Even with good initialization, there's a deeper problem: every agent is essentially a temp worker who only lasts 200,000 tokens. They're going to have to pick up from where the last one left off, and they can only do that if documentation is excellent.

Part of the  solution is session logs. Each agent creates a session log when it launches, so when I'm running multiple agents simultaneously they know who else is working on what. The log tracks what the agent is working on, what decisions it's made, what problems it's encountered.

The `/end` command is equally important. When an agent finishes work, running this command triggers a wrap-up protocol: archive the session log in a searchable location, capture things learned, document next steps, update the project's TODO and LOG files. This ensures continuity across agents. The session logs can later be searched if I want to track down some particular piece of work or understand why a decision was made. You can also search full transcripts when using  Claude Code itself.

---

## Skills System

Beyond sessions, there's a layer of accumulated capability called skills (developed by Anthropic but now widely adopted). These are reusable patterns that future agents can draw on instead of reinventing the wheel.

A skill is a package of knowledge about how to do something. Where a command is an instruction to perform some particular sequence of actions, a skill is a behaviour that might be used in a range of different sequences. 

For example, I have a `canvas-sync` skill for synchronizing TODO files, as well as research plans and weekly New's summaries with Slack canvases, a `notion-tasks` skill for creating and updating tasks in a Notion database, a more general `slack-posting` skill for posting messages to Slack or reading DMs. Each skill includes the relevant scripts ready to go, API keys in a known location, and a clear recipe for execution.

The skill structure means agents can work much faster with fewer missteps on project management tasks. When I ask an agent to add a task to Notion, it doesn't need to figure out the API from scratch—it loads the skill and follows the recipe. The same goes for posting to Slack, generating news summaries, processing meeting notes, and so on.

Skills also accumulate. When an agent finishes work, part of the `/end` protocol is reflecting on whether anything it did should become a skill for future agents. Agents aren't perfect at recognizing reusable patterns, but they get better with clearer documentation, and the skill library steadily grows.

---

## What Agents Do For Me Now

With this infrastructure in place, I'm now trying to fit agents into basically every aspect of my work. I'm not sure there are any tasks I'd want an executive assistant or research assistant to handle for me that I wouldn't now give to an agent first—with the exception of tasks where agents are artificially hobbled by platforms that deny them access. (That's a topic I'll be writing about properly soon, with a bunch of collaborators.)

Meeting notes are a great example. I have a meeting with a collaborator, Gemini transcribes it, and then I have a sript convert those notes into markdown and copy them to a folder in my project directory. An agent processes them, I talk through things we came up with, and together we extract the most important points for moving forward—often including insights that would otherwise evanesce before I got around to writing them down.

Platform management is another area where agents really help. The value of tools like Notion and Slack depends on giving them lots of data to work with, but entering that data is super tedious. Agents make it effortless. I don't directly add entries to Notion databases anymore; I ask an agent to do it, and to fill in all the metadata fields that are useful after the fact but boring to populate in the moment. Updating slack is now much easier--and it's easier too to keep a few different surfaces synchronised. 

And agents have obviously been great for working with actual code. Now when I read a CS paper I give an agent access to the repo, and I can then ask it all the questions I have that the paper doesn't answer. And of course I can use the agents to help me build pilot experiments to explore my ideas further. The final experiment will have to be coded more rigorously, but the barriers to exploration are now almost invisible.

Agents are also excellent for escaping walled gardens. I wanted to get away from Office 365 because it comes with too much employer control and involuntary AI integration. But Microsoft To Do held me hostage through accumulated context—years of tasks and notes that would be tedious to migrate manually. Agents helped me extract all that content through screenshots, then create a new database in Notion where I can structure things however I want. And now I can allow my agents to manage tasks, tag them, monitor them for when they get stale, and file them away when done. Similarly, I find some of the controls on my exchange calendar very frustrating, so used agents to create a script that copies work calendar events to Gmail, where I can do whatever I want with the API.

---

## Parallel Agents and Research at Scale

It's cool having one automated software engineer at your beck and call 24/7. It's even cooler to have 40 of them. So I've been finding projects that really scale, and seeing whether I can set large teams of agents working on them. 
The most ambitious thing 

For example, for a project on agent infrastructure, I had Claude agents build a large database of relevant technologies, protocols, and standards. Then I divided the database among multiple agents for verification—each one checking the work of the initial pass. The resulting dataset has about 600 entries, each meticulously researched.

This was experimental, and it's taken me up against the limits of these systems' capabilities (or perhaps my ability to get the best out of them). Getting multi-agent projects to work is really hard. Context limitations are the biggest problem, but also it's a matter of orchestration and coordination of agents (and the two things interact). There are a few ways to go. If you just have Claude spawn subagents, things look superficially like they work, but you're likely to hit rate limits fast, and the subagents lose stats really badly. Else the subagents do a poor job of managing their context, and run out. If they compact, then they start making mistakes and acting out of sync. If they don't compact then they're just stuck, and you can get orphaned entries in your database that are marked as done. 

In general, I think the biggest improvement that could be made, now, in getting these agents to work would be if they knew when they were about to run out of context, and could tie off sensibly within their limits, preparing the ground for their successor. I have created a "hook" for Claude code to do this, but so far it hasn't worked. Will keep experimenting.

Otherwize, the only real solution is to break each task into chunks so that a single agent can complete each chunk within its context window. The best way to do this is to set up one agent with all the necessary context, then fork it, giving each fork a sub-component of the larger task. 

Imbue's Sculptor app is key here (Claude code allows forking sessions too, but it's a bit fiddly). Sculptor allows you to configure one agent properly, then split it into multiple instances, each tackling a piece of the problem. This has been easily the most reliable agent orchestration method I have tried, significantly more effective than just leaving things in Claude's hands to orchestrate subagents. If agents were better at coordinating with each other, or if they worked properly over really long contexts, forking might not be necessary—but even then I suspect it would be beneficial.

Once you can get the agents working together at scale, the next and probably deeper issue is verification. AI can generate enormous amounts of content, but you want to avoid generating slop for humans to sift through. You can verify as much as you like with AI, ultimately it has to be parsed and processed by a human brain. And I'm not yet sure whether we'll end up with really useful stuff, or just s lot of makework. So this remains a research project—we're interested in finding out whether doing research this way produces robust content that ultimately saves time rather than draining it. My sense is that it will, but it's a substantial verification job and won't be complete until mid-January.

---

## Security Considerations

I've been pretty reckless about security. `--dangerously-skip-permissions` all the way. My only defenses are multiple redundant backups of everything and three different computers I can use if one gets borked. I've also held off from giving agents access to my email, just in case—though I'd really like to remove that constraint, because this is the first time I've actually wanted AI help managing my inbox.

Imbue has a better approach: Sculptor runs all agents in Docker containers, which limits what they can do. But there's a learning curve since it's built around Git, and it means you can't easily give each project the same rich context without a lot of duplication.

Cursor occupies a middle ground. It allows agents to run fairly freely for the most part but enforces some reasonably bright lines they won't cross. It's not perfect, but it's workable.

My mental model is that agents could be compromised at any moment, or could make some catastrophic error, so everything has to be robust against that eventuality. This is probably the right way to think regardless of what precautions you take.

---

## Model Preferences

I've tried all the major models extensively. I keep coming back to Claude Opus 4.5 for the hardest tasks—it's consistently the winner when something genuinely difficult needs to happen. I also appreciate that Claude doesn't just refuse when I ask it to do something outside its comfort zone. It will explain why it's hesitant and is open to counterarguments. Codex, by comparison, is a robot.

For normal work, I prefer running Opus in the Cursor harness because context engineering is better in the IDE and I value not being locked into one model. But for really hard tasks I'll drop into the terminal with Claude Code directly. Likewise when working remotely, when I'm stuck in terminal anyway. And for parallelizable work, Sculptor.

A note of caution: Gemini 3 Pro and Codex have both made catastrophic mistakes at various points. The worst was Codex messing up my fstab on the Linux laptop so that it wouldn't boot. Claude has never done anything comparably destructive. Your mileage may vary, but I now treat non-Claude models with extra care on anything system-critical.

---

## Remote Access

I've set up Tailscale and Termius on my phone so that I can talk to agents remotely. This is useful when I'm away from my desk but want to kick off some work or check on progress. It's a bit of a work in progress tho. The main problem is that connections often drop and your agent doesn't continue running async. For this reason I'll often just use chrome remote access so that if I go out of reception my agents will keep working.

My next side-project for the new year is making this hands-free—being able to talk to agents by voice from anywhere, without needing to type. I'm confident it's feasible; I just need to work out the details.

---

## Resources

Several recent resources have been particularly useful in thinking about this workflow. Steve Newman's writing on hyperproductivity captures much of the opportunity I've been exploring. ([Link](https://secondthoughts.ai/p/hyperproductivity)) Xu et al.'s work on context engineering provides a more systematic framework for thinking about how to give agents the context they need. ([Link](https://arxiv.org/abs/2512.05470)) Shah et al.'s paper on Human Context Protocol addresses the problem of making human preferences and context legible to agents at scale. ([Link](https://ssrn.com/abstract=5403981))

I've cobbled this all together from a bunch of different sources, as well as a bunch of trial and error, so I'm curious to see other approaches and ways to make things more effective or efficient. I'm not drawing broader lessons here—just sharing what has worked and what hasn't, so that others can try something similar.

---

## Repo

Rather than just share artefacts piecemeal I'm trying to set this up as a repo that you can clone and implement, or else just have your agent ransack for ideas about how to improve your own system. You can find a guide to what's here at the [README](/readme.html).

---

## Gaps and Next Steps

A few things I'd still like to figure out. I want to set up automations where agents run certain tasks on a schedule—I'm sure it's feasible but haven't worked out the details. I'd like to find better solutions for the security question that don't sacrifice too much convenience. And I'm curious whether the research-at-scale workflow actually produces a net time savings once verification is complete. And I would like to figure out how to run multiple agents more effectively and efficiently. Going to spend some time with Claude Code's fork session command next.

I'll be keeping this repo updated; new projects and results will be shared in the [Guide](/guide.html).
