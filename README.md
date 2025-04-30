```markdown
# 🧮 Python Calculator with Pytest Testing

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Pytest](https://img.shields.io/badge/pytest-passing-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A robust calculator application built in Python, with comprehensive unit tests using `pytest`. Ideal for learning:
- **Python OOP** (Calculator class)
- **Unit testing** (pytest fixtures, assertions)
- **VS Code integration** (debugging, test discovery)

---

## 🛠️ Prerequisites
- Python 3.8+
- Git (for cloning)
- VS Code (recommended)

---

# 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/calculator-project.git
cd calculator-project
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install pytest
```

```bash
python.exe -m pip install --upgrade pip
```

### 4. Run the Calculator
```bash
python calculator.py
```

```bash
pip install pytest pytest-mock pytest-xdist pytest-cov
```

### 5. Execute Tests
```bash
pytest -v  # Verbose mode for detailed output
```

---

# 🏗️ Project Structure (Fixed Version)

```
calculator-app/
├── calculator/               # Python package
│   ├── __init__.py          # Exposes Calculator class
│   └── calculator.py        # Main implementation
├── tests/                   # All test files
│   ├── __init__.py          # Makes tests a package
│   ├── test_basic.py        # Simple syntax tests
│   ├── test_coverage.py     # Edge case tests
│   ├── test_exceptions.py   # Error handling
│   ├── test_fixtures.py     # Fixture demonstrations
│   ├── test_mocking.py      # Mocking tests (fixed)
│   ├── test_parallel.py     # Parallel execution
│   ├── test_parametrized.py # Data-driven tests (fixed)
│   └── test_skipping.py     # Skipped tests
└── README.md                # Project documentation
```

---

# 🧪 Testing with Pytest
Tests verify all calculator operations, including edge cases (e.g., division by zero).

### Example Test Output:
```bash
========================= test session starts =========================
collected 5 items

test_calculator.py::test_add PASSED                             [ 20%]
test_calculator.py::test_subtract PASSED                        [ 40%]
test_calculator.py::test_multiply PASSED                        [ 60%]
test_calculator.py::test_divide PASSED                          [ 80%]
test_calculator.py::test_divide_by_zero PASSED                  [100%]

========================== 5 passed in 0.02s ==========================
```

### 🐞 Debugging in VS Code
1. Set breakpoints in `test_calculator.py`.
2. Press `F5` or use the **Run and Debug** panel.
3. Select **Python: Current File**.
---

### **📌 pytest Feature Summary**

| **Feature**               | **Description**                                                                 | **Example**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **Simple Syntax**         | No boilerplate - tests are plain functions                                       | `def test_add(): assert 1+1 == 2`                                           |
| **Fixtures**              | Reusable setup/teardown with `@pytest.fixture`                                  | ```python<br>@pytest.fixture<br>def db():<br>    yield connection<br>```    |
| **Parametrization**       | Run tests with multiple inputs via `@pytest.mark.parametrize`                   | ```python<br>@pytest.mark.parametrize("a,b,expected", [(1,2,3)])<br>```    |
| **Exception Testing**     | Verify errors with `pytest.raises()`                                            | ```python<br>with pytest.raises(ValueError):<br>    divide(1, 0)<br>```    |
| **Mocking**              | Patch objects using `pytest-mock` plugin                                        | ```python<br>mocker.patch("module.func", return_value=5)<br>```             |
| **Markers**              | Tag tests (skip, xfail, custom)                                                | ```python<br>@pytest.mark.skip(reason="WIP")<br>```                         |
| **Parallel Execution**    | Run tests in parallel with `pytest-xdist`                                       | `pytest -n 4` (4 workers)                                                  |
| **Test Coverage**         | Measure coverage with `pytest-cov`                                              | `pytest --cov=my_module`                                                   |                      |