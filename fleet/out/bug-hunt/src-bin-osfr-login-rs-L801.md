<!-- fleet job=bug-hunt id=src-bin-osfr-login-rs-L801 status=done turns=8 usd=0.0101 tokens(read,write,in,out)=[73883, 27634, 18, 11873] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr-login.rs lines 801-946 of 946

Window reviewed: `prototype/osfr-tools/src/bin/osfr-login.rs` 801-946 (plus `Session::handle`, `Session::application`, `BrokerPeer` polling at 230-800 for the callees). I found one candidate; it is weak, so it is reported at low severity with the uncertainty stated.

- **[low] prototype/osfr-tools/src/bin/osfr-login.rs:837 - `broker.poll(...)?` turns any non-`WouldBlock` accept error into a return from `run()`, so one transient error on the AUTH2 listener exits the whole login server and drops every UDP session.**
  - **Failure scenario:** a TCP peer completes a connection to the AUTH2 listener and then resets it before the server calls `accept`. If the kernel returns that pending network error from `accept()` (Linux `accept(2)` documents that it can pass already-pending network errors on the new socket), `BrokerPeer` polling at line 319 (`Err(e) => return Err(e)`) returns the error. Line 837 propagates it with `?`, `run()` returns `Err`, `main` at 913-918 prints it and calls `exit(1)`, and all UDP sessions at 826 are lost.
  - **Reach:** the remote peer reaches `Broker::poll` through `TcpListener::accept` in `poll` (lines 295-320), called every loop iteration at 836-838. Nothing upstream catches the error: the only `accept` error that is tolerated is `WouldBlock`. The `peers.len() >= 16` and `net_policy` checks run only after a successful accept, so they do not stop this path.
  - **Uncertainty:** I could not confirm which errno a remote reset actually produces on the deployed kernel, and EMFILE is not remote-reachable in practice (accepted streams are bounded at 16 or dropped). So the remote trigger is plausible but unproven.
  - **Fix:** in `poll` at 318-320, treat transient accept errors (`ConnectionAborted`, `ConnectionReset`, `Interrupted`, and similar) as `continue`/`break` rather than `return Err`, or log and continue in `run()` at 837 instead of `?`.

No other defects in the window. Checked and dropped:
- The `Ok(true)` / `Ok(false)` removal test at 872-880 is consistent with `handle` (Ok(true) only on a matching disconnect, Ok(false) otherwise).
- The 32-session cap at 852 and the retry-only reuse at 847-851 are bounded and correct.
- The `retain` cleanup at 893-909 is correct; short-circuiting `all` at 906 is safe because the session is then removed.
- `Request::parse` at 408-422 (called from 844) guards its slicing and clamps values, so the handshake path does not panic.
- `Bucket::take` argument order at 873 matches `net_policy.rs:43`.
- `recv_from` error handling at 884-891 treats the Linux-relevant transient kinds as non-fatal; the remaining fatal case is not a demonstrated remote trigger.
