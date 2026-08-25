# AI Coding Workflows course
## Prompts

This file contains every prompt used in the course, along with short notes on when to run each one and what to check before you do. Keep it open as you follow along. The notes around each prompt matter as much as the prompts themselves.

> **Before you start:** the repo is organized into folders by lesson range (`Lessons_02-08`, `Lessons_09`, `Lessons_11-12`), each holding the project files as they should look during that stretch of the course. If you're following the course in order, you only need `Lessons_02-08`; the prompts below create everything that appears in the later folders.

### Lesson 2 in Claude Code

Run this after entering the three spec files, to set up the project dependencies:

```
Read @specs/tech-stack.md then create a requirements.txt and update the virtual environment from that.
```

### Lesson 3 in Claude Code
```
Look in @specs/mission.md and @specs/tech-stack.md for project details.
Look at the @specs/roadmap.md and:
- Implement each task one at a time from Phase 1 and Phase 2.

Do not fix anything after the subagent. Do a review and provide a list of critical mistakes.
```

### Lesson 4 in Claude Code
```
Look in @specs/mission.md and @specs/tech-stack.md for project details.
Look at the @specs/roadmap.md and:
- Implement Phase 1 using a **new spawned** @general subagent.
- Implement Phase 2 using a **new spawned** @general subagent.

Do not fix anything after the subagent. Do a review and provide a list of critical mistakes.
```

### Lesson 5 in Claude Code

```
Look in @specs/mission.md and @specs/tech-stack.md for project details.
Look at the @specs/roadmap.md and:
- Implement Phase 1 using a **new spawned** Haiku subagent.
- Implement Phase 2 using a **new spawned** Haiku subagent.

Do not fix anything after the subagent. Do a review and provide a list of critical mistakes.
```

### Lesson 6 in OpenCode

Configure OpenCode to use OpenRouter as a provider. Replace `YOUR-API-KEY` with the API key you created on OpenRouter. Don't share that key with anyone.

```
Set up OpenCode to use OpenRouter as a provider with an API Key of YOUR-API-KEY
```

Then trim the model list down to the two models used in this course:

```
Edit the global OpenCode configuration file to have the following:
- Only list DeepSeek v4 Pro and DeepSeek v4 Flash as OpenRouter models
- Don't list any OpenCode provider models
- Set medium reasoning for both
```

### Lesson 7 in OpenCode

```
Look in @specs/mission.md and @specs/tech-stack.md for project details.
Look at the @specs/roadmap.md and:
- Implement each task one at a time from Phase 1 and Phase 2

Do not fix anything after the subagent. Do a review and provide a list of critical mistakes.
```

### Lesson 8 in OpenCode

```
Look in @specs/mission.md and @specs/tech-stack.md for project details.
Look at the @specs/roadmap.md and:
- Implement Phase 1 using a **new spawned** general subagent.
- Implement Phase 2 using a **new spawned** general subagent.


Do not fix anything after the subagent. Do a review and provide a list of critical mistakes.
```

### Lesson 9 in OpenCode

Lesson 9 uses two prompts. First, create the `implementer` subagent. (The `Lessons_09` folder already contains the finished file, so if you're working from that folder, delete `.opencode/agents/implementer.md` before running this prompt and let it recreate the file.)

```
Create an "implementer" subagent:
- This subagent should use an openrouter/deepseek/deepseek-v4-flash model
- The main goal of this agent is to generate code and implement tasks delegated to it
```

Then run the implementation prompt:

```
Look in @specs/mission.md and @specs/tech-stack.md for project details.
Look at the @specs/roadmap.md and:
- Generate Phase 1 spec for the implementer subagent with task list
- Spawn one new implementer subagent at a time and delegate implementation of each task in Phase 1 spec list. New @implementer subagent to each task.

Then do the same steps for Phase 2.
- Do not write the full code file for/instead of subagents, only suggest snippets.
- Do not make fixes after subagents.
- Do a review and provide a list of critical mistakes.
```


### Lesson 10 in OpenCode

Connect OpenCode to your local LM Studio server. The URL below is LM Studio's default, and the model ID matches the Mac (MLX) build. Check both in LM Studio's Developer tab and swap in yours if they differ (Windows/Linux GGUF builds have a different model ID).

```
Set up OpenCode to use the local LM Studio hosted model 'gemma-4-12b-it-mlx' available at http://127.0.0.1:1234

add it to the models list in the global OpenCode configuration file
```

### Lesson 11 in OpenCode

First, split the roadmap so each phase is small enough for the local implementer model. (The roadmap in the `Lessons_11-12` folder already has this split, so skip this prompt if you started from that folder.)

```
Edit the @specs/roadmap.md Phase 2 and move the work for the add complaint form, starting at "A form at the bottom with,", into a new Phase 3. Make sure Phase 2 and 3 have validation tests.
```

Also switch your implementer subagent to the local model. The updated `implementer.md` is in the course repo at `Lessons_11-12/.opencode/agents/implementer.md`. Copy it over yours. Note it references the Mac (MLX) Gemma model ID and a Mac/Linux-style `.venv/bin/python` test command; on Windows, adjust to your model ID and `.venv\Scripts\python`.

Then run the implementation prompt below. It handles **one phase per run**, so you'll send it three times: first as written, then with "Run only Phase 1" changed to "Run only Phase 2", then changed again to "Run only Phase 3".

```
Read @specs/mission.md, @specs/tech-stack.md, and @specs/roadmap.md. Run only Phase 1.

Read the phase's target files, then delegate this phase exactly once to a fresh `@implementer` subagent with a compact, self-contained packet: repo-relative writable paths, complete required final state, and exact behavior/tests to preserve. Do not refer the child to specification files or include file contents. Do not provide complete files, complete functions, code blocks, pseudocode, or line-by-line implementations. Include exact literals, imports, route signatures, API constraints, test semantics, and preserved behavior when they are contract requirements.

Include this exact instruction: "For every writable file, use `write` with its complete final content; never use `edit`." Do not modify phase files or use another agent.

Tell the child this is its final tool call and it must stop whether it passes or fails: `.venv/bin/python -m pytest tests/`.

After it returns, use only `read` on the reported changed files. Do not use Bash, glob, task, edit, or write. Report the exact validation result, files changed, and only critical contract violations: missing required strings, routes, imports, or unexpected files.
```

### Lesson 12 in OpenCode

Lesson 12 continues from Lesson 11's setup: the split three-phase roadmap and the local implementer. If you're jumping in here, start from the `Lessons_11-12` folder, which has both in place.

Connect OpenCode to the Qwen model in LM Studio. As in Lesson 10, the URL below is LM Studio's default and the model ID matches the Mac (MLX) build. Check both in LM Studio's Developer tab and swap in yours if they differ (Windows/Linux GGUF builds have a different model ID).

```
Set up OpenCode to use the local LM Studio hosted model 'qwen3.5-27b-ud-mlx' available at http://127.0.0.1:1234

Add it to the models list in the global OpenCode configuration file.
```

For the implementation, reuse the **Lesson 11 implementation prompt**, phase by phase, exactly as before.

If the review reports issues, tell the main agent to send the fixes back to the subagent, e.g. `Have the @implementer fix <the reported issue>`.

