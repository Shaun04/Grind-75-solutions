# GRIND 75 problem solutions

This repository contains my take on the Grind 75 problem solutions.

## Table of Contents :bookmark_tabs:

1. [Two Sums](#two-sums)
2. [Valid Parentheses](#valid-parentheses)
3. [Best Time to Buy and Sell Stock](#best-time-to-buy-and-sell-stock)
4. [Valid Palindrome](#valid-palindrome)
5. [Majority Element](#majority-element)
6. [Insert Interval](#insert-interval)
7. [Three Sums](#three-sums)
8. [Product Except Self](#product-except-self)
9. [Combination Sum](#combination-sum)
10. [Container with most amount of water](#container-with-most-amount-of-water)
11. [Sort Colors](#sort-colors)

## Solutions Used :bookmark_tabs:
## Arrays
### [Two Sums](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/twosums.py)
- Used a hashmap for this algorithm.
- Time Complexity is O(nlogn)


### [Best Time to Buy and Sell Stock](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/besttimetobuyandsell.py)
- It uses two variables min and max_profit. It traverses the list when it finds the least number of profit it adds it in the min varaible.
- Time Complexity is O(n)

### [Valid Palindrome](https://github.com/Shaun04/Grind-75-solutions/blob/main/String/valid-palidrome.py)
- If the string contains alphanumeric characters then it is added to a new variable and then later it is checked if its a palindrome or not.
- Time Complexity is O(n)

### [Majority Element](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/majority-element.py)
Solution 1 (Using Hashmap)
- In this solution we have used a Hashmap to store the values as well as the number of times they occur as a key value pair
- Time Complexity is O(n)

Solution 2 (Using Boyer Moore Algorithm)
- We initalise two varaibles res and count. If we encounter the same variable we increment count and if we encounter a different number we decrement count.
- Once the res is 0 we change the number
- Time Complexity is O(1)

### [Duplicate Element](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/duplicate-element.py)
Solution 1 (Using Hashmap)
- In this solution we have used a Hashmap to store the values when we encounter a number from the list first we check if it exists in the hashmapm, if it doesnt exist in the hashmap we add that element otherwise we return True.
- Time Complexity is O(n)

Solution 2 (Using Sets)
- Sets in python can only store distinct elements so we convert the list into a set and then check if the length of the set is equal to the length of the list. If both are equal we can be certain there are no duplicate elements.
- Time Complexity is O(n)

### [Insert Interval](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/insert-interval.py)
- First we check if the newInterval is in the beginning or end of the already exisitng interval. If it is we directly add it to the list.
- If the newInterval is in the middle of the array we merge the overlapping element.
- Time Complexity is O(n)

### [Three Sums](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/three-sums.py)
- First we sort the list then we take the first number of the list and use the two pointer approach to find the second and third number.
- If the first, second and third number equates to zero we add it to a set.
- We use a set so that it eliminates the duplicate answers
- Time Complexity is O(n^2)

### [Product Except Self](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/productexceptself.py)
- We use two methods, both the methods are similar but one uses 2 arrays and the other one uses only 1 array.
- Find the prefix product and the postfix product of the input array and then multiply the prefix and postfix together.
- Time Complexity is O(n)
- Space Complexity for two arrays is O(n) and for using only one array is O(1)

### [Combination Sum](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/combination-sum.py)
- We use backtracking and recursion approach for this problem.
- If the total sum of the combination is greater than the target we backtrack to the previous element and try again.
- Time Complexity is O(2^n) where n is the target.

### [Container with most amount of water](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/container-with-most-water.py)
- We use the two pointer approach to solve this problem.
- We first intialise a max variable and we start the pointers from left and right. If left is less than the right we shift the left by one an vice versa.
- Time Complexity is O(n)

### [Sort Colors](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/sort-colots.py)
- We have used the three pointer approach. For this we need three pointers low,med,high.
- We swap low and med if med encounters a 0. And when med encounters a 1 we increment med by 1 and read the next.
- We swap high and med is med encounters a 2.
- Time Complexity is O(n)

## Stacks
### [Valid Parentheses](https://github.com/Shaun04/Grind-75-solutions/blob/main/Stack/valid-parentheses.py)
- Open parentheses is pushed in the stack and when a closing parentheses appears it pops the opening parentheses in the stack.
- Time complexity is O(n)