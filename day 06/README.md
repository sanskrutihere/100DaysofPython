<h1> Day 06 Overview <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Snake.png" alt="Snake" width="20" height="20" />
</h1>
Today, I learnt about functions, built in functions, while loop and indentation in python

## 🐣 Project: 
This project is 2D Maze Escape Game that uses functions in Reeborg's world.

![Escape Maze](https://github.com/sanskrutihere/100DaysofPython/blob/main/assets/gif/maze.gif)

## Content:
- Key Concepts

1. [functions](#functions-in-Python)
2. [Indentation](#Indentation)
3. [While Loop](#While-Loop)
---
## Key Concepts <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bookmark%20Tabs.png" alt="Bookmark Tabs" width="25" height="25" />

### 1. functions in Python
**a) Defining and Calling Functions**
A function is defined using the def keyword, followed by the function name and parentheses. Parameters can be passed inside the parentheses.

```python
# Define a function
def greet(name):
    return f"Hello, {name}!"

# Call the function
print(greet("Alice"))
```

**b) Built-in Functions**
Python provides several built-in functions that can be used without needing to define them. For example, print(), len(), sum(), etc.

```python
# Example of built-in functions
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # Output: 5
print(sum(numbers))  # Output: 15
```
### 2. Indentation
Python uses indentation to define the structure of code blocks, instead of curly braces {} like in C++ or Java. It is typically 4 spaces or a tab.

Example:

```python
def check_positive(num):
    if num > 0:
        print(f"{num} is positive.")
    elif num == 0:
        print(f"{num} is zero.")
    else:
        print(f"{num} is negative.")

# Call the function
check_positive(3)
check_positive(0)
check_positive(-5)
```
Here, the body of the if, elif, and else blocks are defined by their indentation. Python will raise an error if indentation is inconsistent.

### 3. While Loop
A while loop repeats as long as a certain condition is True.

Example:

```python
# While loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1
```
The condition is checked before each iteration, and the loop stops once the condition becomes False.
