# Evidence-Based Learning System

Version: 2026-07-16

This document defines the learning mechanics used across Python, mathematics,
English, Git, ML, and industrial projects. The six-month topic order remains in
the local `PROGRESS.md`; this file defines how each topic is learned.

## Core Principles

1. Retrieval beats passive rereading for long-term retention.
2. Practice is distributed across sessions instead of concentrated in one sitting.
3. A novice first studies a worked example, then completes a faded example, and
   only then solves a comparable problem independently.
4. Feedback explains the cause of an error and is followed by a new attempt.
5. Mastery requires independent performance and delayed transfer, not merely a
   successful run immediately after an explanation.
6. Interleaving begins after the basic pattern is understood; initial practice may
   remain blocked to avoid unnecessary cognitive overload.
7. AI acts as a scaffold and reviewer. It must not replace retrieval, prediction,
   coding, debugging, or explanation by the student.

## Learning Cycle for a New Topic

Tasks are presented one at a time, but the complete lesson follows this sequence:

1. **Retrieval warm-up** - recall one earlier concept without notes.
2. **Goal and prior knowledge** - state the observable skill and prerequisites.
3. **Worked example** - inspect a small complete example and predict its behavior.
4. **Self-explanation** - explain why each important step exists and where it can
   fail.
5. **Faded example** - fill one or more missing decisions or lines.
6. **Independent task** - solve an isomorphic problem without copying the example.
7. **Transfer task** - change data, constraints, failure mode, or industrial context.
8. **Feedback and retry** - classify the error, correct it, then solve a short
   variant without the previous hint.
9. **Exit retrieval** - explain the concept, predict code, and name when to use it.

Not every micro-session needs all nine steps. A topic may span multiple sessions;
the sequence must be completed before the topic is marked mastered.

## Mastery Gate

A topic is **mastered** only when the student can:

- explain the idea and key terms in their own words;
- predict the behavior of a short example before running it;
- implement the core pattern independently;
- diagnose at least one realistic error;
- adapt the pattern to a changed condition;
- repeat the essential performance in a later session without step-by-step help.

Status values:

- **Introduced** - explanation and worked example completed.
- **Practiced** - guided and independent practice completed in the same session.
- **Retained** - delayed retrieval succeeded in a later session.
- **Transferable** - a changed or mixed problem was solved independently.

The next prerequisite-dependent topic starts only after at least `Retained`.
`Transferable` is required at project and month gates.

## Spacing and Cumulative Review

The exact optimal interval depends on how long knowledge must be retained. The
default operating schedule is:

- start of the next study session: short free recall of the previous topic;
- after two or three study cycles: one mixed prediction/debugging task;
- end of the month: cumulative no-notes task and explanation;
- later projects: reuse earlier concepts without announcing which one is needed.

Anki handles adaptive fact and concept review. It does not replace writing code
from memory. Add `0-3` new cards per lesson only when the item is durable and
worth remembering; card count is not a success metric.

## Practice Mix

For a new construct, use a short blocked sequence until the basic pattern is
stable. Then add cumulative and interleaved practice regularly; as an operational
default, include at least one mixed task after every two or three study cycles:

- old and new Python constructs in one task;
- code reading, implementation, debugging, and modification;
- familiar and unfamiliar data;
- direct exercises and project integration.

Projects do not replace focused exercises. Exercises build components; projects
test integration, decisions, debugging, documentation, and persistence.

## Feedback and Hint Ladder

Use the smallest level that restores productive thinking:

1. ask for prediction or restatement of the goal;
2. identify the relevant concept, not the exact line;
3. point to the responsible block or invariant;
4. show a smaller analogous example;
5. provide a partial solution with a missing decision;
6. show the full solution only after sustained effort or an explicit request.

After levels 4-6, require self-explanation and a fresh variant without assistance.
Correct answers with weak reasoning are not treated as mastery.

## Mathematics and English

Both streams remain continuous but must be meaningful:

- **Math Core:** connect mathematics when the code genuinely uses it. Otherwise,
  spend the short slot retrieving a previously introduced math concept instead of
  inventing an artificial connection.
- **English Core:** introduce technical terms in context, then retrieve them in
  documentation, error messages, README text, and code review.
- Every study cycle must touch both streams, but every individual coding lesson
  does not need new mathematical content or a fixed number of new terms.

## Session Design for the 2/2 Schedule

### Phone / work day

Use 20-30 minutes for Anki review, free recall, code prediction on paper, English
terminology, or a short conceptual discussion. Do not introduce syntax that cannot
soon be practiced at a computer.

### Computer / off day

Use 60-90 minute focused blocks separated by real breaks. A full two-day cycle
contains:

- fundamentals and deliberate exercises;
- current project work;
- mathematics and English;
- code review, Git, documentation, and reflection;
- an AI awareness session every one or two cycles when core work is on track.

Do not enforce a universal `20/80` ratio. Practice should dominate, but the amount
of explanation depends on prior knowledge and task complexity.

## Measurement

Track outcomes rather than time or card volume:

- tasks solved independently;
- hint level required;
- delayed retrieval result;
- transfer/debugging result;
- recurring error category;
- project behavior, tests, and explanation quality.

Weekly checks are low-stakes and cumulative. Monthly exams include explanation,
prediction, implementation, debugging, and transfer. Exam feedback is followed by
targeted corrective practice and a new variant.

## Research Basis

- Dunlosky et al. (2013), review of learning techniques:
  https://doi.org/10.1177/1529100612453266
- Roediger and Karpicke (2006), retrieval practice and delayed retention:
  https://doi.org/10.1111/j.1467-9280.2006.01693.x
- Cepeda et al. (2006), meta-analysis of distributed practice:
  https://digitalcommons.usf.edu/psy_facpub/1771/
- Butler and Roediger (2008), corrective feedback after testing:
  https://pubmed.ncbi.nlm.nih.gov/18491500/
- Kulik, Kulik, and Bangert-Drowns (1990), mastery learning meta-analysis:
  https://doi.org/10.3102/00346543060002265
- Shin et al. (2023), faded worked examples and metacognitive scaffolding in
  introductory Python programming:
  https://doi.org/10.1177/07356331231174454
- Li, Liu, and Dong (2025), GenAI support, cognitive offloading, and transfer:
  https://doi.org/10.14742/ajet.9932
