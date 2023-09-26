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
12. [Sum Closest to Zero](#sum-closest-to-zero)
13. [Implement Queue Using Stacks](#implement-queue-using-stacks)
14. [Evaluate Reverse Polish Notation](#evaluate-reverse-polish-notation)
15. [Min Stack](#min-stack)
16. [Trapping Rain Water](#trapping-rain-water)
17. [Merge Two Sorted Linked List](#merge-two-sorted-linked-list)
18. [Linked List Cycle](#linked-list-cycle)
19. [Reverse Linked List](#reverse-linked-list)
20. [Middle of the Linked List](#middle-of-the-linked-list)
21. [Valid Anagram](#valid-anagram)
22. [Longest Palindrome](#longest-palindrome)

## Solutions Used :bookmark_tabs:
## Arrays
### [Two Sums](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/twosums.py)
- Used a hashmap for this algorithm.
- Time Complexity is O(nlogn)

### [Best Time to Buy and Sell Stock](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/besttimetobuyandsell.py)
- It uses two variables min and max_profit. It traverses the list when it finds the least number of profit it adds it in the min varaible.
- Time Complexity is O(n).

### [Majority Element](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/majority-element.py)
Solution 1 (Using Hashmap)
- In this solution we have used a Hashmap to store the values as well as the number of times they occur as a key value pair
- Time Complexity is O(n)

Solution 2 (Using Boyer Moore Algorithm)
- We initalise two varaibles res and count.
- We put the first number in res
- If we encounter the same variable we increment count and if we encounter a different number we decrement count.
- Once the count is 0 we change the number in res
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
- Space Complexity for two arrays is O(n) and using only one array is O(1)

### [Combination Sum](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/combination-sum.py)
- We use backtracking and recursion approach for this problem.
- If the total sum of the combination is greater than the target we backtrack to the previous element and try again.
- Time Complexity is O(2^n) where n is the target.

### [Container with most amount of water](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/container-with-most-water.py)
- We use the two pointer approach to solve this problem.
- We first intialise a max variable and we start the pointers from left and right. If left is less than the right we shift the left by one an vice versa.
- Time Complexity is O(n)

### [Sort Colors](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/sort-colors.py)
- We have used the three pointer approach. For this we need three pointers low,med,high.
- We swap low and med if med encounters a 0. And when med encounters a 1 we increment med by 1 and read the next.
- We swap var high and var med when var med encounters a 2.
- Time Complexity is O(n)

### [Sum Closest to Zero](https://github.com/Shaun04/Grind-75-solutions/blob/main/Array/sum-closest-to-zero.py)
- We first sort the list.
- Next we then use the two pointer method.
- We then add the two pointers that we come across.
- Time Complexity is O(nlogn) and Space Complexity is O(logn) -> For sorting

## Stacks
### [Valid Parentheses](https://github.com/Shaun04/Grind-75-solutions/blob/main/Stack/valid-parentheses.py)
- Open parentheses is pushed in the stack and when a closing parentheses appears it pops the opening parentheses in the stack.
- Time complexity is O(n)

### [Implement Queue Using Stacks](https://github.com/Shaun04/Grind-75-solutions/blob/main/Stack/implement-queue-using-stacks.py)
- Using queues to build a stack.
- Time Complexity is O(n)

### [Evaluate Reverse Polish Notation](https://github.com/Shaun04/Grind-75-solutions/blob/main/Stack/polish-notation.py)
- It uses a Stack
- If it encounters a int it pushes it to the stack
- Once it encounters a operand it fetched the last two numbers that are on the top of the stack and does the operation
- Then after the answer is obtained its pushed backed in the stack
- Time and Space Complexity is O(n)

### [Min Stack](https://github.com/Shaun04/Grind-75-solutions/blob/main/Stack/min-stack.py)
- We use two stacks in this method
- One stack will contain the elements and the other one will contain the minimum elements
- If popped operation is used then the element is removed from both the stacks
- Time Complexity is O(1)

### [Trapping Rain Water](https://github.com/Shaun04/Grind-75-solutions/blob/main/Stack/trapping-rain-water.py)
- We use the two pointer approach to solve this problem
- Time Complexity is O(n)

## Linked List
### [Merge two sorted list](https://github.com/Shaun04/Grind-75-solutions/blob/main/Linked-List/mergetwosortedlist.py)
- We use head and current variables to connect the linked list. A linked list consists of next and current variables.
- Time Complexity is O(n)

### [Linked List Cycle](https://github.com/Shaun04/Grind-75-solutions/blob/main/Linked-List/linkedlistcycle.py)
- Approach 1:
- We store the visited nodes in a hash set and when we again encounter the same node we return false.
- Time Complexity is O(n) and Space Complexity is O(n)
- Approach 2:
- We use two pointers one slow one fast. The slow one traverses one node at a time but the fast node traverses two nodes at one.
- Time Complexity is O(n) and Space Complexity is O(1)

### [Reverse Linked List](https://github.com/Shaun04/Grind-75-solutions/blob/main/Linked-List/reverselinkedlist.py)
- We go through each nodes in the linkedlist and then reverse it one by one till we reach the end.
- Two pointer approach is used for this. The two pointers are prev and curr
- We initalise previous as None and current as the first node of the Linked List.
- Time Complexity is O(n) and Space Complexity is O(1)

### [Middle of the Linked List](https://github.com/Shaun04/Grind-75-solutions/blob/main/Linked-List/middleofthelinkedlist.py)
- Approach 1:
- We use an array and store the nodes in that array.
- We then divide the length of the array into two parts.
- If the length of the array is even then we add 1 or its its odd we dont change anything.
- Time Complexity is O(n) and Space Complexity is O(n)
- Approach 2:
- We use two pointers one slow and one fast
- The slow pointer goes one ahead and the fast pointer goes two ahead
- Then we return the slow pointer
- Time Complexity is O(n) and Space Complexity is O(1)


## Strings
### [Valid Palindrome](https://github.com/Shaun04/Grind-75-solutions/blob/main/String/valid-palidrome.py)
- If the string contains alphanumeric characters then it is added to a new variable and then later it is checked if its a palindrome or not.
- Time Complexity is O(n).

### [Valid Anagram](https://github.com/Shaun04/Grind-75-solutions/blob/main/String/valid-anagram.py)
- Method 1: Using Hashmap
- We build two hashmap for both the strings with the key as the letter and value as the frequency when the character occurs.
- We then check if the elements are same.
- We can even use python built in datastructers called Counters.
- Time Complexity is O(n+m) and Space Complexity is O(n+m)

- Method 2: Using Sorting
- We sort both the list and then check if both the list match or not 
- Time Complexity is O(n+nlogn) and Space Complexity is O(1)

### [Longest Palindrome](https://github.com/Shaun04/Grind-75-solutions/blob/main/String/longest-palindrome.py)
- First we get the frequency of each character that occurs in the string.
- This whole logic is based on the odd frequency. If a odd frequency occurs that element can only occur once in the palindrome.
- Approach 1: Using set
- We add the odd elements in the set and then at the end we use the logic len(string) - len(set) + 1
Appraoch 2: Using Dictonary
- In this we build a dictonary of the frequency of the elements.
- Then we go through the dictonary and if we encounter a odd number we increment the odd count else we decrement the odd count.
- The logic len(string) - len(set) + 1 applies here too
- Time Complexity and Space Complexity of both the approaches are O(n) and O(n) respectively.