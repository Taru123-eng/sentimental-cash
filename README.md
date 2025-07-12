# Sentimental Cash (Python)

A simple Python program that calculates the minimum number of coins needed to give a user change. The logic works by converting a given dollar amount into cents and then using the U.S. coin denominations (25¢, 10¢, 5¢, 1¢) to compute the smallest number of coins required.

Unlike the typical iterative solutions, this version uses a **recursive approach** for a more algorithmically expressive solution.

##  How It Works

- The user is prompted to enter a positive float value representing change owed (e.g., 0.67).
- This amount is converted into cents.
- A recursive function is used to:
  - Find the largest coin that fits into the remaining amount.
  - Subtract that coin's value and repeat the process with the new remainder.
  - Continue until the amount is reduced to zero.

##  Key Concepts

- Recursion
- Input validation
- Rounding and floating-point handling
- Greedy algorithm for coin change

##  Sample Run

```bash
Change: 0.67
6
