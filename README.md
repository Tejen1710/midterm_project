# Advanced Calculator (Midterm Project)

## Overview
The Advanced Calculator is a command-line interface (CLI) application designed for performing a wide range of mathematical operations. Built with a focus on design patterns, the project incorporates the Factory, Memento, and Observer patterns to ensure scalability and maintainability. It also features robust logging, history management with undo/redo functionality, and CSV-based persistence. The project is thoroughly tested with over 90% test coverage and integrates Continuous Integration (CI) using GitHub Actions.

---

## Features
- **Mathematical Operations**: Supports addition, subtraction, multiplication, division, power, root, modulus, integer division, percentage, and absolute difference.
- **History Management**: Tracks calculation history with undo and redo capabilities.
- **Persistence**: Save and load history using CSV files.
- **Design Patterns**: Implements Factory, Memento, and Observer patterns.
- **Logging**: Comprehensive logging for debugging and auditing.
- **Test Coverage**: Over 90% test coverage with `pytest`.
- **CI/CD**: Automated testing and deployment using GitHub Actions.

---

## Prerequisites
- Python 3.8 or higher
- `pip` (Python package manager)
- Git (optional, for contributing)

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Tejen1710/midterm_project.git
   cd midterm_project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   ```

5. Run the application:
   ```bash
   python -m app.repl
   ```

---

## Usage
### Commands
- Perform operations:
  ```
  add|subtract|multiply|divide|power|root|modulus|int_divide|percent|abs_diff a b
  ```
- Manage history:
  ```
  history | clear | undo | redo | save | load
  ```
- Get help or exit:
  ```
  help | exit
  ```

### Example
```bash
> add 5 3
Result: 8
> history
1. add 5 3 = 8
> undo
Undo successful.
> redo
Redo successful.
```

---

## Testing
Run the following command to execute tests and check coverage:
```bash
pytest --cov=app --cov-report=term-missing --cov-fail-under=90
```

---

## Continuous Integration
The project uses GitHub Actions for CI. The workflow file is located at `.github/workflows/python-app.yml`. It runs tests automatically on every push or pull request to the `main` branch.

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch.
4. Open a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
