# Analytical Lenses

Use these lenses selectively. Pick the few that clarify the user's situation instead of applying all of them.

## Scale Ladder

Move up and down levels:

1. Immediate event: What happened?
2. Mechanism: How did it happen?
3. Pattern: Where has this happened before?
4. System: What structure keeps producing it?
5. Incentives: Who benefits, avoids pain, or has no reason to change?
6. Environment: What market, culture, policy, technology, or timing makes this likely?
7. Identity or narrative: What story are people using to explain it?

Use the level that changes the user's next decision. Avoid staying at the highest abstraction if the useful action is local.

## Symptom, Cause, Constraint, Choice

Separate four categories:

- **Symptom:** The visible pain or event.
- **Cause:** The mechanism producing the symptom.
- **Constraint:** A real limit on available actions.
- **Choice:** A decision the user or another actor can actually make.

Many confused problems come from treating constraints as causes, causes as choices, or symptoms as the whole problem.

## System Map

Map the situation as:

- actors
- resources
- flows of money, time, attention, information, trust, authority, or work
- bottlenecks
- feedback loops
- delays
- externalities
- failure modes

Look for places where a small change modifies a repeated pattern, not just a single event.

## Incentives

For each actor, ask:

- What are they rewarded for?
- What are they punished for?
- What do they avoid saying directly?
- What risk are they trying to transfer?
- What metric or story makes their behavior look rational?

Assume behavior is often locally rational even when globally harmful.

## Bottleneck And Leverage

Identify the limiting factor:

- attention
- money
- time
- trust
- information
- skill
- distribution
- compute or tooling
- authority
- coordination
- demand
- feedback speed

The best next move usually targets the bottleneck, not the most visible irritation.

## Time Horizon

Compare:

- immediate relief
- short-term progress
- medium-term compounding
- long-term optionality

Name when a recommendation changes because the time horizon changes.

## Reversibility

Classify choices:

- reversible: easy to undo, good for experiments
- semi-reversible: undoable with cost
- irreversible: requires higher confidence, mitigation, or staged commitment

Favor experiments when uncertainty is high and reversibility is good.

## Second-Order Effects

Ask what happens after the obvious first result:

- What behavior will this incentive create?
- What expectation will this set?
- What dependency will this introduce?
- What does this make easier or harder next time?
- Who adapts in response?

## Risk And Uncertainty

Separate:

- known facts
- plausible inferences
- assumptions
- unknowns that matter
- unknowns that are noise

For uncertain decisions, recommend information-gathering only when the information can change the action.

## Narrative Frame

When the user is stuck in a story, identify the frame:

- Is this being framed as a competence problem, resource problem, trust problem, timing problem, incentive problem, or identity problem?
- What alternate frame explains more with fewer assumptions?
- What frame creates useful action instead of blame?

## Power And Agency

Clarify:

- What can the user directly control?
- What can they influence?
- What can they only observe or route around?
- What would require coalition, authority, capital, or time?

Do not recommend actions that require power the user does not have without naming the gap.

## Essence vs. Accident

Classify the difficulty before trying to solve it:

- **Essential complexity**: Inherent to the problem itself — the logic, the irreducible requirements, the domain. Cannot be engineered away.
- **Accidental complexity**: Introduced by tools, processes, history, or prior choices. Can be reduced by better tools, refactoring, or simplification.

Only accidental complexity can be eliminated. Effort spent attacking essential complexity with technical tools is largely wasted. Ask whether the difficulty is a property of the problem or a property of how the problem is currently being handled.

## Feedback Loops and Stocks

Map the situation as:

- **Stocks**: What is accumulating or being depleted — trust, technical debt, morale, cash, capability, reputation?
- **Flows**: What is increasing or decreasing those stocks?
- **Reinforcing loops**: Self-amplifying patterns — virtuous cycles or vicious spirals.
- **Balancing loops**: Self-correcting patterns — stabilizers that resist change.
- **Delays**: Time between action and visible effect.

Delays in feedback loops are the source of oscillation, overreaction, and recurring failure. When action produces no visible result, the natural response is to act more — but when the delayed feedback finally arrives, it is already too much. Ask: what is accumulating here, what loop is driving it, and where is the delay?

## Leverage Points

When intervening in a system, the point of intervention matters more than the force applied. In order of increasing impact:

1. Parameters and numbers — rarely change behavior durably
2. Feedback loop strength and delay length
3. Rules, incentives, and information flows
4. Goals and purposes of the system
5. The paradigm — the shared assumptions that generate the system (strongest)

Most interventions happen at level 1. Most durable change happens at levels 3–5. Ask: am I adjusting a number, or changing a rule, a goal, or a shared belief?

## Time × Scale

For technical and organizational decisions, cost does not live at a single moment — it integrates over time and multiplies by the number of people affected:

- A shortcut that saves a day today but adds friction to every future change may be net negative.
- A practice acceptable at 10 people becomes a bottleneck at 1000.
- Any observable behavior of a system will eventually be depended on by someone, regardless of what the documentation says.

Ask: what does this cost per year, times the number of people affected? Is this decision reversible or irreversible? If irreversible, the analysis needs to be proportionally more careful.

## Abstraction Layer

For problems in software systems, ask what layer the root cause actually lives in:

- Application layer: logic, design, algorithm, data model
- Framework or library layer: configuration, version, API contract
- Runtime or OS layer: process, memory, concurrency, scheduling
- Hardware or network layer: latency, bandwidth, physical failure mode

Symptoms often appear at a higher layer than their cause. A bug that looks like application logic may be a library or runtime issue. A performance problem that looks like an algorithm may be a memory locality or I/O pattern problem. Moving one layer down often reveals the actual constraint.

## Equilibrium vs. Optimum

When multiple actors are involved, the outcome is not determined by any one actor's intentions — it is determined by the interaction structure. Individual rationality does not produce collective optimum. The question is not "what should people do?" but "given the payoffs and rules, what will they actually do, and is that the equilibrium I want?"

If the current behavior is an equilibrium — meaning every actor is already doing their best given what others are doing — moral appeals and requests to "do better" will not change it. The structure must change.

Ask: is this behavior an equilibrium? What rule change would make the desired behavior the dominant strategy?

## Principal Contradiction

In any complex situation with multiple tensions, one is principal — its resolution is the precondition for progress on everything else. Scattering effort across all tensions at once is less effective than identifying and attacking the principal one.

Ask: if this one tension were resolved, would the others become easier or dissolve? That is likely the principal contradiction. Which side of it is currently dominant, and is that shifting?

## Internal Cause vs. External Condition

External inputs — tools, methodologies, outside experts, new technology — accelerate or constrain what a system can do, but they cannot substitute for internal structural capacity. A system that lacks the internal structure to absorb a change will resist or reject it regardless of how powerful the external input is.

Ask: am I trying to fix internal structure, or am I importing an external solution and hoping it takes? What internal capability or design change would make the external input actually land?
