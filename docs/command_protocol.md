# Command Protocol

## `НАЧИНАЕМ`

Start the next lesson from the current checkpoint.

Each lesson must include:

- lesson goal;
- short theory;
- `2-5` micro-examples;
- `3-5` tasks from simple to harder;
- one engineering task;
- mastery criteria.

## `ГОТОВО`

Expected use:

- student sends code or answers;
- review is performed;
- weaknesses are identified;
- control questions are asked if needed;
- either reinforcement or next step follows.

## `СТОП`

Expected output:

- fixed checkpoint;
- what was learned;
- what remains unstable;
- exact next lesson or subtopic.

## `ПРОДОЛЖИМ`

Resume exactly from the last fixed checkpoint without resetting the sequence.
