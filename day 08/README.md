<h1> Day 08 Overview <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Snake.png" alt="Snake" width="20" height="20" />
</h1>
Today, I learnt about Function Parameters & Caesar Cipher.

## 🐣 Project: [Caeser Cipher](https://github.com/sanskrutihere/100DaysofPython/blob/main/day%2008/main.py)
This project is a simple encryption and decryption program based on caesar cipher algorithm.

![Caeser Cipher](https://github.com/sanskrutihere/100DaysofPython/blob/main/assets/gif/ceasercipher.gif)

## Contents:
- Key Concepts

1. Functions with inputs
2. Positinal vs Keyword Arguments
3. Caeser Cipher

- Exercises

1. Love Calculator
2. Life in Weeks

---
## Key Concepts <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bookmark%20Tabs.png" alt="Bookmark Tabs" width="25" height="25" />

### 1.  Functions with Inputs

**a) Function Parameters and Arguments:**
A function can take inputs, known as parameters, which allow you to pass data into the function. When calling the function, the values provided are known as arguments.

Example:
```python
# Function with parameters
def add(a, b):
    return a + b

# Call the function with arguments
result = add(3, 5)
print(result)  # Output: 8
```
In the above example, a and b are parameters, and when we call add(3, 5), the values 3 and 5 are passed as arguments.

**b) Multiple Parameters:**
Functions can have multiple parameters. The number of arguments passed must match the number of parameters, unless default values are provided.

Example:
```python
# Function with multiple parameters
def greet(name, message="Welcome!"):
    print(f"{message}, {name}!")

# Call the function with one or two arguments
greet("Alice")          # Output: Welcome!, Alice!
greet("Bob", "Hello")   # Output: Hello, Bob!
```
In this case, message has a default value, so it’s optional when calling the function.

### 2. Positional vs. Keyword Arguments

**a) Positional Arguments:**
When you call a function, positional arguments are assigned based on the order in which they are passed to the function. The first argument is assigned to the first parameter, the second to the second, and so on.

Example:
```python
def subtract(a, b):
    return a - b

# Positional arguments: 10 is assigned to 'a' and 5 to 'b'
result = subtract(10, 5)
print(result)  # Output: 5
```
Here, the position of the arguments matters. If you change their order, the result will change.

**b) Keyword Arguments:**
With keyword arguments, you specify the name of the parameter when passing the argument, so the order does not matter.

Example:
```python
# Using keyword arguments
result = subtract(b=5, a=10)  # Same result as positional
print(result)  # Output: 5
```
In this case, you explicitly assign a=10 and b=5, so the order doesn’t affect the result.

**c) Mixing Positional and Keyword Arguments:**
You can mix positional and keyword arguments when calling a function, but positional arguments must come first.

Example:
```python
def introduce(name, age, city="Unknown"):
    print(f"Name: {name}, Age: {age}, City: {city}")

# Mixing positional and keyword arguments
introduce("Alice", age=25)         # Output: Name: Alice, Age: 25, City: Unknown
introduce(name="Bob", age=30, city="NYC")  # Output: Name: Bob, Age: 30, City: NYC
```

**d) Default Parameter Values:**
In the example above, city has a default value, meaning you can call the function without providing that argument, and it will use the default.

### 3. Caeser Cipher
The Caesar Cipher is one of the oldest and simplest encryption techniques. It is a type of substitution cipher where each letter in the plaintext is shifted by a certain number of positions in the alphabet. It was famously used by Julius Caesar to send secret messages.

**Components of Caesar Cipher:**

- Encryption (Encoding):
  To encrypt a message, each letter in the original message (plaintext) is replaced by a letter a fixed number of positions down the alphabet.
  The number of positions to shift by is known as the shift amount.
  Example:
  For a shift of 3, the letter 'A' becomes 'D', 'B' becomes 'E', and so on.

- Decryption (Decoding):
  To decrypt a message, you reverse the process by shifting the letters back by the same amount.
  If the cipher shifts letters forward by a given number, the decryption will shift them backward by the same number.
  
- Shift Amount:
  The shift can be any number, but since there are only 26 letters in the English alphabet, a shift of 26 would return the original message. Therefore, the shift amount is typically taken modulo 26 (shift % 26).

- Wrap-around:
  When shifting letters at the end of the alphabet (like 'X', 'Y', 'Z'), the cipher wraps around to the beginning ('A', 'B', 'C').

**Example of Caesar Cipher:**
Encryption:
```python
Plaintext: hello
Shift: 3
Ciphertext: khoor
```
The letter 'h' is shifted by 3 positions to 'k', 'e' becomes 'h', and so on.

Decryption:
```python
Ciphertext: khoor
Shift: 3 (reverse shift by -3)
Plaintext: hello
```
---
## Exercises <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bookmark%20Tabs.png" alt="Bookmark Tabs" width="25" height="25" />
### 1. Love Calculator
You can call this function with any two names to check their love score.
```python
def calculate_love_score(name1, name2):
    # Combine both names into one string and convert to lowercase
    combined_names = (name1 + name2).lower()
    
    # Check for the occurrences of the letters in "TRUE"
    true_count = 0
    for letter in "true":
        true_count += combined_names.count(letter)
    
    # Check for the occurrences of the letters in "LOVE"
    love_count = 0
    for letter in "love":
        love_count += combined_names.count(letter)
    
    # Combine both counts to form a two-digit number
    love_score = int(str(true_count) + str(love_count))
    
    # Print the love score
    print(f"Love Score = {love_score}")

# Call your function with hard-coded values
calculate_love_score("Kanye West", "Kim Kardashian") #OUTPUT: Love Score = 42
```

### 2. Life in Weeks
You can call this function with different ages to check how many weeks are left until age 90.
```python
def life_in_weeks(age):
    # Constants for the number of years to live and time units
    total_years = 90
    weeks_in_year = 52
    
    # Calculate the remaining time in weeks
    remaining_years = total_years - age
    remaining_weeks = remaining_years * weeks_in_year
    
    # Output the result using an f-string
    print(f"You have {remaining_weeks} weeks left.")

# Call your function with a hard-coded value
life_in_weeks(56) #Output: You have 1768 weeks left.
```
