# ➕➖➗ Calculator (Python)

A clean and extensible **command-line calculator** built using Python. Supports mathematical expressions, variables, basic functions, and easy extension—ideal for learning parsing, REPL interfaces, or quick CLI calculations.

---

## 📋 Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Requirements](#requirements)  
4. [Installation](#installation)  
5. [Usage Examples](#usage-examples)  
6. [Code Structure](#code-structure)  
7. [Extendability](#extendability)  
8. [Contributing](#contributing)  
9. [License](#license)

---

## 💡 Overview

This command-line calculator provides interactive evaluation of mathematical expressions, support for variables, and function definitions. It’s implemented with emphasis on modular design, clean parsing, and intuitive user experience—perfect for educational purposes or as a building block in larger tools.

---

## ✅ Features

- ✅ **Evaluate expressions**: `+, -, *, /, **`, parentheses  
- 🧮 Use **variables** (`x = 5`, `y = x * 2`)  
- 🛠️ Define **simple functions**: e.g. `def square(n): return n**2`  
- 🧵 Interactive **REPL loop**: Accepts assignments, expressions, and commands  
- 🗑️ **Session state persistence**: Variables/functions retained throughout session  
- 🔄 Easily **extendable parser** for new operators or functions

---

## 🧾 Requirements

- Python **3.7+**  
- No external dependencies—implemented with `ast`, `math`, and standard libraries

---

## ⚙️ Installation

```bash
git clone https://github.com/MisaghMomeniB/Calculator-Python.git
cd Calculator-Python
````

---

## 🚀 Usage Examples

Start the REPL:

```bash
python calculator.py
```

Example session:

```
> x = 10
> y = 3 * x + 5
> y
35
> def square(n): return n * n
> square(7)
49
> (x + y) / square(2)
9.0
> quit
```

---

## 📁 Code Structure

```
Calculator-Python/
├── calculator.py     # Main file with parser, evaluator, and REPL
└── README.md         # This file
```

* Uses the `ast` module for safe expression parsing
* Maintains a symbol table for variables/functions
* Handles errors like division by zero or syntax errors gracefully
* REPL supports built-in commands: `help`, `quit`, etc.

---

## ⚙️ Extendability

* 🌐 Add **math module functions** (`sin`, `cos`, `log`) via symbol table
* ➕ Extend parser with new operators or syntax
* 📦 Package as a module or CLI script with `argparse`
* 🔐 Add **sandbox restrictions** for secure execution

---

## 🤝 Contributing

Contributions are welcome! Ideas include:

* Add built-in **trigonometric functions** (`math.sin`, `math.cos`, etc.)
* Implement **persistent session** (save/load variables)
* Add **unit tests** (e.g., using `pytest`)
* Enhance REPL with **history navigation** (`readline`) or features

To contribute:

1. Fork the repository
2. Create a branch (`feature/...`)
3. Add tests & comments
4. Submit a detailed Pull Request

---

## 📄 License

Released under the **MIT License** — see `LICENSE` for details.
