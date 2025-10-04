# Logic Box
_A menu-driven Python console app that practices core programming concepts: loops, `range()`, control statements, and nested loops._

![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![Status](https://img.shields.io/badge/status-MVP-green)

## ✨ Overview
**Logic Box** implements two learning modules:

1. **Pattern Generator** – builds text patterns using nested loops (e.g., a right-angled triangle) based on user input.
2. **Number Analyzer** – iterates through a user-defined range using `range()` and reports:
   - whether each number is **odd or even**
   - the **sum of all numbers** in the range

The project intentionally showcases `for` and `while` loops, `range()`, and control flow with `break`, `continue`, and `pass`, wrapped in a simple **menu-driven interface**.

---

## 📚 Learning Objectives
- Practice **control structures** (`if/elif/else`) and **loops** (`for`, `while`)
- Use **`range()`** to generate sequences
- Apply **`break`**, **`continue`**, and **`pass`** appropriately
- Implement **nested loops** for pattern building
- Add **input validation** and basic **error handling**
- Structure a small but complete **console program**

---

## 🧩 Features
- Welcome screen with instructions
- Menu options:
  1. Generate a Pattern (right-angled triangle)
  2. Analyze a Range of Numbers (odd/even + total sum)
  3. Exit
- Validates inputs (positive row counts; end ≥ start)
- Demonstrates `break`, `continue`, and `pass` in context
- Clear error messages and exit message

---
## 🛠️ Installation & Run

**Prerequisites:** Python 3.9+ (works on 3.8+, but tested on 3.9+)

```bash
# 1) Clone the repo
git clone https://github.com/<your-username>/logic-box.git
cd logic-box

# 2) Run
python logic_box.py

