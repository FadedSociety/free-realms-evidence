You audit one test file of a Free Realms revival: a Rust game server (prototype/osfr-tools). The team's rule
(Bryce): gameplay values live in data files (prototype/osfr-tools/data/content/*.json) and stay live-tunable, so
tests read such values from the data or check sane bounds; they never pin the exact number. A cheap model already
screened this file's assertions and listed the ones that may pin a tunable number. You can only read.

## Sources (tools)

`search` / `read` / `list` over root `repo` (tests under `prototype/osfr-tools/tests`, code under
`prototype/osfr-tools/src`, data under `prototype/osfr-tools/data/content`).

## For each listed line

1. Read the test around it and find where the number really comes from: a data file field (give the file and the
   field), a constant in code, or a fixture the test builds itself.
2. It is a finding only when the expected number equals a value from a shipped data file (or is computed from one,
   such as a price times a discount) and retuning that data value would break the test while the code is still right.
   A number the test's own fixture sets, a protocol constant, a count of rows, an id or a layout is NOT a finding.
3. Say how the test should get the value instead: the existing helper under `prototype/osfr-tools/tests/common/`
   that loads it if there is one (search first), or reading the row in the test, or a bound.

## Result (call `submit` once)

`status`: `done` with findings, or `nothing_found`. `result`, in Markdown, one entry per finding:

- **path:line test_name - pins `<number>` from `<data file>` `<field>`.**
- **Fix:** read it through `<helper or row>` (or bound it as ...).

Group nothing; one entry per assertion. Leave out lines that are not findings.
