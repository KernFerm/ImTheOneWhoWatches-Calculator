#!/usr/bin/env python3
"""
MathIt! - A command-line calculator that supports arithmetic, algebra, trigonometry, 
and other mathematical operations. Each operation's input and output is logged to answer.txt.
"""

import os
import math
import time
import sympy as sp
import colorama
from colorama import Fore, Style

# Initialize colorama with auto-reset
colorama.init(autoreset=True)

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to log results to answer.txt
def log_result(problem: str, result: str):
    with open("answer.txt", "a") as file:
        file.write(f"{problem} = {result}\n")

# Help information functions
def print_arithmetic_help():
    print("Arithmetic Operations 🧮:")
    print("1. Addition ➕: Adds two numbers.")
    print("2. Subtraction ➖: Subtracts one number from another.")
    print("3. Multiplication ✖️: Multiplies two numbers.")
    print("4. Division ➗: Divides one number by another.")
    print("5. Modulus 🔢: Returns the remainder of division.")
    print("6. Floor Division ⌊⌋: Returns the quotient (rounded down).")

def print_algebra_help():
    print("Algebraic Operations 📐:")
    print("1. Solve Linear Equation (ax + b = c) ➗: Solves linear equations.")
    print("2. Solve Quadratic Equation (ax^2 + bx + c = 0) 📊: Solves quadratic equations.")
    print("3. Solve Cubic Equation (ax^3 + bx^2 + cx + d = 0) 📈: Solves cubic equations.")
    print("4. Solve Exponential Equation (a^x = b) 🔥: Solves exponential equations.")
    print("5. Solve Logarithmic Equation (log_a(x) = b) 🔍: Solves logarithmic equations.")
    print("6. Y = MX + B ➡️: Calculates y for a given linear equation.")
    print("7. Simplify Algebraic Expression 🧩: Simplifies algebraic expressions.")

def print_trigonometry_help():
    print("Trigonometry Operations 📏:")
    print("1. Sine (sin) 🌟: Calculates the sine of an angle.")
    print("2. Cosine (cos) 🌟: Calculates the cosine of an angle.")
    print("3. Tangent (tan) 🌟: Calculates the tangent of an angle.")
    print("4. Inverse Sine (arcsin or asin) 🔄: Returns arcsine (in degrees) of a value in [-1,1].")
    print("5. Inverse Cosine (arccos or acos) 🔄: Returns arccosine (in degrees) of a value in [-1,1].")
    print("6. Inverse Tangent (arctan or atan) 🔄: Returns arctangent (in degrees) of a value.")
    print("7. Cosecant (csc) ❗: Calculates the cosecant of an angle.")
    print("8. Secant (sec) ❗: Calculates the secant of an angle.")
    print("9. Cotangent (cot) ❗: Calculates the cotangent of an angle.")

def print_mathematical_help():
    print("Mathematical Operations 🧮:")
    print("1. Square Root √: Calculates the square root of a number.")
    print("2. Power ^: Raises a number to a power.")

def print_banner():
    print(Fore.BLUE + """
 ______ __           ____               _       __  __          _       __          __           __
/_  __// /_   ___   / __ \  ____   ___ | |     / / / /_   ____ | |     / / ____ _  / /_  _____  / /_   ___    _____
 / /  / __ \ / _ \ / / / / / __ \ / _ \| | /| / / / __ \ / __ \| | /| / / / __ `/ / __/ / ___/ / __ \ / _ \  / ___/
 / /  / / / //  __// /_/ / / / / //  __/| |/ |/ / / / / // /_/ /| |/ |/ / / /_/ / / /_  / /__  / / / //  __/ (__  )
/_/  /_/ /_/ \___/ \____/ /_/ /_/ \___/ |__/|__/ /_/ /_/ \____/ |__/|__/  \__,_/  \__/  \___/ /_/ /_/ \___/ /____/
""" + Style.RESET_ALL)

def print_separator():
    print(Fore.GREEN + "=" * 120 + Style.RESET_ALL)

def input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print_error("Invalid input. Please enter a valid number.")

def print_error(message):
    print(Fore.RED + f"❌ Error: {message}" + Style.RESET_ALL)

