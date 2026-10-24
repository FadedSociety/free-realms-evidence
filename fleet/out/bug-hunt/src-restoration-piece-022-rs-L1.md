<!-- fleet job=bug-hunt id=src-restoration-piece-022-rs-L1 status=done turns=6 usd=0.0093 tokens(read,write,in,out)=[76242, 31113, 14, 9344] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_022.rs lines 1-600 of 600

Window reviewed: `prototype/osfr-tools/src/restoration/piece_022.rs` lines 1-600. No high or medium defects found. Both findings below are low severity. Nothing in the window panics on client bytes: `decode_enter_request` checks length 17 before indexing bytes 12-16, and `read_u16`/`read_u64` are only reached after length checks. `register_house` validates before mutating, and `restore` builds a fresh router so a failed restore leaves `*self` untouched.

- **[low] prototype/osfr-tools/src/restoration/piece_022.rs:375-385 - `#[derive(Default)]` on `HousingEntranceRouter` sets `next_instance_id` to 0, contradicting the `new()` invariant (line 395-397: first assigned id is 1).**
  - Failure scenario: a caller builds the router with `HousingEntranceRouter::default()` instead of `new()`. The first `enter()` for any house then assigns runtime instance id 0 (lines 473-474), and `EntranceGrant.instance_id` is 0.
  - Reach: `Default` is a public derived impl. I found no in-tree call to `HousingEntranceRouter::default()`. `restore()` and `load_from_path()` both go through `new()` (lines 536, 560), so the persisted path is not affected. Reachability from a client packet is nil, so this is only a latent logic trap.
  - Fix: replace the derived `Default` with a manual impl that delegates to `new()`, or drop the derive and keep `new()` as the only constructor.

- **[low] prototype/osfr-tools/src/restoration/piece_022.rs:575-579 - if `File::create`, `write_all` or `sync_all` fails, the `?` returns before the cleanup at line 595, so the `.<name>.<pid>.tmp` file is left behind.**
  - Failure scenario: a save hits a full disk or an I/O error during `write_all`. `save_to_path` returns `SnapshotCorrupt`, which is correct, but a partial temp file stays in the data directory. Each failed save leaves another one, with a different pid suffix on each run.
  - Reach: `save_to_path` (line 544) → `write_atomic` (line 568). This is a server-side save path, not client input. The destination file is not corrupted, because the rename never runs.
  - Fix: wrap the create/write/sync block so that any error calls `fs::remove_file(&temporary)` before returning, for example by moving the block into a closure and cleaning up on `Err`.

Observations deliberately not reported (documented as deferred to piece 023 in the module header and doc comments): `enter()` (line 453) does not check `is_locked` or any invite/permission state, and `request.unknown != 0` (line 499) sets the client-visible `is_preview` flag from a client-supplied int. Both are acknowledged in the module as unrecovered or out of scope, and I could not show a concrete server-state consequence from inside this window.
