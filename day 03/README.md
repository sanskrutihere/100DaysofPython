<h1> Day 03 Overview <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Snake.png" alt="Snake" width="20" height="20" />
</h1>
Today, I explored `if-else` conditionals, modulo operator, logical operators, multiple if statements, nested if statements.

## 🐣 Project: [Treasure Island](https://github.com/sanskrutihere/100DaysofPython/blob/main/day%2003/treasure-island.py)
This project is a simple adventure game using conditionals that takes players on an exciting treasure hunt.

![Treasure Island GIF](https://github.com/sanskrutihere/100DaysofPython/blob/main/assets/gif/treasure-island.gif)

## Content:
- Key Concepts

1. [Basic if-else Statement](#basic-if-else-statement)
2. [Nested if-else Statements](#nested-if-else-statements)
3. [Multiple if Statements](#multiple-if-statements)
4. [if-elif-else Statement](#if-elif-else-statement)
5. [Logical Operators](#logical-operators)
6. [Modulo Operator %](#modulo-operator)

- Exercises

1. [BMI Calculator](#bmi-calculator)
2. [Rollercoaster Ride](#rollercoaster-ride)
3. [Python Pizza Order](#python-pizza-order)

---
## Key Concepts <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bookmark%20Tabs.png" alt="Bookmark Tabs" width="25" height="25" />

### 1. Basic `if-else` Statement
Syntax:
``` python
  if condition:
      # code to execute if condition is true
  else:
      # code to execute if condition is false
```
Example:
```python
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```
### 2. Nested `if-else` Statements
You can nest if-else statements within each other to create more complex decision structures.

Syntax:
```python
if condition1:
    if condition2:
        # code to execute if both condition1 and condition2 are true
    else:
        # code to execute if condition1 is true but condition2 is false
else:
    # code to execute if condition1 is false
```
Example:
```python
  age = 20
  if age >= 18:
      if age >= 21:
          print("You can drink alcohol.")
      else:
          print("You are an adult but cannot drink alcohol.")
  else:
      print("You are a minor.")
```
### 3. Multiple `if` Statements
Each if statement is independent. All the conditions are evaluated separately, and multiple blocks of code may be executed if multiple conditions are true.

Syntax:
```python
  if condition1:
      # code to execute if condition1 is true
  if condition2:
      # code to execute if condition2 is true
  if condition3:
      # code to execute if condition3 is true
```
Example:
```python
  num = 15
  if num > 10:
      print("The number is greater than 10.")  # This will be printed
  if num % 2 == 0:
      print("The number is even.")  # This will NOT be printed
  if num % 5 == 0:
      print("The number is divisible by 5.")  # This will be printed
```
Note: Unlike if-elif-else, each if block is checked independently.

### 4. `if-elif-else` Statement
This structure is used when there are multiple conditions to be checked, but only one block of code should be executed. The first if or elif block that is true gets executed, and the rest are skipped.

Syntax:
```python
  if condition1:
      # code to execute if condition1 is true
  elif condition2:
      # code to execute if condition1 is false and condition2 is true
  elif condition3:
      # code to execute if condition1 and condition2 are false and condition3 is true
  else:
      # code to execute if all the above conditions are false
```
Example:
```python
  year = int(input("Enter a year: "))
  
  if year % 400 == 0:
      print(f"{year} is a leap year.")
  elif year % 100 == 0:
      print(f"{year} is not a leap year.")
  elif year % 4 == 0:
      print(f"{year} is a leap year.")
  else:
      print(f"{year} is not a leap year.")
```
### 5. Logical Operators
Python has three logical operators: and, or, and not. These are used to combine multiple conditions.
- `and`: Both conditions must be True.
- `or`: At least one condition must be True.
- `not`: Negates a condition.

Example with `and`:

```python
  age = 20
  has_id = True
  
  if age >= 18 and has_id:
      print("You are allowed entry.")
  else:
      print("Entry denied.")
```
Example with `or`:

```python
  age = 16
  has_permission = True
  
  if age >= 18 or has_permission:
      print("You can enter the event.")
  else:
      print("You cannot enter.")
```
Example with `not`:

```python
  is_raining = False
  
  if not is_raining:
      print("You can go outside.")
  else:
      print("Stay indoors.")
```
### 6. Modulo Operator `%`
The modulo operator returns the remainder of division, which is often used to check divisibility.

Example:
```python
  number = int(input("Enter a number: "))
  if number % 2 == 0:
      print("Even")
  else:
      print("Odd")
```
---
## Exercises <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bookmark%20Tabs.png" alt="Bookmark Tabs" width="25" height="25" />
### 1. BMI Calculator
```python
  height = float(input("Enter height in meters: "))
  weight = float(input("Enter weight in kg: "))
  bmi = round(weight / (height ** 2), 2)
  
  if bmi < 18.5:
      print(f"Your BMI is {bmi}. You are underweight.")
  elif bmi < 25:
      print(f"Your BMI is {bmi}. You have a normal weight.")
  else:
      print(f"Your BMI is {bmi}. You are overweight.")
```
### 2. Rollercoaster Ride
```python
  height = int(input("What is your height in cms? : "))
  if height >= 120:
      age = int(input("How old are you? : "))
      bill = 0
      if age <= 12:
          bill += 5
      elif age < 18:
          bill += 7
      else:
          bill += 12
  
      photo = input("Do you want a photo? Y/N : ")
      if photo == "Y":
          bill += 3
      print(f"Your total bill is ${bill}.")
  else:
      print("Sorry, you cannot ride.")
```
### 3. Python Pizza Order:
```python
  size = input("Choose pizza size S, M, L: ")
  pepperoni = input("Do you want pepperoni? Y/N : ")
  cheese = input("Do you want extra cheese? Y/N : ")
  
  bill = 0
  if size == 'S':
      bill += 15
  elif size == 'M':
      bill += 20
  else:
      bill += 25
  
  if pepperoni == 'Y':
      if size == 'S':
          bill += 2
      else:
          bill += 3
  
  if cheese == 'Y':
      bill += 1
  
  print(f"Your total bill is ${bill}.")
```
