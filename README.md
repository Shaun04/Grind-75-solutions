# GRIND 75 problem solutions

This repository contains my take on the Grind 75 problem solutions.

## Table of Contents :bookmark_tabs:

1. [Two Sums](#two-sums)
2. [Valid Parentheses](#valid-parentheses)
3. [Best Time to Buy and Sell Stock](#best-time-to-buy-and-sell-stock)
4. [Valid Palindrome](#valid-palindrome)

## Solutions Used :bookmark_tabs:
### [Two Sums](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/twosums.py)
- Used a hashmap for this algorithm.
- Time Complexity is O(nlogn)

### [Valid Parentheses](https://github.com/Shaun04/Grind-75-solutions/blob/main/Stack/valid-parentheses.py)
- Open parentheses is pushed in the stack and when a closing parentheses appears it pops the opening parentheses in the stack.
- Time complexity is O(n)

### [Best Time to Buy and Sell Stock](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/besttimetobuyandsell.py)
- It uses two variables min and max_profit. It traverses the list when it finds the least number of profit it adds it in the min varaible.
- Time Complexity is O(n)

### [Valid Palindrome](https://github.com/Shaun04/Grind-75-solutions/blob/main/String/valid-palindrome.py)
- If the string contains alphanumeric characters then it is added to a new variable and then later it is checked if its a palindrome or not.
- Time Complexity is O(n)