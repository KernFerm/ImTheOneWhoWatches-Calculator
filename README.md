# MathIt!

MathIt! is an engaging command-line calculator that supports a wide range of mathematical operations—including arithmetic, algebra, trigonometry, and other advanced calculations. All inputs and outputs are logged to an `answer.txt` file for easy reference. The interface is enhanced with emojis and colored output using [Colorama](https://pypi.org/project/colorama/), while [Sympy](https://www.sympy.org/) is used to simplify algebraic expressions.

# I made it better for him he had issues
[https://github.com/ImTheOneWhoWatches/Calculator](https://github.com/ImTheOneWhoWatches/Calculator)

## Features

- **Arithmetic Operations**  
  ➕ Addition, ➖ Subtraction, ✖️ Multiplication, ➗ Division, 🔢 Modulus, and ⌊⌋ Floor Division.

- **Algebraic Operations**  
  📐 Solve linear, quadratic, and cubic equations.  
  🔥 Solve exponential equations and 🔍 logarithmic equations.  
  🧩 Simplify algebraic expressions using Sympy.

- **Trigonometry Operations**  
  🌟 Calculate sine, cosine, tangent and their inverses (with results in degrees).  
  ❗ Compute cosecant, secant, and cotangent.

- **Mathematical Operations**  
  🧮 Calculate square roots and powers.

- **Logging**  
  Every calculation (both the problem and its result) is automatically appended to `answer.txt`.

## Dependencies

- **Python 3.x**
- [**Sympy**](https://www.sympy.org/) (>=1.8) – for symbolic mathematics and expression simplification.
- [**Colorama**](https://pypi.org/project/colorama/) (>=0.4.4) – for colored terminal output and a more engaging interface.

## Installation

Navigate to the Project Directory:

```
cd forkedfromImTheOneWhoWatches-Calculator
```

Install the Required Dependencies:
```
pip install -r requirements.txt
```

## Usage
Run the calculator script using Python:
```
python calculator.py
```
- Follow the interactive on-screen menus to perform various mathematical operations. The script uses clear instructions and fun emojis to guide you through your calculations.

## File Structure
- `calculator.py` – The main Python script for MathIt!
- `requirements.txt` – Contains the list of required packages.
- `answer.txt` – Log file where each calculation's problem and answer are recorded.
- `readme.md` – This file.

## Acknowledgments
MathIt! was created to deliver a fun, interactive, and efficient command-line calculator experience. Enjoy using it and feel free to contribute!
