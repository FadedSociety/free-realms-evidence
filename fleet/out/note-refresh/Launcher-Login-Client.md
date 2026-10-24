<!-- fleet job=note-refresh id=Launcher-Login-Client status=done turns=11 usd=0.0125 tokens(read,write,in,out)=[175576, 32666, 24, 13234] model=claude-haiku-5-5 -->
# notes/Research/Launcher Login Client.md

**Verdict:** badly stale on the entry hook and UI wiring. The code and the module, profile, ACL, timeout and test-count claims still hold. The note's "not wired" statements were true when W100 wrote them and are false at the tip.

**Corrections:**

1. `old:` **That hook is not
currently in main.rs**, which this task explicitly forbids editing. (lines 47-48)
   `new:` **That hook is now in main.rs:** `main()` calls `osfr_launcher::key_command` before `diagnostics::init` and the GUI, prints the public key or the error, and exits.
   `why:` repo:launcher/src/main.rs:1392-1407 (`key_command` dispatch, `println!`/`eprintln!` + `exit(2)`); repo:launcher/src/lib.rs:10-35.

2. `old:` Both the
hook and the UI LoginProvider wiring remain lead-owned; no callable executable
CLI or authenticated Play-button claim is made here. (lines 49-50)
   `new:` The entry hook and the UI LoginProvider are both wired: `RealmLogin` implements `LoginProvider` via `auth::load_profile` and `auth::login`, is built on the Play path, and Settings calls `auth::new_key`/`auth::save_profile`. The executable exposes the `--new-key` / `--print-public-key` CLI, and Play runs the authenticated login. Native acceptance is still not claimed here.
   `why:` repo:launcher/src/main.rs:242-244 (`RealmLogin` → `auth::login`), :491 (Play-path login provider), :543-544 (`auth::new_key`, `auth::save_profile`); repo:launcher/src/main.rs:1392-1407.

3. `old:` 3. **CLI entry hook.** Main dispatch and authenticated UI integration cannot be
   `new:` 3. **CLI entry hook (now routed).** Main dispatch is in `main.rs`, and the authenticated UI path is also wired; see the status line above.
   `why:` repo:launcher/src/main.rs:1392-1407, :242-244, :491.

4. `old:` the executable does not yet route it.
   `new:` the executable routes it (`launcher/src/main.rs:1392-1407`, before `diagnostics::init`).
   `why:` repo:launcher/src/main.rs:1392-1407.

5. `old:` **Implemented, acceptance blocked.**
   `new:` **Implemented and wired into the CLI and Play path; lead-verified as a normal user (22 launcher tests green); native acceptance still open.**
   `why:` repo:notes/Design/Build Plan.md:135 ("Lead ran the gates as a normal user in a clean worktree ... 22 launcher tests green"; "Open: ... native launch with the token"); repo:notes/Autopilot/T445.md:86; repo:launcher/src/main.rs:1392-1407, :491.

6. `old:` need a normal user-token run by the lead.**
   `new:` were run by the lead as a normal user. Build Plan reports 22 launcher tests green, including a real `osfr-login` enrol-and-login. The tests are `launcher/tests/auth.rs:70, :155, :187, :218, :250, :371`.
   `why:` repo:notes/Design/Build Plan.md:135; repo:notes/Autopilot/T445.md:86; repo:launcher/tests/auth.rs:70-371 (six `#[test]` cases).

7. `old:` No valid pin-disable canary or full green build/test result is claimed.
   `new:` The pin canary was run as a normal user. Per the Build Plan, `wrong_pin_sends_no_proof_canary` fails when the pin check is disabled. The warning-free full gate is not separately recorded here.
   `why:` repo:notes/Design/Build Plan.md:135 ("the pin canary fails `wrong_pin_sends_no_proof_canary`"); repo:launcher/tests/auth.rs:155-187.

**Checked and holding (no change):** `launcher/src/auth.rs` exists and is declared in `lib.rs:4`; profile path `%APPDATA%/FreeRealmsExpanded/profiles/<id>/` (auth.rs:151); `key.ed25519` and `profile.json` names (auth.rs:220-286); 2 s connect and 3 s exchange timeouts (auth.rs:21-22); `AuthError::Refused` and `TryLater` (auth.rs:28-29); Windows owner-only DACLs `D:P(A;OICI;FA;;;OW)` and `D:P(A;;FA;;;OW)` (auth.rs:502-504); Unix 0700/0600 modes (auth.rs:418-436); `SessionToken` has no Debug/Display (lib.rs:83-84); four new direct deps in `launcher/Cargo.toml:19-22`; auth_wire.rs has three tests; `auth_canary.py` sits in `launcher/tests/`. The Key-pair Login Contract cites ("Exact launcher contract", lines 24-39) and the Multi Login Design decision lines 13-22 both still match.

**Unsure:**
- Line 175-177 ("The mandatory warning-free full build/test gate remains open"): I did not run or read a warning log, so I cannot say whether this is still true.
- Native launch with the token (Build Plan line 135 lists it as open). I found the code path to `SessionToken`, but no evidence either way for native acceptance.
- Citation ranges `prototype/osfr-tools/tests/login_broker.rs:37-231` and `src/bin/osfr-account.rs:14-149`: the files exist and the relevant items are in range, but I did not verify the exact extents.
- The Unix-branch claim ("not compiled/tested here") is unverified either way; I did not check it.
