<!-- fleet job=bug-hunt id=src-bundle-budget-rs-L1 status=nothing_found turns=7 usd=0.0041 tokens(read,write,in,out)=[44227, 14622, 16, 3708] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bundle_budget.rs lines 1-61 of 61

No defects found in `prototype/osfr-tools/src/bundle_budget.rs` lines 1-61.

What I checked:
- **`stage` (l.42-54):** the length sum is over in-memory `Vec` lengths, and the add is `saturating_add`, so no overflow or panic is reachable. Refusal returns `io::ErrorKind::InvalidData` and the charge stays. The module note (l.9-14) and the doc (l.41) document that as deliberate, so it is not a defect.
- **`message` (l.36-38):** `starts_with(&[0, 25])` is bounds-safe for short input. It matches the bundle detection used elsewhere (`gateway.rs:1414`, `gateway.rs:711`, `trace.rs:87`, `login.rs:97`), so the flag agrees with the other bundle checks.
- **Callers:**
  - `gateway.rs:1439-1443` and `:1806` slice `outcome.replies[counted_replies..]`. I found no truncate, drain, or clear on `outcome.replies` inside `handle_at`, so the slice cannot go out of range. The reassignments at `gateway.rs:1363` and `:1375` are on other outcome objects.
  - `osfr-gateway.rs:1522-1526` sets the budget per message and resets it to `outside()` afterwards.
  - `osfr-gateway.rs:1740` charges the replies of the staged child before commit. That is the accounting the module note says is intentional.
- **`used` (l.58-60):** observation only, with no server-side authority.

Nothing in the window is reachable as a panic, an unbounded allocation, or a logic contradiction. The one open question, that refused bytes are never refunded, is an explicitly accepted policy and is outside this window's defect criteria.
