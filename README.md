
# Advanced Calculator (Midterm)

Design-pattern-driven CLI calculator with Factory, Memento, Observer; logging, history with undo/redo, CSV persistence, tests (≥90% coverage), and CI via GitHub Actions.

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python -m app.repl
```

## Commands
`add|subtract|multiply|divide|power|root|modulus|int_divide|percent|abs_diff a b`  
`history | clear | undo | redo | save | load | help | exit`

## Tests
```bash
pytest --cov=app --cov-report=term-missing --cov-fail-under=90
```

## CI
See `.github/workflows/python-app.yml`. Runs tests on push/PR to `main`.