# Arithmetic operations
def arithmetic_operations():
    while True:
        print_separator()
        print("Arithmetic Operations 🧮:")
        print("1. Addition ➕")
        print("2. Subtraction ➖")
        print("3. Multiplication ✖️")
        print("4. Division ➗")
        print("5. Modulus 🔢")
        print("6. Floor Division ⌊⌋")
        print("7. Clear Screen 🧹")
        print("8. Help ℹ️")
        print("9. Back to main menu ⬅️")

        operation = input("Enter your choice: ")

        if operation == "1":
            num1 = input_number("Enter first number: ")
            num2 = input_number("Enter second number: ")
            result = num1 + num2
            print(f"➕ {num1} + {num2} = {result} ✅")
            log_result(f"{num1} + {num2}", result)
        elif operation == "2":
            num1 = input_number("Enter first number: ")
            num2 = input_number("Enter second number: ")
            result = num1 - num2
            print(f"➖ {num1} - {num2} = {result} ✅")
            log_result(f"{num1} - {num2}", result)
        elif operation == "3":
            num1 = input_number("Enter first number: ")
            num2 = input_number("Enter second number: ")
            result = num1 * num2
            print(f"✖️ {num1} * {num2} = {result} ✅")
            log_result(f"{num1} * {num2}", result)
        elif operation == "4":
            num1 = input_number("Enter numerator: ")
            num2 = input_number("Enter denominator: ")
            if num2 != 0:
                result = num1 / num2
                print(f"➗ {num1} / {num2} = {result} ✅")
                log_result(f"{num1} / {num2}", result)
            else:
                print_error("Cannot divide by zero")
        elif operation == "5":
            num1 = input_number("Enter first number: ")
            num2 = input_number("Enter second number: ")
            result = num1 % num2
            print(f"🔢 {num1} % {num2} = {result} ✅")
            log_result(f"{num1} % {num2}", result)
        elif operation == "6":
            num1 = input_number("Enter numerator: ")
            num2 = input_number("Enter denominator: ")
            if num2 != 0:
                result = num1 // num2
                print(f"⌊ {num1} // {num2} = {result} ⌋")
                log_result(f"{num1} // {num2}", result)
            else:
                print_error("Cannot divide by zero")
        elif operation == "7":
            clear_screen()
            print_banner()
        elif operation == "8":
            print_arithmetic_help()
        elif operation == "9":
            break
        else:
            print_error("Invalid Entry")

        time.sleep(2)

