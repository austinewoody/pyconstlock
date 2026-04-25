# pyconstlock

A simple Python utility to enforce constant variables.

## Installation

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