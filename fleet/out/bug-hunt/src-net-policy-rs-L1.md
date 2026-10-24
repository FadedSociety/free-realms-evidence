<!-- fleet job=bug-hunt id=src-net-policy-rs-L1 status=nothing_found turns=4 usd=0.0046 tokens(read,write,in,out)=[19739, 14987, 10, 5085] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/net_policy.rs lines 1-169 of 169

I read `prototype/osfr-tools/src/net_policy.rs` lines 1-169 in full and traced its callers (`osfr-login.rs` 99-112, 202-224, 297-310, 827-843; `osfr-gateway.rs` 370, 510-521; `social_chat.rs` 44-50). I found no defect I could tie to a line and show reachable from client input.

Candidates considered and dropped:

- **`is_private_network` / `allowed` (lines 11-24):** the IPv4 ranges (RFC 1918, 169.254/16, 100.64/10) and the IPv6 unique-local check `(segments[0] & 0xfe00) == 0xfc00` are correct. Wildcard `0.0.0.0` and `::` are not admitted, which the test at lines 130-131 confirms. IPv4-mapped IPv6 (`::ffff:a.b.c.d`) and IPv6 link-local are denied even under `--allow-lan`. That is fail-closed, and the callers bind concrete addresses, so no client path opens up.
- **`Bucket::take` (lines 43-52):** `saturating_duration_since` handles a `now` earlier than `last`. The `min(burst)` cap and the refill arithmetic are sound, and a rejected take spends nothing. A cost above burst simply always refuses, with no panic.
- **`KeyedBuckets::allow` eviction (lines 76-93):** the `retain` closure keeps busy buckets and drops idle ones. The probe works on a copy, so it does not mutate state. An evicted idle key is equivalent to a fresh `Bucket::full`, so eviction changes no behaviour. The `max_keys` cap is enforced after eviction, so memory stays bounded.
- **Spray behaviour:** when the key set is full of busy keys, new keys are refused. That is the documented design, not a defect.
- **`remove` (lines 99-102)** and **`len`/`is_empty`:** straightforward, with no client-controlled indexing.
- **Tests (lines 112-168):** excluded from scope, and the assertions match the implementation as I read it.

No panic, unbounded-growth, atomicity, trust, or comparison defect appears in the window.
