# Representative Pilot Cases

These authored cases define representative validation scenarios. Generated execution evidence belongs outside the skill package.

## Pilot 1: shared authentication capability

### Baseline failure pattern

- starts from OAuth or framework middleware;
- exposes provider claims as the domain model;
- leaves ownership and product acceptance implicit;
- treats repository or SDK selection as the capability.

### Expected with-skill improvement

- defines trusted identity context as the capability;
- records policies and invariants independently from providers;
- places OAuth, passkeys, passwords, provider adapters, and runtime bindings in separate layers;
- hands the stable model to domain and architecture owners.

### Observable comparison dimensions

- boundary clarity;
- adapter independence;
- invariant visibility;
- downstream usefulness;
- unsupported assumptions.

## Pilot 2: queue backlog and concurrency

### Baseline failure pattern

- assumes queue length proves the queue is the bottleneck;
- increases concurrency without checking provider rate limits, database contention, retry amplification, or operations visibility;
- optimizes local worker throughput rather than end-to-end outcomes.

### Expected with-skill improvement

- identifies actors and dependency direction;
- traces causal relationships, delays, retry loops, and failure propagation;
- identifies the actual system constraint before selecting an intervention;
- records trade-offs, reversibility, and residual risks.

### Observable comparison dimensions

- causal completeness;
- bottleneck accuracy;
- second-order effects;
- leverage-point quality;
- implementation deferral until evidence is sufficient.

## Pilot 3: local variable rename

### Baseline failure pattern

- activates every available reasoning and architecture capability;
- creates ceremonial stakeholder, causal-loop, or domain models;
- adds cost without changing the decision.

### Expected with-skill improvement

- classifies the task as bounded and low risk;
- does not activate, or uses LIGHT depth only if a hidden invariant is discovered;
- preserves proportionality.

### Observable comparison dimensions

- verbosity;
- execution cost;
- unnecessary artifacts;
- decision quality;
- false-positive activation.

## Pilot verdict rule

A pilot is not `PASS` until baseline and with-skill outputs are executed by the repository evaluation path, results are traceable to a commit SHA or skill version, and independent review confirms the comparison. Until then the pilot status is `NOT_VERIFIED`.