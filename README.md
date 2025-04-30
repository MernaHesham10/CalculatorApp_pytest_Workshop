# 🧮 CalculatorApp_pytest_Workshop

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Pytest](https://img.shields.io/badge/pytest-passing-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A robust calculator application with comprehensive unit tests using `pytest` for learning modern Python testing techniques.

---

## 📋 Table of Contents
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Testing Features](#-testing-features)
- [Running Tests](#-running-tests)
- [Debugging](#-debugging)
- [License](#-license)

---

## ✨ Features
- **Pure Python implementation** (OOP principles)
- **Complete test coverage** (100% coverage target)
- **Modern testing techniques**:
  - Fixtures
  - Parametrization
  - Mocking
  - Parallel execution

---

## 🛠️ Prerequisites
- Python 3.8+
- Git
- VS Code (recommended)

---

## 🚀 Quick Start

### 1. Clone & Setup
```bash
git clone https://github.com/your-username/calculator-project.git
cd calculator-project
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 2. Install Dependencies
```bash
pip install -e .
pip install pytest pytest-mock pytest-xdist pytest-cov
```

### 3. Run Tests
```bash
pytest -v  # Basic test run
pytest --cov=calculator --cov-report=html  # Coverage report
```

---

## 🏗️ Project Structure

```
calculator-app/
├── calculator/
│   ├── __init__.py
│   └── calculator.py        # Core Calculator class
├── tests/
│   ├── __init__.py
│   ├── test_basic.py        # Core functionality
│   ├── test_exceptions.py   # Error cases
│   ├── test_fixtures.py     # Fixture examples
│   ├── test_mocking.py      # Mocking examples
│   └── ...                 # Other test types
└── README.md
```

---

## 🔧 Testing Features

### 🧪 Core Testing Capabilities
| Feature               | Implementation Example                  | Command               |
|-----------------------|----------------------------------------|-----------------------|
| Simple Assertions     | `assert calc.add(2,2) == 4`            | `pytest tests/`       |
| Fixtures              | `@pytest.fixture def calc():`          | N/A                   |
| Parametrization       | `@pytest.mark.parametrize()`           | N/A                   |
| Exception Testing     | `with pytest.raises(ValueError):`      | N/A                   |

### 🚀 Advanced Features
| Feature               | Implementation Example                  | Command               |
|-----------------------|----------------------------------------|-----------------------|
| Parallel Execution    | `@pytest.mark.parallel`                | `pytest -n 4`        |
| Coverage Reporting    | N/A                                    | `pytest --cov`       |
| Mocking              | `mocker.patch()`                       | N/A                   |
---

## 🧪 Running Tests

### Basic Test Suite
```bash
pytest -v
```

### With Coverage Reporting
```bash
pytest --cov=calculator --cov-report=html
```

### Parallel Execution
```bash
pytest -n 4  # 4 parallel workers
```

---

## 🐞 Debugging in VS Code
1. Set breakpoints in test files
2. Press `F5` or use Run/Debug panel
3. Select test configuration
4. View variables in debug console

---

## 💡 Learning Resources
- [Pytest Documentation](https://docs.pytest.org/)
- [Python Testing with pytest](https://pythontest.com/pytest-book/)
