<h1> Day 05 Overview <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Snake.png" alt="Snake" width="20" height="20" />
</h1>
Today, I learnt about For loops and the range() function.

## 🐣 Project: 
This project is a simple adventure game using conditionals that takes players on an exciting treasure hunt.

![Password Generator GIF](https://github.com/sanskrutihere/100DaysofPython/blob/main/assets/password-generator.gif)

## Content:
- Key Concepts

1. [For Loop](#for-Loop-in-python)
2. [For Loops with Range](#For-Loops-with-Range)

- Exercises

1. [Highest Score](#Highest-Score)
2. [sum of all the even numbers from 1 to 100](#Sum-of-all-the-even-numbers-from-1-to-100)
3. [Gauss Challenge](#The-Gauss-Challenge)
4. [FizzBuzz game](#FizzBuzz-Game)
5. [Average Height](#Average-Height)

---
## Key Concepts <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bookmark%20Tabs.png" alt="Bookmark Tabs" width="25" height="25" />

### 1. `for` Loop in Python
Loops allow us to repeat actions without manually coding each repetition. Instead of writing repetitive code, loops provide a way to automate actions, especially for tasks that require doing something multiple times, such as printing numbers or processing items in a list.

Syntax of a For Loop
```python
for <variable_name> in <a List>:
    <do something>
    <do something else>
```
`<variable_name>`: A placeholder that holds the value of the current item in the list as the loop iterates through it.
`<a List>`: This could be any iterable, such as a list or range.
Example:
```python
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
```
This will print each fruit and then print the fruit with " pie" added to it.

- **Indentation in Python Loops**
  
  Indentation is crucial in Python. After a colon (:), any following block of code should be properly indented to indicate it belongs to that loop or control structure.
  
  Example:
  ```python
  for fruit in fruits:
      print(fruit)
      print("Hello")
  ```
  This loop will print the fruit and then "Hello" for each fruit in the list.
  
  But if you move the print statement outside the loop:
  
  ```python
  Copy code
  for fruit in fruits:
      print(fruit)
  print("Hello")
  ```
  "Hello" will only be printed once after the loop finishes.

### 2. For Loops with Range
The range() function creates a sequence of numbers. When used with a for loop, you can iterate through a specific range of numbers.

Example:
```python
for number in range(1, 10):
    print(number)
```
This will print the numbers 1 to 9 (the upper bound is exclusive).

**Range Definition:** 

`a <= range(a, b) < b`, which means the range includes a but excludes b.

---
## Exercises <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bookmark%20Tabs.png" alt="Bookmark Tabs" width="25" height="25" />
### 1. Highest Score
```python
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score) #output: 199
```

### 2. Sum of all the even numbers from 1 to 100
You are going to write a program that calculates the sum of all the even numbers from 1 to 100, including 1 and 100.

e.g. 2 + 4 + 6 + 8 +10 ... + 98 + 100
```python
total = 0

for num in range(1,101):
    if num % 2 == 0:
        total += num

print(total)
```
### 3. The Gauss Challenge
To find the total of numbers between 1 and 100, you can use a loop combined with range().

Example:
```python
total = 0
for number in range(1, 101):
    total += number

print(total)  # Output: 5050
```
### 4. Fizzbuzz Game
```python
'''
You are going to write a program that automatically prints the solution to the FizzBuzz game.

Your program should print each number from 1 to 100 in turn.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".

`When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 

`And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`
'''

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    elif num % 3 != 0 and num % 5 == 0:
        print("Buzz")
    else:
        print(num)
```
### 5. Average Height
```python
student_heights = [180, 124, 165, 173, 189, 169, 146]

total_height = 0

for height in student_heights:
    total_height += height

print(f"Average height of students is {round(total_height/len(student_heights))}")
```
