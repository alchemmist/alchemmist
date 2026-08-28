# ICCQ 2026: fit assessment for Anton Moss

Assessment date: 2026-08-23.

## Verdict

Anton is technically qualified to participate in ICCQ 2026 and has source material for a
relevant paper. The strongest basis is Quality Graph together with its production origin in
Monori. The limiting factor is not implementation maturity but the lack of a completed
research contribution: a narrow research question, comparison baseline, experiment,
dataset, and written paper.

Submitting by the current deadline is possible but high-risk. The official deadline is
2026-08-27, leaving four calendar days. A credible submission should be a focused six-page
experience or empirical paper, not a broad product overview.

## Conference constraints

ICCQ focuses on static and dynamic analysis, program verification, programming-language
design, bug detection, and software maintenance. It evaluates novelty, importance,
evidence, and clarity. Evidence may include an implemented system, experiments, case
studies, or anecdotes. Review is double-blind and performed by at least three reviewers.
Submissions must use the specified ACM SIGPLAN layout, contain 6–20 pages, and publish
digital artifacts through Zenodo. Publication and registration are free; remote talks are
allowed. [ICCQ 2026 call for papers](https://www.iccq.ru/2026.html)

The selection bar is meaningful. In 2025, ICCQ received 39 submissions, desk-rejected 23,
and accepted 4. In 2024, it received 23, desk-rejected 10, and accepted 4.
[ICCQ 2025](https://www.iccq.ru/2025.html),
[ICCQ 2024](https://www.iccq.ru/2024.html)

Past programs show that empirical studies, tools with evaluations, replications, and
qualitative feasibility studies can all fit. A purely descriptive README-style system paper
would still be weak because accepted work states a research contribution and supports it
with evaluation.

## Relevant portfolio evidence

| Project | ICCQ relevance | Current evidence | Submission value |
| --- | --- | --- | --- |
| [Quality Graph](https://github.com/alchemmist/quality-graph) | CI quality pipelines, result protocols, failure governance, secure analysis publication, software maintenance | Functional pre-release; declarative DAG compiler; SARIF/JUnit/native result adapters; fork-safe trusted publisher; stable findings and approvals; 254 unit tests and one fake-GitHub integration test passed locally on 2026-08-23 | Strongest paper nucleus |
| [Monori](https://github.com/alchemmist/monori) | Real-world quality-system case study, mutation testing, static analysis, integration and performance testing | 1,073 commits, 608 tracked files, 169 test files, and the production implementation from which Quality Graph was extracted at inspected commit `a414b18a` | Strong longitudinal case-study subject |
| [loglint](https://github.com/alchemmist/loglint) | Direct static analysis and bug/security-smell detection in Go logging | `go/analysis` implementation for standard log, slog, and zap; configurable checks and fixes; 58 tests passed with the race detector on 2026-08-23 | Relevant, but currently too narrow and heuristic for a paper without a corpus evaluation |
| [devsyringe](https://github.com/alchemmist/devsyringe) | Maintenance and configuration automation | Working Go CLI/TUI with multiple installation channels | Peripheral to ICCQ and lacks research evidence |
| [CIer](https://github.com/alchemmist/CIer) | CI workflow reuse and maintenance | Tooling concept is relevant | Secondary evidence; weaker than Quality Graph for a 2026 submission |

Repository counts were taken from the checked-out Git histories on 2026-08-23. Test claims
come from `make test` in Quality Graph and loglint.

## Best paper direction

### Recommended thesis

**Compiling repository-owned quality graphs into secure native CI pipelines: an industrial
case study.**

The paper should not claim that DAG-based CI itself is novel. The defensible contribution is
the combination of:

1. a compact, repository-owned quality declaration compiled into independently observable
   native GitHub Actions jobs;
2. a language-neutral result protocol with stable semantic finding identity;
3. separation of untrusted pull-request execution from trusted publication and governance;
4. evidence from extracting the system from a large real repository into a reusable tool.

Candidate research questions:

- How much workflow duplication and maintenance surface does the declaration/compiler remove
  compared with handwritten GitHub Actions?
- Can the generated architecture preserve native parallelism, rerun semantics, and
  least-privilege fork safety?
- How reliably does the result protocol normalize heterogeneous SARIF, JUnit, and native
  results while preserving stable findings across source movement and reruns?

### Minimal evaluation

Use Monori plus the bundled Python, TypeScript, and Go consumers. Compare handwritten and
generated setups on:

- authored configuration lines and duplicated workflow fragments;
- graph nodes, generated jobs, critical path, and parallelism;
- permission scopes and behavior for same-repository and fork pull requests;
- correct handling of reruns, stale artifacts, traversal/symlink payloads, unauthorized
  approvals, and moved findings;
- setup time or maintenance edits for adding one check to each consumer.

Publish the anonymized configuration corpus, measurement scripts, raw CSV, and replication
instructions on Zenodo. Because review is double-blind, verify with the chairs how to expose
an already-public repository artifact without compromising anonymity.

## Alternative direction

`loglint` could support a paper about detecting sensitive-data exposure and log-message
quality problems in Go, but it first needs a labeled corpus and comparison with existing
linters. Required work includes sampling real repositories, defining ground truth, measuring
precision/recall per logging API and rule, analyzing false positives, and comparing against
available golangci-lint analyzers. This is not realistic to complete rigorously in four days.

## Four-day submission plan

1. **23 August:** freeze one thesis and 2–3 research questions; email the chairs immediately
   about public artifacts and double-blind handling.
2. **24 August:** implement the measurement harness and run all scenarios on Monori and the
   three example repositories; save raw results.
3. **25 August:** analyze results and write method, system design, threats to validity, and
   related work.
4. **26 August:** finish the six-page paper, anonymize it, prepare the Zenodo artifact, and
   validate the exact SIGPLAN layout.
5. **27 August:** final reproducibility check and submission with several hours of buffer.

## Bottom line

- **Attend/watch:** yes, unconditionally; the stream and registration are free.
- **Submit a paper:** yes, technically, and the topic fits; acceptance is plausible only with
  a narrow empirical Quality Graph paper.
- **Submit the repositories as they stand:** no. Strong engineering is necessary evidence,
  but it is not yet a research paper.
- **Realistic confidence:** moderate for producing a compliant submission in four days, low
  to moderate for acceptance without a co-author experienced in empirical software
  engineering and rapid experimental design.

