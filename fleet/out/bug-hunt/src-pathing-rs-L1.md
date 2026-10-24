<!-- fleet job=bug-hunt id=src-pathing-rs-L1 status=nothing_found turns=6 usd=0.0062 tokens(read,write,in,out)=[45944, 17191, 14, 7261] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/pathing.rs lines 1-185 of 185

No reportable defects in `prototype/osfr-tools/src/pathing.rs` lines 1-185.

Checked and dropped (with reasons):

- **Body indexing in `parse` (lines 82-92):** `word`/`vec4` index `body[at..at+4]` only inside `(body.len() == BODY).then(|| ...)`, which is lazy, so the reads (max offset 48 of 52) are in range. Non-finite values are refused at line 135, before any use.
- **Reach and overflow (lines 138-143):** the 4D reach sum is written as `!(reach <= MAX)`, so NaN and overflow to infinity are refused. Because `reach <= 90000`, every per-axis difference is at most 300, so the `lerp` values (lines 172, 180) cannot overflow.
- **Segment count and output size (lines 166-167, 183):** `run` is bounded by about 424 m, so `segments` is at most 85, clamped to 79. That gives at most 80 points, equal to `MAX_POINTS`, and `segments >= 1` rules out division by zero in `t = i / segments`.
- **Zone check and grid lookup (lines 144, 158-164):** `from` is held within 300 m of the server's `player` position, and `to` within 300 m of `from`, so `Terrain::height_at` (terrain.rs:102-121) sees bounded coordinates. Its `floor() as i64` saturates rather than panicking, and the `c + 1` step cannot overflow at these magnitudes.
- **Rate budget (lines 147-157):** the window reset uses `saturating_sub`. Budget is spent only on answered requests, and the reset happens before the `used` check, so the budget cannot be bypassed by ordering.
- **Lint-level observation, not reported:** `answer` (lines 117-118) returns `Some(Err(Malformed))` for any 98/1 frame of the wrong length, before the kind check, while the doc at line 104 says `None` for anything that is not kind 1 or 2. The caller (gameplay.rs:2255-2266) then returns an empty outcome, skipping the later handlers. The only effect is on malformed frames that no later handler would act on (gateway.rs:505-506 routes 98/1 to "pathing" and nothing else handles family 98), so I found no observable impact and did not report it.
