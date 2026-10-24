<!-- fleet job=test-audit id=tests-pet-bots-rs-L1 status=done turns=7 usd=0.0074 tokens(read,write,in,out)=[90933, 24543, 16, 6884] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/pet_bots.rs lines 1-612 of 612

Window reviewed: `prototype/osfr-tools/tests/pet_bots.rs` 1-612. The main scenario is sound: `wait_for` drains older inbox messages, so the actor-before-activation order is enforced, and `pet_guid` is an XOR tag (injective), so the B-owned negative check is meaningful. Dismiss ignores its id word (`pets.rs:947`), so the zero id in the raw dismiss is harmless. Findings:

- **[medium] tests/pet_bots.rs:548 a_saved_pet_is_summoned_seen_by_two_players_and_dismissed (and module doc, lines 1-2: "a saved owned pet is listed after relog") - the roster/listing claim is never asserted.** `is_pet_list` (line 543-545) is defined but never called anywhere in the file, and `#![allow(dead_code)]` (line 4) hides the unused-helper warning. The test only checks actor, active and removal messages.
  - Why it cannot catch a regression: the gateway could stop sending the saved roster (`53/5`) on login or after relog, or send an empty roster, and every assertion here would still pass, because summon, active, neighbour and late-arrival checks never depend on the roster.
  - Fix: after `let mut a = rig.connect(0, "petA")` (line 560), add `a.wait_for(T, |m| is_pet_list(m) && m.windows(4).any(|w| w == pet_id.to_le_bytes())).expect("A: saved roster lists the pet")`, or otherwise assert the roster contains `pet_id`. Remove the helper if the claim is dropped.

- **[medium] tests/pet_bots.rs:565 a_saved_pet_is_summoned_seen_by_two_players_and_dismissed - the comment says "neither A nor B sees a B-owned actor", but only A is checked.** Lines 571-578 wait on `a` only. B's refusal wait at 567-570 consumes everything older in B's inbox, so an actor for B sent to B would be silently drained, not caught.
  - Why it cannot catch a regression: a server change that echoes an unowned summon's actor to the requester (B) before the refusal would still pass, since B's inbox is never checked for that actor.
  - Fix: after the refusal, assert on `b` too, e.g. `assert!(b.wait_for(Duration::from_secs(1), |m| is_pet_actor(m, PetService::pet_guid(gb))).is_err(), "B saw an unowned pet actor")`, with the check placed before any later `wait_for` on `b` for a pet message.

- **[low] tests/pet_bots.rs:567-568 a_saved_pet_is_summoned_seen_by_two_players_and_dismissed - the refusal match is a loose substring, "do not own".** `pets.rs:1803` ("pet is not owned" → "You do not own that pet.") and `pets.rs:1805` ("You do not own that pet item.") both contain it, so a refusal for the wrong reason (for example an item-path refusal) would satisfy the check.
  - Why it cannot catch a regression: a change that refuses B for the item-path reason, or any other "do not own" text, still passes.
  - Fix: match the exact text, `t == "You do not own that pet."`, rather than `contains("do not own")`.
