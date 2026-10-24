<!-- fleet job=pin-audit id=tests-pets-rs status=nothing_found turns=4 usd=0.0019 tokens(read,write,in,out)=[16204, 9404, 10, 1133] model=claude-haiku-5-5 -->
# tests/pets.rs

No findings for `tests/pets.rs:217` (`adopts_owned_item_and_generated_name_validation`).

`service.rename(id, 60, 0)` passes an out-of-range zero-based index into the `PetNames.txt` first-name table. `src/pets.rs:261` requires that table to have exactly 60 rows, so 60 is one past the end and the error is expected. This is a layout fact, not a value from a data file. The screen's "price / rename fee" concern does not apply: `src/pets.rs:837` says name-change purchases are not part of this code path, and no fee field is read by `rename`.
