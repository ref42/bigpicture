---
name: bigpicture
description: "Strategic sensemaking for messy, ambiguous, high-context, or overly narrow problems. Use when the user asks for the big picture, wants to zoom out, feels stuck, needs root-cause, system, incentive, stakeholder, tradeoff, risk, or second-order-effect analysis, is deciding what matters, comparing options, planning next moves, or wants a broader frame across technical, product, business, career, learning, organizational, relationship, creative, or life-planning contexts."
---

# Big Picture Thinking

## Purpose

Turn a scattered situation into a usable map: what is happening, what is driving it, what is constrained, what choices exist, and what to do next.

Compress context; do not expand it for its own sake. The output should reduce confusion and improve the user's next decision.

## When To Use

Use this skill when the user needs diagnosis, strategy, a decision, systems thinking, a technical zoom-out, or a broader frame around a personal, organizational, product, business, or creative problem. It is especially useful when the stated problem may be a symptom of a different problem.

Do not force a big-picture treatment onto a simple factual question, a narrowly scoped implementation request, or a problem where the user only needs a direct edit. If a direct answer is enough, give it.

## Operating Protocol

### 1. Classify the job

Choose the dominant mode; combine modes only when the situation genuinely requires it:

1. **Diagnostic:** explain why a pattern or failure is occurring.
2. **Strategic:** choose a direction under uncertainty.
3. **Decision:** compare options against an objective and constraints.
4. **Systems:** map actors, incentives, flows, feedback loops, and power.
5. **Technical:** move from local implementation details to boundaries, failure modes, dependencies, and evolution cost.
6. **Product or business:** connect customer value, economics, distribution, positioning, and operating capability.
7. **Personal or career:** clarify goals, constraints, opportunity cost, optionality, and skill leverage.
8. **Conflict or organization:** examine stakeholders, incentives, authority, trust, communication, and coordination costs.
9. **Creative or communication:** clarify audience, desired response, message, narrative, and channel.

### 2. Establish the frame

State the surface problem in one sentence, then state the larger system it belongs to. Define the boundary: what is in scope, what is outside it, and what outcome the user is trying to improve.

Separate four categories explicitly:

- **Symptoms:** what is visible or being reported.
- **Causes:** mechanisms producing the symptoms.
- **Constraints:** facts that limit the available moves.
- **Choices:** decisions the user can actually make.

Do not treat a label such as “culture,” “communication,” “technical debt,” or “market fit” as a causal explanation. Name the observable mechanism underneath it.

### 3. Build the smallest useful causal map

Identify only the actors, incentives, resources, dependencies, bottleneck, and feedback loops that could change the conclusion. Distinguish internal causes from external conditions, and local optimization from system-level outcomes.

For each important claim, distinguish:

- **Observed:** directly supplied by the user or inspected in the workspace.
- **Inferred:** a reasoned explanation supported by the observations.
- **Unknown:** information that could materially change the recommendation.

Use confidence language when evidence is thin. Do not invent stakeholders, motives, metrics, or causal certainty. For technical problems, inspect relevant code, logs, architecture, tests, or artifacts in the workspace before making an architectural claim.

If current facts, prices, laws, health, finance, legal, safety, news, or other time-sensitive information materially affects the answer, verify them with appropriate sources before making confident claims. Otherwise state the assumption and continue.

### 4. Find the principal tension

Reduce the analysis to the few variables that matter most. Ask what is scarce, what is being optimized, what is being sacrificed, and what would make the problem disappear rather than merely move.

Make tradeoffs concrete: speed versus quality, local versus global optimization, reversibility versus commitment, short-term relief versus long-term capability, or control versus autonomy. Include likely second-order effects and identify which risks are reversible, bounded, or catastrophic.

### 5. Turn the map into action

Offer 2–4 viable paths only when there is a real choice. For each path, say when it fits, what it costs, its main risk, and what it preserves or gives up. Recommend one default path tied to the user's stated objective and constraints.

End with the smallest useful next move: a concrete inspection, conversation, experiment, decision rule, or reversible commitment. Include a leading indicator and a time or evidence checkpoint when useful.

Name the one or two unknowns that would change the recommendation. Ask a question only if the missing answer blocks a useful next move; otherwise make a clearly labeled assumption and proceed.

## Reference Routing

Read only the references that fit the request:

- Read `references/lenses.md` when the user needs deeper causal analysis, systems thinking, incentives, risk, time horizon, leverage, second-order effects, feedback loops, structural leverage points, abstraction layers, time-and-scale implications, equilibrium analysis, or principal contradiction identification.
- Read `references/playbooks.md` when the request fits a common problem type such as decisions, technical architecture, business strategy, career, conflict, crisis, creative framing, large project coordination, recurring structural problems, incentive misalignment, or entangled tensions.
- Read `references/software-engineering.md` when the request needs a software-engineering big picture: architecture, code quality, testing, project execution, technical tradeoffs, systems design, product/UI design, engineering organizations, or book-derived engineering lenses.
- Read `references/templates.md` when choosing an output format such as a one-screen answer, decision memo, systems map, executive brief, or technical zoom-out.
- Read `references/question-bank.md` when the situation is under-specified and one or two sharp questions would materially improve the analysis.

## Output Selection

Choose the lightest format that preserves the reasoning:

- **Quick take:** conclusion, three drivers, tradeoff, next move.
- **Deep or ambiguous problem:** surface problem, system, drivers, constraints, paths, recommendation, and what would change it.
- **Decision:** objective, constraints, options, recommendation, risk control, next step.
- **Systems problem:** actors, flows, feedback loops, bottleneck, leverage point, side effects.
- **Technical problem:** system boundary, failure mode, root-cause candidates with confidence, tradeoff, better boundary, next inspection or change.

For most responses, use:

```markdown
**The Big Picture**
[What is really going on.] [Modeled claims should be marked as observed, inferred, or unknown when useful.]

**What Matters Most**
[The few variables driving the situation.]

**Tradeoffs**
[The real choices and costs.]

**Next Move**
[The smallest useful practical action, with a checkpoint when useful.]
```

Keep quick answers to roughly 3–6 bullets. Use a fuller map only when the complexity or stakes justify it.

## Guardrails

- Prefer causal explanation over generic advice and concrete variables over abstract labels.
- Prefer explicit assumptions, calibrated confidence, and tradeoffs over hidden certainty or one-sided recommendations.
- Do not force every lens, framework, stakeholder, or feedback loop into every answer.
- Do not confuse more context with better analysis; stop once the map supports a decision.
- Do not give specialist medical, legal, financial, or safety advice beyond high-level framing and source-aware caveats.
- When emotional distress is present, acknowledge the human situation before analyzing strategy.
- Keep agency with the user: distinguish what they can control, influence, test, or only prepare for.

## Quality Bar

A strong answer leaves the user with:

- a clearer map of the situation
- fewer but better variables to watch
- an honest view of tradeoffs and uncertainty
- a practical next move with a way to learn
- awareness of what would change the conclusion
