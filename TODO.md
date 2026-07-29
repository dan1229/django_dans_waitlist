# TODO - Django Dan's Waitlist
#### By: [Daniel Nazarian](https://danielnazarian) 🐧👹

-------------------------------------------------------
## [Unreleased]
-----
### Improvements



#### something something webhooks?


#### analytics of some sort?


#### integrations with hubspot or something?


#### install the standard release workflow
- there is no `.github/workflows/detect-version.yml` here at all - releasing means opening
  the Actions tab and running `release.yml` by hand, and the GitHub release object gets
  whatever generic body that job writes. This is a public PyPI package, so strangers read
  that body
- the standard makes the release a commit: a `release: [X.X.X]` subject on main tags the
  repo, cuts a `release/X.X.X` marker branch, and creates the release with notes read out
  of `CHANGELOG.md` at that SHA
- keep `release.yml` and wire it as the downstream dispatch so PyPI publishing still runs.
  It is `workflow_dispatch`, not `on: push: tags:`, so it will not stop firing once CI
  pushes the tag
- turn ON the version-source check using the **`setup.cfg`** variant - the version lives
  there, not in `pyproject.toml`
- tags stay bare (`1.0.3`, not `v1.0.3`)
- note the drift while in here: `setup.cfg` and `CHANGELOG.md` both say 1.1.0 but the newest
  tag is 1.0.3, so 1.1.0 was written and never released
- `docs/release.md` still describes the run-it-from-the-Actions-tab flow and has to be
  rewritten in the same change, or it contradicts the workflow the day it lands
- `/dan:release-setup` installs it


-------------------------------------------------------

##### Copyright 2024 © Daniel Nazarian.
