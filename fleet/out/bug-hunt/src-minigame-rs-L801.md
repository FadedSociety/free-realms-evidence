<!-- fleet job=bug-hunt id=src-minigame-rs-L801 status=nothing_found turns=7 usd=0.0047 tokens(read,write,in,out)=[55853, 20171, 16, 3256] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/minigame.rs lines 801-822 of 822

Window `prototype/osfr-tools/src/minigame.rs:801-822` (end of `family39_header`, `validate_asset_name`, `read_i32`, `invalid`) has no defect I can tie to client input, a save, or a server state change.

What I checked:

- **`family39_header` (801-802):** pure serialization into a fresh `Vec`. No panic, no unbounded growth, no state mutation.
- **`read_i32` (816-818):** slices `bytes[offset..offset+4]` with no bounds check, so it would panic if called short. Every caller in this file is length-guarded:
  - `minigame.rs:304-306` runs only after `packet.len() != HEADER_LEN` (15) returns early, and reads offsets 3, 7 and 11.
  - `minigame.rs:401-402` runs only when `packet.len() == 12`, and reads offsets 4 and 8.
  The other `read_i32` hits in the grep are separate functions in other modules. None is a caller of this one.
- **`validate_asset_name` (804-814):** accepts `.` and `-` without rejecting a leading dot, so `..` passes. That is looser than `mining.rs:2421-2434`, but it is not exploitable. The only caller is `RunSpec::validate` at `minigame.rs:102`, and the movie string is never a client value:
  - `chess_service.rs:614` uses the constant `chess::MOVIE`.
  - `harvesting_lifecycle.rs:395` and `mining_lifecycle.rs:385` use engine launch-movie content.
  - The string is sent to the client via `flash_launch_packet` (`minigame.rs:708`). I found no `join`/`open` on it on the server side.
- **`invalid` (820-822):** a constructor only.

I did not report the `validate_asset_name` leniency as a finding. Without a server-side path use or a client-supplied source for the name, it does not meet the bar.
