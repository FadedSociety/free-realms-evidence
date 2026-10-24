<!-- fleet job=pin-audit id=tests-minigame-rs status=nothing_found turns=5 usd=0.0023 tokens(read,write,in,out)=[20077, 11270, 12, 1428] model=claude-haiku-5-5 -->
# tests/minigame.rs

No findings in `prototype/osfr-tools/tests/minigame.rs` for the three screened lines.

- **294 / 297 (`flash_start_play_win_close_has_exact_packet_bytes_and_once_only_reward`) and 573 (`reward_api_duplicate_key_is_inert`):** the `15` is not from a data file. It is the test's own fixture arithmetic. `Fixture::new(10)` (lines 23–37) writes a starting coin balance of 10 into a temp `inventory.json`, and `grant()` (lines 247–261) builds a `RewardGrant` with `coins: 5` inline. 10 + 5 = 15. Retuning any file under `data/content/` does not affect it, because neither the fixture nor `grant()` loads a content file.
- **294 (`won.reward_packets[0]` bytes `[38, 0, 19, 0, 15, 0, 0, 0]`):** the `15` in the packet is the same 10 + 5 balance, serialized by the code under test. The other bytes are protocol layout. The line is not a finding.
- **294 (`won.reward_packets[1][..4]` = `[50, 0, 1, 1]`):** opcode and flag bytes. Not a finding.

No edit is needed. If the team wants these to be more self-describing, the sum could be written as `10 + 5` using the fixture's own values, but that is optional.