# Algebraic operations
def algebra_operations():
    while True:
        print_separator()
        print("Algebraic Operations 📐:")
        print("1. Solve Linear Equation (ax + b = c)")
        print("2. Solve Quadratic Equation (ax^2 + bx + c = 0)")
        print("3. Solve Cubic Equation (ax^3 + bx^2 + cx + d = 0)")
        print("4. Solve Exponential Equation (a^x = b)")
        print("5. Solve Logarithmic Equation (log_a(x) = b)")
        print("6. Y = MX + B")
        print("7. Simplify Algebraic Expression 🧩")
        print("8. Clear Screen 🧹")
        print("9. Help ℹ️")
        print("10. Back to main menu ⬅️")

        operation = input("Enter your choice: ")

        if operation == "1":
            a = input_number("Enter the coefficient of x: ")
            b = input_number("Enter the constant term: ")
            c = input_number("Enter the constant on the right side: ")
            if a != 0:
                x = (c - b) / a
                print(f"📐 {a}x + {b} = {c}  ⟹  x = {x} ✅")
                log_result(f"Solve: {a}x + {b} = {c}", x)
            else:
                print_error("Coefficient 'a' cannot be zero.")
        elif operation == "2":
            a = input_number("Enter the coefficient of x^2 (a): ")
            b = input_number("Enter the coefficient of x (b): ")
            c = input_number("Enter the constant term (c): ")
            if a != 0:
                discriminant = b**2 - 4 * a * c
                if discriminant > 0:
                    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
                    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
                    print(f"📊 Roots: {root1} and {root2} ✅")
                    log_result(f"Solve: {a}x^2 + {b}x + {c} = 0", f"{root1}, {root2}")
                elif discriminant == 0:
                    root = -b / (2 * a)
                    print(f"📊 Single root: {root} ✅")
                    log_result(f"Solve: {a}x^2 + {b}x + {c} = 0", root)
                else:
                    real_part = -b / (2 * a)
                    imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
                    print(f"📊 Complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i ✅")
                    log_result(f"Solve: {a}x^2 + {b}x + {c} = 0", f"{real_part} + {imaginary_part}i, {real_part} - {imaginary_part}i")
            else:
                print_error("Coefficient 'a' cannot be zero for a quadratic equation.")
        elif operation == "3":
            a = input_number("Enter the coefficient of x^3 (a): ")
            if a == 0:
                print_error("Coefficient 'a' cannot be zero for a cubic equation.")
                continue
            b = input_number("Enter the coefficient of x^2 (b): ")
            c = input_number("Enter the coefficient of x (c): ")
            d = input_number("Enter the constant term (d): ")
            # Cardano's method for solving cubic equations
            p = c / a - (b**2) / (3 * a**2)
            q = d / a - (b * c) / (3 * a**2) + (2 * b**3) / (27 * a**3)
            delta = (q**2) / 4 + (p**3) / 27

            if delta > 0:
                u = (-q / 2 + math.sqrt(delta))**(1/3)
                v = (-q / 2 - math.sqrt(delta))**(1/3)
                root1 = u + v - b / (3 * a)
                print(f"📈 Real root: {root1} ✅")
                log_result(f"Solve: {a}x^3 + {b}x^2 + {c}x + {d} = 0", root1)
            elif delta == 0:
                if q >= 0:
                    root = -2 * (q / 2)**(1/3) - b / (3 * a)
                else:
                    root = 2 * abs(q / 2)**(1/3) - b / (3 * a)
                print(f"📈 Real root: {root} ✅")
                log_result(f"Solve: {a}x^3 + {b}x^2 + {c}x + {d} = 0", root)
            else:
                t = -q / 2
                phi = math.acos(t / math.sqrt(-p**3 / 27))
                root1 = 2 * math.sqrt(-p / 3) * math.cos(phi / 3) - b / (3 * a)
                root2 = 2 * math.sqrt(-p / 3) * math.cos((phi + 2 * math.pi) / 3) - b / (3 * a)
                root3 = 2 * math.sqrt(-p / 3) * math.cos((phi + 4 * math.pi) / 3) - b / (3 * a)
                print(f"📈 Real roots: {root1}, {root2}, {root3} ✅")
                log_result(f"Solve: {a}x^3 + {b}x^2 + {c}x + {d} = 0", f"{root1}, {root2}, {root3}")
        elif operation == "4":
            a = input_number("Enter the base (a): ")
            b_val = input_number("Enter the value (b): ")
            if a > 0 and a != 1:
                x = math.log(b_val) / math.log(a)
                print(f"🔥 {a}^x = {b_val}  ⟹  x = {x} ✅")
                log_result(f"Solve: {a}^x = {b_val}", x)
            else:
                print_error("Base 'a' must be positive and not equal to 1")
        elif operation == "5":
            a = input_number("Enter the base of the logarithm (a): ")
            b_exp = input_number("Enter the exponent (b): ")
            if a > 0 and a != 1:
                x = a ** b_exp
                print(f"🔍 log_{a}(x) = {b_exp}  ⟹  x = {x} ✅")
                log_result(f"Solve: log_{a}(x) = {b_exp}", x)
            else:
                print_error("Base 'a' must be positive and not equal to 1")
        elif operation == "6":
            m = input_number("Enter the slope (m): ")
            x_val = input_number("Enter the x-coordinate: ")
            b_val = input_number("Enter the y-intercept (b): ")
            y = m * x_val + b_val
            print(f"➡️ For y = {m}x + {b_val} at x = {x_val}, y = {y} ✅")
            log_result(f"Solve: y = {m}x + {b_val} for x = {x_val}", y)
        elif operation == "7":
            expression = input("Enter the algebraic expression: ")
            simplified_expression = sp.simplify(expression)
            print(f"🧩 Simplified: {simplified_expression} ✅")
            log_result(f"Simplify: {expression}", simplified_expression)
        elif operation == "8":
            clear_screen()
            print_banner()
        elif operation == "9":
            print_algebra_help()
        elif operation == "10":
            break
        else:
            print_error("Invalid Entry")

        time.sleep(2)

