# pyconstlock

![PyPI](https://img.shields.io/pypi/v/pyconstlock)
![Python](https://img.shields.io/pypi/pyversions/pyconstlock)
![License](https://img.shields.io/badge/license-MIT-green)
![Downloads](https://img.shields.io/pypi/dm/pyconstlock)
![Last Commit](https://img.shields.io/github/last-commit/austinewoody/pyconstlock)
![Stars](https://img.shields.io/github/stars/austinewoody/pyconstlock)

A lightweight Python package for creating constant-style values that cannot be reassigned or deleted.

Python does not have a built-in `const` keyword like JavaScript. `pyconstlock` gives you a simple protected object for constant values.

## 📦 Installation

```bash
pip install pyconstlock


Usage

from pyconstlock import Const

const = Const()

const.API_KEY = "abc123"
const.MAX_USERS = 50
const.APP_NAME = "My App"

print(const.API_KEY)
print(const.MAX_USERS)
print(const.APP_NAME)

const.MAX_USERS = 100  # error

Features

-Prevent reassignment
-Prevent deletion
-Enforce uppercase naming
