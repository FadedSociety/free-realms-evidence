<!-- fleet job=bug-verify id=src-bin-osfr-bot-rs-L1-f1 status=done turns=5 usd=0.0057 tokens(read,write,in,out)=[41116, 18045, 12, 5969] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/bin/osfr-bot.rs:178-214

**Verdict:** confirmed (the mechanism is real), but the severity is overstated. Severity if confirmed: **low**.

**Evidence**

1. **Module tree.** `osfr-bot.rs` is a binary target, not a library module. It is built by `scripts/bundle/make_bundle.py:280` and used by `scripts/stress/run.py` and `scripts/bundle/check_bundle.py`, and its code is pulled into tests via `#[path]`. It is a headless test and stress client. It is not server code and is not in `src/lib.rs`.

2. **Reach.** `osfr-bot.rs:457-458` accepts datagrams only from `peer == self.config.gateway`. `osfr-bot.rs:486` passes each reliable message to `receiver.receive`, then `osfr-bot.rs:509` calls `logical_messages` when no login crypto is active. Nothing upstream checks bundle nesting. So the trigger needs a datagram from the configured gateway address. That means a malicious gateway, or a spoofed UDP source on the LAN, since the CRC is not authentication. Player traffic never reaches this code.

3. **Mechanism (confirmed).** `osfr-bot.rs:179` matches `[0,25]`, and the nested child matches the same prefix. `osfr-bot.rs:212` recurses with `child.to_vec()`, and the parent `message` stays alive. Recursion depth is attacker-controlled, so unbounded recursion and quadratic copying are real. The gateway does reject nesting at `gateway.rs:679-680` ("nested message bundles are unsupported"), and the bot has no equivalent check.

4. **Correction to the claim's size cap.** The claim says the receiver accepts up to 16 MB (`max_message`, line 335). That is wrong in effect. `soe.rs:315-343` shows `ReliableReceiver::new` clamps `max_message` with `.min(MAX_LOGICAL_MESSAGE)`, and `soe.rs:22` sets `MAX_LOGICAL_MESSAGE = 1_048_576`. The effective cap is 1 MiB. The attack still works at that size: about 3 bytes per level gives roughly 350k levels, and the copying cost is larger still. The 40k-level example is still valid.

**Why the severity is low, not medium**

- The impact is the bot process dying. It is a test client. The bot cannot corrupt saves, grant items or coins, or crash the gateway, login or any player-facing server.
- The rubric's "high" tier (remote player crashes the server, corrupts a save, gains items) does not apply. A "medium" rating is also not supported, because the trigger needs the gateway peer or spoofing the gateway address.

**Corrected fix:** the claimed fix is fine. After `take` at line 209, return early if `child.starts_with(&[0, 25])`, matching `gateway.rs:679`. Also fix the cap statement to 1 MiB, not 16 MB. Optionally, reject `size < 2` as the gateway does at `gateway.rs:675`.
