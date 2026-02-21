# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A simple Python calculator project. The main logic lives in `calculator.py` and tests are in `test_calculator.py`.

## Commands

Run tests:
```bash
python -m pytest test_calculator.py
```

Run a single test by name:
```bash
python -m pytest test_calculator.py::test_function_name
```

Run the calculator directly:
```bash
python calculator.py
```

## Code Preferences

- Commentaar en docstrings in het Nederlands
- Altijd type hints gebruiken bij functies
- Docstrings verplicht bij elke functie
- Variabelenamen in het Engels
- Geen hardcoded waarden, gebruik constanten of parameters