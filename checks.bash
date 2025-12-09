#!/bin/bash
ruff check
ruff format
pylint year2025
python3 -m unittest discover year2025/tests
