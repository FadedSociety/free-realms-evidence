<!-- fleet job=note-refresh id=Kart-Local-Racer-and-Gate-Binding status=done turns=13 usd=0.0138 tokens(read,write,in,out)=[307284, 43308, 28, 10666] model=claude-haiku-5-5 -->
# notes/Research/Kart Local Racer and Gate Binding.md

**Verdict:** badly stale on status. Section 1 (local-racer ownership, tail bytes) still matches the code. Sections 2 and 3 describe as future work a gate-hit service that is now built and routed: the `33/7` authority checks, the ordered waypoints, the oriented band and the CDTA gate-leaf recovery.

**Corrections:**

1. `old:` **Original gate ids and gate geometry are unrecovered.** What can be built is a bounded
   `new:` **Original gate ids are unrecovered. The authored gate leaves were recovered from the shipped CDTA (`sg_kt_gates_bbec_004.cdt`, 144 vertices, 72 triangles, 17 vertical planes) and enter as content `gate_curtains`; waypoint positions and the oriented band remain reconstructed. The bounded reconstruction is built (see below).**
   `why:` repo:prototype/osfr-tools/src/kart_service.rs:95-98 (GATE GEOMETRY paragraph), :262-274 (`GateCurtain`), :241-260 (`GateBand`).

2. `old:` * treat each accepted hit as an ordered waypoint sample (dedupe by radius, order by server time);
   `new:` * implemented: the ordered waypoints are `KartServiceContent.gates` (`GateWaypoint`), attributed in order by `attribute_gate` against the expected gate, so a skipped or stale hit cannot advance the race;
   `why:` repo:prototype/osfr-tools/src/kart_service.rs:236-239 (`GateWaypoint`), :334 (`gates`), :2631-2650 (`attribute_gate`), :2555-2559 (expected checkpoint).

3. `old:` A server-side gate check needs, at minimum:
   `new:` A server-side gate check needs, at minimum (all four are implemented in `KartService`; the list is kept as the requirement set):
   `why:` repo:prototype/osfr-tools/src/kart_service.rs:24-31 (AUTHORITY paragraph: "A client gate hit is a claim, never evidence").

4. `old:` 1. an authenticated sender: the guid in the packet must be bound to the connected member, and only that member's own guid may appear;
   `new:` 1. an authenticated sender: the guid in the packet must be bound to the connected member, and only that member's own guid may appear (implemented: `own_guid` checks the offered guid against the session's `player_guid`, which the gateway sets to the session);
   `why:` repo:prototype/osfr-tools/src/kart_service.rs:1881-1886 (`GATE_HIT_SUBTYPE` arm calls `own_guid`), :2471-2482 (`own_guid`); repo:prototype/osfr-tools/src/kart_gateway.rs:684-687 (`player_guid: context.session`).

5. `old:` 2. a server clock: hits are accepted in monotonic server time, not in client time;
   `new:` 2. a server clock: hits are accepted in monotonic server time, not in client time (implemented: a claim whose clock predates the last accepted one is refused as a regression, `ClaimRate { delta_ms: 0 }`);
   `why:` repo:prototype/osfr-tools/src/kart_service.rs:2422-2425 (`check_movement`), :2551 (`check_movement` call from `claim_gate`).

6. `old:` 3. movement corroboration: the displacement between consecutive accepted samples must be reachable
   `new:` 3. movement corroboration: the displacement between consecutive accepted samples must be reachable (implemented in `check_movement`: `max_step_ms` gap, `max_speed_mps` budget with banked credit; the spawn-transform cross-check is not implemented);
   `why:` repo:prototype/osfr-tools/src/kart_service.rs:2426-2459, :300-306 (`max_speed_mps`, `max_step_ms` bounds).

7. `old:` 4. rejection on failure (teleport, back-tracking, duplicate, or out-of-order hits) rather than
   `new:` 4. rejection on failure (teleport, back-tracking, duplicate, or out-of-order hits) rather than (implemented: refused claims change nothing, and every in-window attempt counts against `max_claims`);
   `why:` repo:prototype/osfr-tools/src/kart_service.rs:28-29 (refused claims change nothing), :2539-2549 (`ClaimBudget`, race window), :2551-2554 (refusal returns before any state change).

8. `old:` **Original gate ids and gate geometry are unrecovered.** — already covered by correction 1; no second edit.

9. `old:` Server guidance: keep sending tail byte 1 for the local player's own vehicle and 0 for others (as
   `new:` Server guidance: the `33/11` tail is carried as a verbatim attribute block supplied by the lead's content, not built by the server, so the server does not currently choose the tail byte. If content is authored for the local vehicle, keep tail byte 1 for it and 0 for others (as
   `why:` repo:prototype/osfr-tools/src/kart_entry.rs:37-40 (33/11 tail as "a verbatim attribute block" from private content), :164 (`33/11` body layout).

**Unsure:**

- Section 1 "the native consumer picks locality from the packet guid plus a predicate-driven stack flag": client-side decompile claim. I did not check it in `client`/`ui`; the repo has no client parser to compare against.
- Section 2 "the packet has no client parse case at all (it is send-only)": repo:prototype/osfr-tools/src/kart_service.rs:14-16 says the same, but that rests on the decompile, which I did not re-read.
- Section 2 "What can be built" bullet 3 (expect the racer to approach the next waypoint with a distance and time window): broadly implemented by `check_movement` and the expected-gate attribution, but I did not confirm every window matches the note's wording.
- The lab artifacts (`lab/reports/kart-local-gate-binding-20261009T162829Z/`, proof sha256) are outside the repo, so I could not verify the hashes or checker output.
