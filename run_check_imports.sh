#!/bin/bash

PROJECT_DIR="/lustrehome/clolorusso/ClaudiaLorusso/tools/revtrack"

cd "$PROJECT_DIR" || exit 1
source "$PROJECT_DIR/.venv/bin/activate"

python -u check_imports.py
