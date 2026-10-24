<!-- fleet job=note-refresh id=Startup-Message-Builders status=done turns=11 usd=0.0138 tokens(read,write,in,out)=[240710, 45957, 24, 11247] model=claude-haiku-5-5 -->
# notes/Research/Startup Message Builders.md

**Verdict:** badly stale. The capture inventory table and the seven-builder description in `startup_messages.rs` still hold. The "Builder implementation status" and "Gateway handoff" sections describe the pre-integration state. The W19 integration has since made the switch, and `notes/Research/Startup Integration.md` says it supersedes this note's handoff.

**Corrections:**

1. `old:` This does **not** meet the requested 46-message replacement yet.
   `new:` The gateway now builds all 46 startup messages: 45 from the typed snapshot and index 07 (self data) from typed self data. See [[Research/Startup Integration]].
   `why:` `repo:prototype/osfr-tools/src/gateway.rs:1892-1923` (`startup_for` builds ranges 0..8 and 8..46; index 7 goes to `build_self_message`); `repo:prototype/osfr-tools/src/startup_snapshot.rs:307-368`; `repo:notes/Design/Build Ledger.md:39`.

2. `old:` The unimplemented capture indices are `00, 04-32, 35-38, 40-42, 44-45` (39 messages).
   `new:` The snapshot builds every capture index except 07 (`startup_snapshot.rs` `build_packet`, indices 0–6 and 8–45); index 07 is built from self data by `Gateway::build_self_message`.
   `why:` `repo:prototype/osfr-tools/src/startup_snapshot.rs:307-368`; `repo:prototype/osfr-tools/src/gateway.rs:1917`, `1925`.

3. `old:` In particular, no complete builder exists for self data (index 07), so synthetic character name/GUID/position and inventory-size coverage is still absent.
   `new:` Index 07 is built by `Gateway::build_self_message` from `startup_selfdata::build_self`, seeded from captured template 7. Its action-bar rows remain the captured ones.
   `why:` `repo:prototype/osfr-tools/src/gateway.rs:1925-1960`; `repo:notes/Design/Build Ledger.md:40`; `repo:notes/Research/Startup Integration.md:9-10`.

4. `old:` Do not switch the gateway until all 46 packet builders and synthetic character-state coverage are reviewed.
   `new:` The gateway switch is done (W19). Remaining open items are the native-client acceptance and the field-level layouts listed above.
   `why:` `repo:prototype/osfr-tools/src/gateway.rs:1445-1476`; `repo:notes/Research/Startup Integration.md:3`, `:39-41`.

5. `old:` No gateway edits are part of this worker scope. After every message builder passes the private byte oracle, the lead's exact switch points are:
   `new:` The gateway switch has been made (W19, see [[Research/Startup Integration]]). The points below are kept as a record of the handoff.
   `why:` `repo:prototype/osfr-tools/src/gateway.rs:1445-1476`; `repo:notes/Research/Startup Integration.md:3`.

6. `old:` call: replace with `startup_messages::build_login(...)`.
   `new:` call: replaced by `self.startup_for(Kind::Login, &state, gameplay.as_ref())`, which builds from `startup_snapshot`.
   `why:` `repo:prototype/osfr-tools/src/gateway.rs:1445-1453`, `1892-1923`. There is no `startup_messages::build_login` in the tree.

7. `old:` replace only the `templates_for(Kind::Ready, &state, gameplay.as_ref())` fallback with `startup_messages::build_ready(...)`
   `new:` the fallback now calls `self.startup_for(Kind::Ready, &state, gameplay.as_ref())`
   `why:` `repo:prototype/osfr-tools/src/gateway.rs:1455-1473`. The `kart_ready_stream()` route is still in place at `:1460-1466`.

8. `old:** Remove `Gateway::templates_for` after its identity, inventory, zone and gameplay patches have moved into the builder inputs.
   `new:` `Gateway::templates_for` is already gone (no definition or call under `prototype/osfr-tools/src`). The template-removal step is still open: `load_reference` still reads and hash-checks all 46 template files, and template 7 still seeds self data.
   `why:` search of `prototype/osfr-tools/src` finds no `templates_for`; `repo:prototype/osfr-tools/src/gateway.rs:312-345`; `repo:notes/Design/Build Ledger.md:39-40`.
   (Note for the editor: the `old` text above has a stray `**` at its start. Copy the sentence without it: `Remove `Gateway::templates_for` after its identity, inventory, zone and gameplay patches have moved into the builder inputs.`)

**Unsure:**
- The `lab/...` citations (the capture inventory, command log, `lab/references`, `lab/content/startup-snapshot/startup.json`) point to private paths that are not in the repo, so I could not check them.
- The table's byte counts, SHA/RTTI/address citations (for example `00aa36c0`, `00921a10`) and the per-packet field descriptions are client-side claims. I did not verify them; I only checked the repo-side claims.
- I did not re-run the ignored private oracles. The integration note reports them passing, but I could not confirm that from the code alone.