# Trigonometry operations
def trigonometry_operations():
    while True:
        print_separator()
        print("Trigonometry Operations 📏:")
        print("1. Sine (sin) 🌟")
        print("2. Cosine (cos) 🌟")
        print("3. Tangent (tan) 🌟")
        print("4. Inverse Sine (arcsin or asin) 🔄")
        print("5. Inverse Cosine (arccos or acos) 🔄")
        print("6. Inverse Tangent (arctan or atan) 🔄")
        print("7. Cosecant (csc) ❗")
        print("8. Secant (sec) ❗")
        print("9. Cotangent (cot) ❗")
        print("10. Help ℹ️")
        print("11. Back to main menu ⬅️")

        operation = input("Enter your choice: ")

        if operation in ["1", "2", "3", "7", "8", "9"]:
            angle = input_number("Enter the angle in degrees: ")
            angle_rad = math.radians(angle)
            if operation == "1":
                result = math.sin(angle_rad)
                print(f"🌟 sin({angle}°) = {result} ✅")
                log_result(f"sin({angle}°)", result)
            elif operation == "2":
                result = math.cos(angle_rad)
                print(f"🌟 cos({angle}°) = {result} ✅")
                log_result(f"cos({angle}°)", result)
            elif operation == "3":
                result = math.tan(angle_rad)
                print(f"🌟 tan({angle}°) = {result} ✅")
                log_result(f"tan({angle}°)", result)
            elif operation == "7":
                try:
                    result = 1 / math.sin(angle_rad)
                    print(f"❗ csc({angle}°) = {result} ✅")
                    log_result(f"csc({angle}°)", result)
                except ZeroDivisionError:
                    print_error("Cosecant is undefined for this angle.")
            elif operation == "8":
                try:
                    result = 1 / math.cos(angle_rad)
                    print(f"❗ sec({angle}°) = {result} ✅")
                    log_result(f"sec({angle}°)", result)
                except ZeroDivisionError:
                    print_error("Secant is undefined for this angle.")
            elif operation == "9":
                try:
                    result = 1 / math.tan(angle_rad)
                    print(f"❗ cot({angle}°) = {result} ✅")
                    log_result(f"cot({angle}°)", result)
                except ZeroDivisionError:
                    print_error("Cotangent is undefined for this angle.")
        elif operation in ["4", "5", "6"]:
            value = input_number("Enter a value (ensure it is in the valid domain): ")
            if operation == "4":
                try:
                    result_rad = math.asin(value)
                    result_deg = math.degrees(result_rad)
                    print(f"🔄 arcsin({value}) = {result_deg}° ✅")
                    log_result(f"arcsin({value})", f"{result_deg}°")
                except ValueError:
                    print_error("Invalid input for arcsin. Value must be between -1 and 1.")
            elif operation == "5":
                try:
                    result_rad = math.acos(value)
                    result_deg = math.degrees(result_rad)
                    print(f"🔄 arccos({value}) = {result_deg}° ✅")
                    log_result(f"arccos({value})", f"{result_deg}°")
                except ValueError:
                    print_error("Invalid input for arccos. Value must be between -1 and 1.")
            elif operation == "6":
                result_rad = math.atan(value)
                result_deg = math.degrees(result_rad)
                print(f"🔄 arctan({value}) = {result_deg}° ✅")
                log_result(f"arctan({value})", f"{result_deg}°")
        elif operation == "10":
            print_trigonometry_help()
        elif operation == "11":
            break
        else:
            print_error("Invalid Entry")

        time.sleep(2)

# Mathematical operations
def mathematical_operations():
    while True:
        print_separator()
        print("Mathematical Operations 🧮:")
        print("1. Square Root √")
        print("2. Power ^")
        print("3. Help ℹ️")
        print("4. Back to main menu ⬅️")

        operation = input("Enter your choice: ")

        if operation == "1":
            num = input_number("Enter a number: ")
            if num >= 0:
                result = math.sqrt(num)
                print(f"√({num}) = {result} ✅")
                log_result(f"√({num})", result)
            else:
                print_error("Cannot calculate the square root of a negative number.")
        elif operation == "2":
            base = input_number("Enter the base: ")
            exponent = input_number("Enter the exponent: ")
            result = base ** exponent
            print(f"{base} ^ {exponent} = {result} ✅")
            log_result(f"{base} ^ {exponent}", result)
        elif operation == "3":
            print_mathematical_help()
        elif operation == "4":
            break
        else:
            print_error("Invalid Entry")

        time.sleep(2)

def main():
    while True:
        clear_screen()
        print_banner()
        print("Welcome to MathIt! 🎉, by TheOneWhoWatches")
        print_separator()
        print("Select an operation: 🔢")
        print("1. Arithmetic Operations 🧮")
        print("2. Algebraic Operations 📐")
        print("3. Trigonometry Operations 📏")
        print("4. Mathematical Operations 🧮")
        print("5. Quit 🚪")

        choice = input("Enter your choice: ")

        if choice == "1":
            arithmetic_operations()
        elif choice == "2":
            algebra_operations()
        elif choice == "3":
            trigonometry_operations()
        elif choice == "4":
            mathematical_operations()
        elif choice == "5":
            print("Thank you for using MathIt! 😊 Goodbye! 🚪")
            time.sleep(2)
            break
        else:
            print_error("Invalid Entry")
        time.sleep(2)

if __name__ == "__main__":
    main()
