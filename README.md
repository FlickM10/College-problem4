# 🎯 Leibniz Series for Pi Calculation

# 📜 Overview

This Python script calculates the value of π (Pi) using the Leibniz formula for π (also known as the Madhava–Leibniz series). It allows the user to specify the number of terms (N) in the series to compute and then reports the calculated value, the number of terms used, and the accuracy compared to Python's built-in math.pi.

# 🔢 The Mathematical Formula

The script implements the following infinite series, which converges to π/4:

<img width="474" height="115" alt="image" src="https://github.com/user-attachments/assets/0d4b227a-066b-4d4d-8121-66706df7d3f8" />


Your script multiplies the entire summation by 4 to directly approximate π:

<img width="326" height="123" alt="image" src="https://github.com/user-attachments/assets/64e0def4-e445-43c2-960f-4da24b6be1b7" />


This calculation is performed iteratively within the for loop.

# 💻 Code Breakdown

    Variable,    Description
    
    N,    The user-defined number of terms to compute (controls the loop).
    y,    The running total of the series (the approximation of π).
    x,    "The loop index (the term number in the series, starting at 0)."
    y0,    The value of the current term in the series before being added to y.
    Accuracy,    The difference between the math.pi constant and the calculated value (y).


🚀 Getting Started

Prerequisites

You only need Python installed on your system. No external libraries are required beyond the built-in math module.

How to Run the Script

    Save the Code: Save the provided code as a file named calculate_pi.py.

    Open Terminal: Navigate to the directory where you saved the file.

    Execute: Run the script from your command line:
    Bash

    python calculate_pi.py

    Input: The script will prompt you to enter the number of repetitions (terms) to use in the series.


# Key Calculation

The core of the calculation is in the for loop: 

    y0 = 4 * (((-1) ** x) / ((2 * x) + 1))
    y = y0 + y

# ⚠️ Note on Convergence

The Leibniz series is known for its slow convergence. To achieve high accuracy (e.g., 6 decimal places), you would need to run the calculation for hundreds of thousands of terms. This script is excellent for demonstrating this convergence property.
