# Proposal

## Why

`LAB7.1` imports Pillow through `PIL` in its login and home views, but the project has no dependency file for that lab. As a result, a fresh environment can fail at startup with `ModuleNotFoundError: No module named 'PIL'`, and the repository does not give users a consistent installation path.

## What Changes

- Declare Pillow as a dependency for `LAB7.1` and document the installation command from the repository root.
- Document a matching Python invocation so the package is installed into the interpreter that runs the app.

## Capabilities

### New Capabilities

- `python-dependency-setup`: Reproducible installation of Python dependencies required by a lab.

### Modified Capabilities

None.

## Impact

- `LAB7.1/Views/login_view.py` and `LAB7.1/Views/home_view.py` depend on Pillow's `PIL` imports.
- Add a `LAB7.1` dependency manifest and installation guidance. No application API changes are expected.
