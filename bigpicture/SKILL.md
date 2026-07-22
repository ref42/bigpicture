---
name: bigpicture
description: "Strategic sensemaking for messy, ambiguous, high-context, or overly narrow problems. Use when the user asks for the big picture, wants to zoom out, feels stuck, needs root-cause, system, incentive, stakeholder, tradeoff, risk, or second-order-effect analysis, is deciding what matters, comparing options, planning next moves, or wants a broader frame across technical, product, business, career, learning, organizational, relationship, creative, or life-planning contexts."
---

# Big Picture Thinking

## Purpose

Help the user move from scattered details to a usable map of the situation: what is happening, why it is happening, what matters most, what tradeoffs exist, and what to do next.

Do not merely add more context. Compress context into clearer causal drivers, constraints, risks, and leverage points.

## Triage

Start by classifying the request:

1. **Diagnostic:** The user asks why something is happening.
2. **Strategic:** The user asks what direction to take.
3. **Decision:** The user compares options or feels stuck choosing.
4. **Systems:** The user needs actors, incentives, feedback loops, or root causes.
5. **Technical:** The user is buried in implementation details and needs architecture or failure-mode framing.
6. **Product or business:** The user needs market, customer, distribution, positioning, or operating-model context.
7. **Personal or career:** The user needs goals, constraints, opportunity cost, skill leverage, or life-stage framing.
8. **Conflict or organization:** The user needs stakeholder, incentive, power, trust, or communication framing.
9. **Creative or communication:** The user needs audience, message, narrative, or positioning clarity.

If current facts, prices, laws, health, finance, legal, safety, news, or other high-stakes or time-sensitive information materially affects the answer, verify with appropriate sources before making confident claims.

## Core Workflow

Use this workflow unless the user asked for a very short answer:

1. Restate the surface problem in one sentence.
2. Name the larger system the problem belongs to.
3. Separate symptoms, causes, constraints, and choices.
4. Identify the key actors, incentives, resources, bottlenecks, and feedback loops.
5. Surface hidden assumptions and missing information.
6. Distinguish what matters from what is noise.
7. Explain the main tradeoffs and second-order effects.
8. Give 2-4 viable paths forward.
9. Recommend the next smallest useful action.

## Reference Routing

Read only the references that fit the request:

- Read `references/lenses.md` when the user needs deeper causal analysis, systems thinking, incentives, risk, time horizon, leverage, second-order effects, feedback loops, structural leverage points, abstraction layers, or time-and-scale implications.
- Read `references/playbooks.md` when the request fits a common problem type such as decisions, technical architecture, business strategy, career, conflict, crisis, creative framing, large project coordination, or recurring structural problems.
- Read `references/templates.md` when choosing an output format such as a one-screen answer, decision memo, systems map, executive brief, or technical zoom-out.
- Read `references/question-bank.md` when the situation is under-specified and one or two sharp questions would materially improve the analysis.

## Default Output

For most responses, use this structure:

```markdown
**The Big Picture**
[What is really going on.]

**What Matters Most**
[The few variables driving the situation.]

**Tradeoffs**
[The real choices and costs.]

**Next Move**
[The most useful practical action.]
```

Keep the output proportional to the user's request. If the user asks for a quick take, answer in 3-6 bullets. If they ask for a deep view, build a fuller map.

## Reasoning Standards

- Prefer causal explanation over generic advice.
- Prefer concrete variables over abstract labels.
- Prefer explicit assumptions over hidden certainty.
- Prefer tradeoffs over one-sided recommendations.
- Prefer next actions over philosophical closure.
- Identify when a problem is primarily about incentives, constraints, information, timing, trust, capability, or resource allocation.
- Mark unknowns that could change the conclusion.
- Ask at most 1-2 high-value questions when missing context blocks a useful recommendation.

## Response Guardrails

- Do not over-expand the problem until it becomes unusable.
- Do not force every lens onto every request.
- Do not use named frameworks as decoration.
- Do not give specialist medical, legal, financial, or safety advice beyond high-level framing and source-aware caveats.
- Do not treat emotional distress as a strategy puzzle only; acknowledge the immediate human context before zooming out.
- Do not skip local facts for technical problems. Inspect available code, logs, architecture, or artifacts before giving an architectural read when the workspace contains relevant evidence.

## Quality Bar

A strong big-picture answer should leave the user with:

- a clearer map of the situation
- fewer but better variables to watch
- a more honest view of tradeoffs
- a practical next move
- awareness of what would change the conclusion
