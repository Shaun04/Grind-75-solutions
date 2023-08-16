# GRIND 75 problem solutions

This repository contains my take on the Grind 75 problem solutions.

## Table of Contents :bookmark_tabs:

1. [Two Sums](#two-sums)
2. [Valid Parentheses](#valid-parentheses)
3. [Best Time to Buy and Sell Stock](#best-time-to-buy-and-sell-stock)
4. [Valid Palindrome](#valid-palindrome)
5. [Majority Element](#majority-element)

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

### [Valid Palindrome](https://github.com/Shaun04/Grind-75-solutions/blob/main/String/valid-palidrome.py)
- If the string contains alphanumeric characters then it is added to a new variable and then later it is checked if its a palindrome or not.
- Time Complexity is O(n)
<<<<<<< HEAD

### [Majority Element](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/majority-element.py)
- Solution 1 (Using Hashmap)
- In this solution we have used a Hashmap to store the values as well as the number of times they occur as a key value pair
- Time Complexity is O(n)
- Solution 2 (Using Boyer Moore Algorithn)
- We initalise two varaibles res and count. If we encounter the same variable we increment count and if we encounter a different number we decrement count.
- Once the res is 0 we change the number
- Time Complexity is O(1)
=======
>>>>>>> 15271c8178ec09eb6b6ad3671e0715ebd37f9e55
