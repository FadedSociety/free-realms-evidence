<!-- fleet job=test-verify id=tests-harvesting-reward-catalogue-rs-L1-f1 status=done turns=3 usd=0.0031 tokens(read,write,in,out)=[9820, 10626, 8, 3412] model=claude-haiku-5-5 -->
# high: tests/harvesting_reward_catalogue.rs:147

**Verdict:** `confirmed`

**Evidence:**
- The state half of the test cannot fail under any change to `Gameplay::load`. Line 156 passes `state.clone()`, so the value the code receives is a different object from `state`. Lines 158-162 then serialize `state`, the original, and compare it with `before_state`, which was taken from that same `state` at line 151. Nothing that `load` does to its argument can reach `state`. The assertion is a tautology.
- The signature is `pub fn load(directory: &Path, state: Option<GameplayState>)` (`src/gameplay.rs:602`), so the state is taken by value. A caller cannot observe mutation of the value it moved in. The "caller's save" wording in the test name and message at line 161 describes something the API does not expose.
- The content-bytes half (lines 163-167) is real. `write_shipped` writes the shipped configuration, and a refused load that rewrote `harvesting.json` would change the bytes and fail that assertion. The `load_error` helper (lines 84-89) does panic if `load` returns `Ok`, so the refusal itself is also checked.

**Correction to the proposed fix:** the suggested rewrite is also vacuous. Serializing a state, deserializing it, passing the copy to `load`, and then comparing `serde_json::to_value(&state)` with `before_state` still compares `state`, which is never passed. Keeping "a second independent copy" does not help either, because the code only ever receives a moved value. No assertion on the caller's side can detect a mutation of the passed-in clone.

**Minimal fix:** delete the state assertion at lines 158-162 and rename the test to something like `refused_load_refuses_without_rewriting_content_bytes`. The byte-level check is the only meaningful preservation check here. A stronger canary, if one is wanted, would be to assert that the refused load leaves the directory's other files unchanged (the test does not check any file except `harvesting.json`).
