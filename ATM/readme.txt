# 🏧 ATM Withdrawal System

A simple Python mini-project that simulates an ATM withdrawal system.

The program allows a user to enter a withdrawal amount and checks whether the transaction is valid based on the available account balance.

---

## 📌 Features

- Displays the current account balance
- Takes the withdrawal amount from the user
- Checks for invalid withdrawal amounts
- Checks for insufficient balance
- Calculates the remaining balance after a successful withdrawal
- Uses functions for withdrawal validation
- Uses conditional statements to handle different situations

---

## 🧠 Concepts Used

This project uses the following Python concepts:

- Variables
- User Input
- if / elif / else
- Functions
- Parameters
- Arguments
- `return`
- Comparison Operators
- Logical Operators


## How It Works

The program starts with a balance of:
1000

The user enters a withdrawal amount.


The program then checks:

If the withdrawal amount is 0 or less → Invalid withdrawal amount
If the withdrawal amount is greater than the balance → Insufficient balance
Otherwise → Calculate and display the remaining balance

Example Output
Successful Withdrawal
Enter amount to withdraw: 300

Your balance is: 1000
Your withdrawal amount is: 300

Remaining balance after withdrawal is: 700
Insufficient Balance
Enter amount to withdraw: 1500

Your balance is: 1000
Your withdrawal amount is: 1500

Insufficient balance
Invalid Withdrawal Amount
Enter amount to withdraw: -100

Your balance is: 1000
Your withdrawal amount is: -100

Invalid withdrawal amount
Project Structure
ATM-Withdrawal-System/
│
├── main.py
└── README.md

Future Improvements

Possible improvements for future versions:

Allow multiple withdrawals
Add deposit functionality
Add PIN authentication
Store account balance using files
Create multiple user accounts
Add transaction history
Use Object-Oriented Programming (OOP)

Author: Gyaneshwar Giri Aka Sangam