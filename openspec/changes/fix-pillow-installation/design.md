# Design

## Context

See proposal.md - Why. `LAB7.1` imports `PIL` in two views and currently has no dependency manifest or setup README. The repository's `LAB7` manifest belongs to a different lab and should not be used as `LAB7.1`'s dependency source.

## Goals / Non-Goals

**Goals:**
- Make Pillow installation repeatable for `LAB7.1`.
- Keep dependency installation tied to the Python launcher used to run the lab.

**Non-Goals:**
- Diagnose environment-specific network, proxy, permission, or Python installation failures without the exact error output.
- Change application image handling or other labs' dependencies.

## Decisions

- Add `LAB7.1/requirements.txt` with the distribution name `Pillow`. Python imports it as `PIL`; using the distribution name lets pip resolve the intended package. A separate manifest avoids mixing this lab's dependencies with `LAB7`'s MySQL connector.
- Add setup guidance to `LAB7.1/README.md` using `py -m pip install -r LAB7.1/requirements.txt`, followed by `py LAB7.1/main.py`. Using `py -m pip` ensures pip targets the launcher-selected interpreter.
- Do not pin a version initially. The project has no stated compatibility bounds, and Pillow publishes wheels for supported Python versions; an unnecessary pin could become stale.

## Risks / Trade-offs

- [A package-index or interpreter-specific installation failure may remain] → The documented command provides a reproducible baseline; exact environment errors require their output to diagnose.

## Migration Plan

Users install the new manifest once from the repository root, then run `LAB7.1/main.py` with the same `py` launcher. No data migration or rollback is needed; removing the manifest and setup section reverses the repository change.
