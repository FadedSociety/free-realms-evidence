<!-- fleet job=note-refresh id=Native-Navigation-Helper status=done turns=6 usd=0.0067 tokens(read,write,in,out)=[50719, 26004, 14, 5952] model=claude-haiku-5-5 -->
# notes/Research/Native Navigation Helper.md

**Verdict:** minor drift. Most of the note describes a helper that lives in the private `lab/` sibling, which is gitignored (`.gitignore:28`) and absent from the repo tip, so most claims cannot be checked here. The one claim the tip can check is wrong: the `--execute` path does not keep the run's `external-inputs.jsonl`.

**Corrections:**

1. `old:` preserving Universal Modder foreground checks and the run's `external-inputs.jsonl`
   `new:` preserving Universal Modder foreground checks; at the tip, `scripts/drive-local-game.py:43` opens `external-inputs.jsonl` with `newline="/n"`, which Python rejects (ValueError) after the input has already been sent (lines 39-41), so the run's input record is not written until that line is fixed
   `why:` `repo:scripts/drive-local-game.py:39-43`. The script runs the game input first (`subprocess.run`, lines 39-41), then appends the record at line 43. `newline` must be None, '', '\n', '\r' or '\r\n'; `"/n"` is not one of them. The pinned UM check and the "physical client pixels" header (lines 1-6) do match the note's foreground-check description.

**Unsure:**

- `lab/tools/navigate-local-game.py`, `lab/tools/wiki-env/…`, `lab/reports/test-native-navigation.py` and the `navigation-*.jsonl` run logs are not in the repo tip (`lab/` is outside it, `.gitignore:28`). I could not check the helper's defaults (2.5 radius, 1.45 rad/s, 8.5 units/s, 150 units/90 s, 300/180 maximums), the 500 ms hold cap, the 17- and 18-batch counts, the 8.605 and 38.637 unit totals, or the "both scripts pass Python compilation" claim.
- The only partial corroboration is `notes/Reviews/Remaining Opening Preflight.md:37`, which documents the same helper with `--radius 2.5 --turn-rate 1.45 --speed 8.5 --max-seconds 90 --max-distance 150` and says the trip is segmented. That matches the note's defaults for the radius, rates and 150/90 bound, but it does not confirm the 300/180 maximum.
- `project/scripts/…` is the vault's name for the repo's `scripts/` folder (the Preflight and Project Map notes use the same prefix). I treated it as the same file.
- The `"/n"` in place of `"\n"` also appears in other tip files (e.g. `scripts/native_map/dispatch.py:313`). That may be a systematic transcription artifact, but the `drive-local-game.py` line is the one that would stop a real `--execute` session from writing its record.
