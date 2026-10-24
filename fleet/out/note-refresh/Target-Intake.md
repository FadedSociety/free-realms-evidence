<!-- fleet job=note-refresh id=Target-Intake status=done turns=10 usd=0.0114 tokens(read,write,in,out)=[200464, 43618, 22, 7963] model=claude-haiku-5-5 -->
# notes/Research/Target Intake.md

**Verdict:** minor drift. Most checkable claims hold at the tip. One status cell is stale. The archive-path and lab-manifest claims cannot be checked from the repo, because `lab/` is outside it.

**Corrections:**

- `old:` Exact executable build not established; no populated FileVersion/ProductVersion resource.
  `new:` Client build confirmed as 1.910.1.530630 by the disposable-copy client log; the PE carries no populated FileVersion/ProductVersion resource.
  `why:` `repo:notes/Research/Free Realms Recovery.md:72` says "The actual supplied client was subsequently launched in disposable copies. Its log confirms version `1.910.1.530630`." `repo:recovery-manifest.json:138-140` records `original_client_baseline.version` as `1.910.1.530630`. The Build Guides and Research notes also treat the native client as 1.910.1.530630 (e.g. `repo:notes/Build Guides/Network/Gateway and Transport.md:285`). The "no populated resource" half is a PE fact I could not re-check, so it is kept as written.

**Unsure:**

- **"recovered OSFRServer project targets net48"** (row "Server runtime"). I found no net48 or target-framework evidence in the repo. `repo:notes/Research/Verified Recovery Workflow.md:20` says the `.csproj` files were synthesized by ILSpy (7 present, no `bin`/`obj`), so the target framework would come from synthesized metadata. The projects themselves sit in `lab/`, which is absent from the repo.
- **"Server config declares `1.910.1.530630`"** (row "Client build"). The supplied server's config is outside the repo. Community configs carry this version (for example `repo:OpenSourceFreeRealms/ofrserver/Config.json:17`), but that does not verify the supplied one.
- **"Supplied launcher points to loopback port 20260"** (row "Local gateway hint"). The supplied launcher is outside the repo. In the repo, 20260 appears as the address of our Rust gateway in `repo:prototype/osfr-tools/README.md:36` and in tests. The repo's own launcher defaults to 127.0.0.1:20042 (login) and 20041 (gateway) (`repo:notes/Design/Public Transport.md:42`; `repo:launcher/src/main.rs:426`). So this row may describe our gateway rather than the supplied launcher, but I could not settle it.
- **Archive hashes, byte counts, "13 server files (6,488,668 bytes)", "1,762 client files", "24 … `.pack` files", "`FreeRealmsMac.exe` is also an x86 Windows PE" and "not received the Ghidra pass".** These are consistent with `repo:notes/Research/Verified Recovery Workflow.md:13-22`, `repo:notes/Research/Universal Modder Assessment.md:36` (1,762 files), `repo:notes/Research/Free Realms Recovery.md:12,23` and `repo:MODLOG.md:158`. The underlying `lab/manifests` could not be opened from the repo.
- **"Main PE timestamp corresponds to March 2014"**. Only the "2014 client" wording in `repo:notes/Project Map.md:91` is visible. I did not check the PE header.
