# Last Week in AI — Dec 10 – Dec 17, 2025

## Normative Competence

**Artemis: evolutionary optimization for LLM agents as black boxes.** Brookes et al. present Artemis, a no‑code platform for optimizing multi-component LLM agent configurations—prompts, tool choices, and other mixed discrete/continuous parameters—without changing the agent's architecture or building differentiable objectives. The paper frames the agent as a black box, then uses evolutionary search with "semantically aware" mutation/crossover operators and hierarchical evaluation (cheap scoring passes before expensive benchmark runs) to explore configuration space efficiently. The core pitch is accessibility and generality: treat "agent tuning" as an automated system that can discover and optimize the knobs you already have, rather than a bespoke research project per agent scaffold. ([Link](https://arxiv.org/abs/2512.09108))

**How should a principal choose a winner in a debate game?** Heckett and Conitzer develop a formal model for "debate games" where a principal must select a winner between two strategic debaters with private information, under constraints that arguments must be verifiable and state‑consistent. They define several classes of debate games and decision rules ("policies") and then analyze what is computationally feasible: evaluating a policy is polynomial-time, but finding a perfect (zero-error) policy is NP‑complete. ([Link](https://www.arxiv.org/abs/2511.23454))

*Also this week:* Simon Willison points to a shift in the practical plausibility of "LLM-based verification," noting that while LLMs are notoriously error-prone, top-tier models paired with search tools can now deliver credible "fact check this" style outputs when prompted carefully. ([Link](https://x.com/simonw/status/2000841629960430055))

---

## Agents

**SIMA 2: a generalist embodied agent for 3D virtual worlds.** The SIMA team describe a Gemini-based vision‑language‑action agent that operates directly from pixels using keyboard/mouse actions, aiming for cross‑world generalization and an open‑ended self-improvement loop. A central design point is a unified multimodal token stream that interleaves internal reasoning, dialogue, and low-level actions, plus "bridge data" intended to causally align what the agent says/thinks with what it does. ([Link](https://arxiv.org/abs/2512.04797))

*Also this week:* Google's Gemini account demos a "rent a car" flow where the agent compares prices, pulls required details from email, and books end-to-end from a budget constraint. ([Link](https://x.com/geminiapp/status/2000616120106221781)) Yam Peleg describes wiring Claude Code to WhatsApp and building a larger personal automation stack from a phone-first interface—an anecdote about how quickly scaffolded agentic tooling can become an end-user "operating system." ([Link](https://x.com/yampeleg/status/2000642897402880491))

---

## Capabilities

**NVIDIA's Nemotron 3: an "open models + infra" push for multi-agent systems.** NVIDIA announced the Nemotron 3 family (Nano/Super/Ultra) alongside data and libraries, positioning the release as infrastructure for efficient, transparent multi-agent systems rather than a single chat model. The story is less "one model beats another" and more "a vendor is trying to define a stack for agentic deployment with unusually broad openness." ([Link](https://nvidianews.nvidia.com/news/nvidia-debuts-nemotron-3-family-of-open-models))

*Also this week:* Percy Liang flags Nemotron as notable partly because it goes beyond releasing weights, pointing to releases of training data, RL environments, and code as a different kind of "open" posture. ([Link](https://x.com/percyliang/status/2000608134205985169))

---

## Policy and Institutions

**OpenAI introduces GPT-5.2.** OpenAI's release post frames GPT‑5.2 as its most capable model for long-horizon professional work, claiming new state‑of‑the‑art benchmark results and improvements in agentic coding and data analysis. ([Link](https://openai.com/index/introducing-gpt-5-2/))

*Also this week:* UK Minister for AI Kanishka Narayan posts about the "International Network for Advanced AI Measurement, Evaluation and Science" (formerly the International Network of AI Safety Institutes), emphasizing international coordination around measurement and evaluation as a basis for trust. ([Link](https://x.com/kanishkanarayan/status/1999027561427243125))

