<h1> Day 02 Overview <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Snake.png" alt="Snake" width="20" height="20" />
</h1>
<p> 
  Today, I learnt about several fundamental programming concepts including <strong>Primitive Datatypes, Numbers, Operations, Type Conversion and f-strings.</strong>
</p>

## 🐣 Project: [Tip-Calculator](https://github.com/sanskrutihere/100DaysofPython/blob/main/day%2002/tip-calculator.py) 
This project is a **Tip Calculator** that calculates the total bill (including tip) and splits it among a specified number of people. 

![Day 2 GIF](https://github.com/sanskrutihere/100DaysofPython/blob/main/assets/gif/tip-calculator.gif)
## Key Concepts <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bookmark%20Tabs.png" alt="Bookmark Tabs" width="25" height="25" />

#### 1. Datatypes
Python supports different datatypes, some primitive data types include: `int`, `float`, `string`,`bool`.
Example:
```python
# String and subscripting
message = "Hello, World!"
first_char = message[0]  # Subscript to access the first character
print(first_char)  # Output: H
last_char = message[-1]  # Subscript to access the last character
print(last_char)  # Output: ! (note: space is also character)

# Integer: whole numbers, can be positive or negative
age = 25
print(age)  # Output: 25

# Float: decimal point numbers
height = 1.75
print(height)  # Output: 1.75

# Boolean: True or False
is_student = True
print(is_student)  # Output: True

# Large integer example
large_number = 123_456_789
print(large_number)  # Output: 123_456_789
```

#### 2. Type Error
A `TypeError` in Python occurs when an operation or function is applied to an object of an inappropriate type.

- Example: 1 Trying to find the length of an integer, which is not allowed
  ```python
      number = 123456
      print(len(number))  # Raises TypeError: object of type 'int' has no len()
  ```
  solution:
  ```python
      number = 123456
      print(len(str(number)))  # Output: 6
  ```
- Example: 2 Attempt to add a string and an integer
  ```python
    x = "hello"
    y = 5
    result = x + y  # Raises TypeError: can only concatenate str (not "int") to str
  ```

#### 3. Type Checking
Checking the type of an object to ensure it’s valid for an operation.
  ```python
        x = 10         # Integer
        y = "Hello"    # String
        z = True       # Boolean
        a = 3.14       # Float
        
        print(type(x))  # Output: <class 'int'>
        print(type(y))  # Output: <class 'str'>
        print(type(z))  # Output: <class 'bool'>
        print(type(a))  # Output: <class 'float'>
  ```

#### 4. Type Conversion
 Type conversion refers to converting a variable from one data type to another. 
 
 - Implicit: done automatically by Python.
   Example:
   ```python
   x = 10   # int
   y = 3.5  # float
   result = x + y  # Python automatically converts x to float, result is 13.5 (float)
   ```
   
 - Explicit: done by the programmer manually using Type Casting.
   - int(): Converts data into an integer.
     Example:
     ```python
           x = "10"
           y = 3.14
           print(int(x))  # Output: 10
           print(int(y))  # Output: 3
     ```
      
   - float(): Converts data into a floating-point number.
     Example:
      ```python
            x = "5"
            y = 10
            print(float(x))  # Output: 5.0
            print(float(y))  # Output: 10.0
      ```
      
   - str(): Converts data into a string.
     Example:
     ```python
            x = 100
            y = 3.14
            print(str(x))  # Output: "100"
            print(str(y))  # Output: "3.14"
     ```
   - bool(): Converts data into a boolean (`True` or `False`).
     Example:
     ```python
            x = 0
            y = "Hello"
            print(bool(x))  # Output: False
            print(bool(y))  # Output: True
     ```
   - Not all conversions are possible. For example, trying to convert a string like "abc" into an integer using int("abc") will raise a ValueError.
   - You may lose data during conversion, like when converting a float to an integer (int(3.7) will result in 3).

#### 5. Operators
- Arithmetic Operators:
  Perform basic mathematical operations like addition, subtraction, multiplication, and division.
  Assume x = 10, y = 3
  | Operator | Description         | Example              | Output   |
  |----------|---------------------|----------------------|----------|
  | `+`      | Addition            | `print(x + y)`       | `13`     |
  | `-`      | Subtraction         | `print(x - y)`       | `7`      |
  | `*`      | Multiplication      | `print(x * y)`       | `30`     |
  | `/`      | Division            | `print(x / y)`       | `3.33`   |
  | `%`      | Modulus (Remainder) | `print(x % y)`       | `1`      |
  | `**`     | Exponentiation      | `print(x ** y)`      | `1000`   |
  | `//`     | Floor Division      | `print(x // y)`      | `3`      |

- Assignment Operators:
  Perform operations and then assign the result to the variable.
  | Operator | Description                | Example                    | Output   |
  |----------|----------------------------|----------------------------|----------|
  | `=`      | Assign value               | `x = 5`                    | `5`      |
  | `+=`     | Add and assign             | `x += 3` (x = x + 3)       | `8`      |
  | `-=`     | Subtract and assign        | `x -= 2` (x = x - 2)       | `6`      |
  | `*=`     | Multiply and assign        | `x *= 4` (x = x * 4)       | `24`     |
  | `/=`     | Divide and assign          | `x /= 2` (x = x / 2)       | `12.0`   |
  | `%=`     | Modulus and assign         | `x %= 5` (x = x % 5)       | `2.0`    |
  | `//=`    | Floor divide and assign    | `x //= 1` (x = x // 1)     | `2.0`    |
  | `**=`    | Exponentiate and assign    | `x **= 3` (x = x ** 3)     | `8.0`    |

#### 6. f- String
f-strings are formatted string literals in Python that allow you to embed expressions and variables directly within string literals for easier and more readable string formatting.
- Example: 1
  ```python
    name = "Alice"
    age = 30
    height = 1.75
    
    # Using f-string to format the output
    print(f"My name is {name}, I am {age} years old and {height} meters tall.")
    
    #Output: My name is Alice, I am 30 years old and 1.75 meters tall.
  ```
- Example: 2
  ```python
    a = 5
    b = 10
  
    # Using an expression inside an f-string
    result = f"The sum of {a} and {b} is {a + b}."
    print(result)
  ```
## Exercises <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bookmark%20Tabs.png" alt="Bookmark Tabs" width="25" height="25" />
1. BMI Calculator:
   ```python
    # Given values
    height = 1.65  # in meters
    weight = 84    # in kilograms
    
    # Calculate BMI
    bmi = weight / (height ** 2)
    
    # Print the result
    print(bmi)   #Output: 30.799999999999997
   ```
2. Number Manipulation:
    
     ```python
     print(bmi)             # Output: 30.799999999999997
     print(int(bmi))        # Output: 30 (floor value)
     print(round(bmi))      # Output: 31
     print(round(bmi, 2))   # Output: 30.80
     ```
   
