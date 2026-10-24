<!-- fleet job=pin-audit id=tests-client-areas-rs status=done turns=4 usd=0.0044 tokens(read,write,in,out)=[32823, 19118, 10, 3330] model=claude-haiku-5-5 -->
# tests/client_areas.rs

Three of the screened lines pin Halloween window boundaries from `data/content/client_areas.json` `seasons[0]` (name "Halloween", start 9/20, end 11/11). `shipped()` loads that file, so these expectations break if the event window is retuned while the code is still correct.

- **tests/client_areas.rs:111 season_windows_are_inclusive_wrap_the_year_and_follow_the_offset - pins `9/20` (day before the start) from `data/content/client_areas.json` `seasons[Halloween].start_month` / `start_day`.**
  **Fix:** read it through the Halloween row of `client_areas.json` (load the file in the test, pick `seasons` where `name == "Halloween"`, and build `at(2026, start_month, start_day - 1, 23, 59)` from it), or bound it as "the day before the window start is outside".

- **tests/client_areas.rs:112 season_windows_are_inclusive_wrap_the_year_and_follow_the_offset - pins `9/20` (first day) from `data/content/client_areas.json` `seasons[Halloween].start_month` / `start_day`.**
  **Fix:** read it through the same Halloween row (`at(2026, start_month, start_day, 0, 0)`), so the inclusive-start check follows the data. The test also relies on `utc_offset_minutes` = 0 from the same file; if that is retuned, the midnight-UTC instant falls on the previous local day. Build the instant from the offset in the file too, or bound the check.

- **tests/client_areas.rs:117 season_windows_are_inclusive_wrap_the_year_and_follow_the_offset - pins `11/12` (day after the end) from `data/content/client_areas.json` `seasons[Halloween].end_month` / `end_day`.**
  **Fix:** read it through the Halloween row (`at(2026, end_month, end_day + 1, 0, 0)`), or bound it as "the day after the window end is outside".

Not findings (checked): 110 uses Oct 21, a mid-window input rather than a boundary, so it does not pin a data value. 119 and 129-130 use Winterfest (absent from the data) and the test-built Yule fixture. 159-162 use the test's own "H" fixture, which the test sets itself (it only coincidentally matches the data). 232 uses Oct 1, an in-season input, and 279-282 use an empty fixture with no seasons. 113-116 and the other screened lines are not findings either.
