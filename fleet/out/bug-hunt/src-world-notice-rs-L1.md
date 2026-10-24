<!-- fleet job=bug-hunt id=src-world-notice-rs-L1 status=nothing_found turns=10 usd=0.0068 tokens(read,write,in,out)=[116288, 20084, 22, 6281] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/world_notice.rs lines 1-160 of 160

I read `world_notice.rs` lines 1-160 in full and traced its callers. I found no defect that meets the criteria, so I am not reporting any finding.

What I checked:
- **`parse` (51-75):** `command.get(..COMMAND.len())` and `command.get(COMMAND.len()..)` are slice-safe for non-ASCII input (they return `None` rather than panicking on a non-char boundary). The byte bound is checked before the char count, so the count never walks an oversized line. The control-character test covers `< 0x20` and `0x7f`. Trimming and the whitespace rule match `split_whitespace` at gameplay.rs:4326, so the two paths agree.
- **`encode` / `chat::system` (chat.rs:82-92):** escaping can grow the text by at most 4x (about 8 KB for a 2048-byte input), and the u32 length is safe. The broadcast is encoded once, not per recipient (delivery.rs:116-126).
- **`stage` (85-90):** the caller takes `out.broadcast` only on success. In gateway (osfr-gateway.rs:1669-1684) the notice is queued only after `commit_outcome` succeeds, so a failed transaction does not broadcast.
- **Authority:** `gameplay.rs:4326` (dispatch from `handle`) is gated by `tool = may_run(command)`, which requires `dev_tools || role_commands` and `can_run_realm_command`. `handle` (gameplay.rs:5296) runs `command_refusal` first. `developer_command_denied` (gameplay.rs:3698) denies `broadcast` for any player without the right role. `account_store.rs:52-77` allows `broadcast` only for Admin, since Builder's list does not include it. So a player cannot reach the fan-out.
- **Raw slicing at gameplay.rs:4325:** `&text.trim()["realm ".len()..]` is safe because the lowercase `strip_prefix("realm ")` at 4307 already proved the first 7 bytes are ASCII `realm `.

Known minor behaviour, not reported: `realm  broadcast x` (two spaces) produces the usage refusal, since `raw` keeps the leading space. That is a cosmetic refusal, not a defect.
