#Employee Salary & Tax Calculator

A simple Python mini-project that calculates an employee's salary after adding a bonus and deducting tax. It also determines the employee's salary bracket based on the final salary.

##Features

- Takes employee salary as input
- Takes bonus percentage
- Calculates salary including bonus
- Takes tax percentage
- Calculates salary after tax
- Determines the employee's salary bracket
- Uses multiple functions to organize the program

##Concepts Used

- Variables
- User input
- Data types
- Arithmetic operators
- Functions
- Parameters and arguments
- Return values
- Passing values between functions
- `if, elif, and else
- Function calling

# 💰 Employee Salary & Tax Calculator

A simple Python mini-project that calculates an employee's salary after adding a bonus and deducting tax. It also determines the employee's salary bracket based on the final salary.

## 📌 Features

- Takes employee salary as input
- Takes bonus percentage
- Calculates salary including bonus
- Takes tax percentage
- Calculates salary after tax
- Determines the employee's salary bracket
- Uses multiple functions to organize the program

## 🧠 Concepts Used

- Variables
- User input
- Data types
- Arithmetic operators
- Functions
- Parameters and arguments
- Return values
- Passing values between functions
- `if`, `elif`, and `else`
- Function calling

##How It Works

The program follows this process:

Enter Salary
     ↓
Enter Bonus %
     ↓
calculate_bonus()
     ↓
Salary + Bonus
     ↓
tax()
     ↓
Salary After Tax
     ↓
check_salary()
     ↓
Salary Bracket


1. Calculate Bonus

The bonus is calculated using:

Bonus = Salary × Bonus Percentage / 100

Then:

Salary with Bonus = Salary + Bonus

2. Calculate Tax

Tax is calculated using:

Tax = Salary with Bonus × Tax Percentage / 100

Then:

Final Salary = Salary with Bonus - Tax

3. Check Salary Bracket

The final salary is classified into three brackets:

Final Salary >= 100000
→ Highest Salary Bracket

Final Salary >= 50000
→ Middle Salary Bracket

Otherwise
→ Lowest Salary Bracket


Example
Input
Enter your salary: 60000
Enter your bonus percentage: 10
Enter tax percentage: 5

Output
Your total before tax with bonus is: 66000.0
Your total after tax with bonus is: 62700.0
You are in the middle salary bracket


How to Run
Open the project in VS Code.
Make sure Python is installed.
Open the terminal.
Run: python file name.py
Enter the requested salary, bonus percentage, and tax percentage.

Future Improvements
Possible improvements for future versions:

+Add employee name
+Add multiple employees
+Add different tax slabs
+Generate a salary report
+Store employee data in a file
+Add input validation
+Improve output formatting


Learning Purpose: This project was created to practice Python functions and understand how values can be returned from one function and passed into another function.


Author: Gyaneshwar Giri Aka Sangam Aka Lorem



