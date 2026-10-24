You screen test assertions from a Rust game server (a revival of the kids' MMO Free Realms). The team's rule: gameplay
values (damage, health, prices, rewards, XP, timers, drop or spawn rates) live in data files and must stay
retunable, so a test should read such a value from the data or check a sane range, never pin the exact number.
Pinning counts, ids, packet layouts and protocol constants is fine.

Each line is "key: path:line assertion". For EVERY line, answer exactly one output line: key|pinned|kind|data
- pinned: yes (the assertion pins an exact gameplay number that a designer would retune), no, or unsure.
- kind: damage, health, price, reward, xp, timer, rate, count, id, layout, other.
- data: for yes or unsure, the data file or field the number probably comes from (a few words), else empty.

Answer only the lines, one per key, nothing else.
