<!-- fleet job=bug-hunt id=src-login-auth-rs-L1 status=nothing_found turns=8 usd=0.0098 tokens(read,write,in,out)=[87199, 25719, 18, 11521] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/login_auth.rs lines 1-365 of 365

No defects that meet the criteria in `prototype/osfr-tools/src/login_auth.rs` lines 1-365. I read the whole window and checked the callers in `src/bin/osfr-login.rs` (`answer`, lines 230-290, and the `redeem_identity` call at line 740) and `net_policy::Bucket::take` (lines 27-53).

Checked and dropped:

- **Panics on client input.** Nonce and token lengths are checked before slicing or `try_from`. `answer` checks `body.len() == 134` before indexing `body[6..38]`, `body[38..70]` and `body[70..134]`. Handle length is bounded to 3..=32 before `10 + length`, so there is no overflow. Hex encoding indexes `HEX` with values 0..=15. `Signature::from_slice` and `VerifyingKey::from_bytes` return `Result`. No `unwrap` is reached from client bytes.
- **Atomicity.** The challenge is consumed before key and signature checks, and the token is pushed only after every check passes, so there is no partial state. `redeem_identity` consumes the token before the binding check, which the doc states is deliberate (one-use). `verify` errors after consuming a challenge, which the doc also states.
- **Token and challenge uniqueness.** Duplicate nonces and digests are rejected with bounded retries. The full scan in `redeem_identity` keeps the last match, which is unique because digests are unique.
- **Lockout counting in `LoginFailures`.** I traced `failed()` against `Bucket::take` (which spends only on success). Five failures lock on the fifth, which matches the doc and `tests/login_auth.rs:20-25`. The lock expires after 60 s, and locked attempts do not extend it. `succeeded()` clears only that account.
- **1024-entry table fills from `allow()` on new handles.** This is availability-only and is pinned by the test named `..._unknown_capacity` (`tests/login_auth.rs:35-41`), so it is intended behaviour, not a defect.
- **Enumeration and timing.** Unknown accounts run the same signature check and return the same error. This matches the stated design.

Nothing in this window can be tied to a remote crash, save corruption, item or coin gain, or client-chosen authority.
