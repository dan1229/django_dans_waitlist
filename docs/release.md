# Release Guide

This guide provides instructions on how to package and release the Django Dans Waitlist package.

## Packaging

**IMPORTANT:** You MUST update your version number in `setup.cfg` before anything else as this is what actually determines the version!

### Continuous Deployment (CD)

To release automatically, follow these steps:

1. **Update Version Number**: Ensure the version number in `setup.cfg` is updated.
2. **Run Release Phase**: Go to GitHub Actions and run the 'release' phase.
3. **Provide Version Number**: It will ask for a version number of the form "X.X.X" and handle everything.

**NOTE:** Even when releasing via CD, you MUST still update your version number in `setup.cfg`!

### Manual Release

To manually build and release the package, follow these steps:

1. **Update Version Number**: Ensure the version number in `setup.cfg` is updated.

2. **Build the Package**: Run the following commands to build the package:

```bash
python setup.py sdist
python setup.py bdist_wheel
```

3. **Release the Package**: Run the following command to upload the package to PyPI:

```bash
python3 -m twine upload --repository pypi dist/*
```

This expects you to have the proper credentials in your `$HOME/.pypirc` file.


-------------------------------------------------------

##### [https://danielnazarian.com](https://danielnazarian.com)

##### Copyright 2024 © Daniel Nazarian.