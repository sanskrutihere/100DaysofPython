<h1> Day 04 Overview <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Snake.png" alt="Snake" width="20" height="20" />
</h1>
Today, I explored Random Module, the Offset, Lists, Index Errors, Nested Lists

## 🐣 Project: [Rock Paper Scissors](https://github.com/sanskrutihere/100DaysofPython/blob/main/day%2004/rock_paper_scissor.py) 
This project is a simple adventure game using conditionals that takes players on an exciting treasure hunt.

![Rock Paper Scissors GIF](https://github.com/sanskrutihere/100DaysofPython/blob/main/assets/rock%3Dpaper-scissors.gif)

## Content:
- Key Concepts

- [Random Module](#random-module-in-python)
- [Lists](#lists)

- Exercises

1. [Flip a Coin](#Flip-a-Coin)
2. [Banker Roulette: Random Name Selection](#Banker-Roulette)

---
## Key Concepts <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bookmark%20Tabs.png" alt="Bookmark Tabs" width="25" height="25" />

### 1. Pseudorandom Number Generators (PRNG)
Computers are deterministic machines, making true randomness impossible. Hence, pseudorandom number generators (PRNG) are used, such as the Mersenne Twister algorithm.

### 2. Random Module in Python
Python offers the random module for generating random numbers. Full documentation: [Random Module Docs.](https://docs.python.org/3/library/random.html)
- Generating Random Whole Numbers
  To generate a random whole number within a range:
  ```python
  import random`
  rand_num = random.randint(1, 10)  # Returns a random integer between 1 and 10 (inclusive).
  ```
- Generating Random Floating-Point Numbers:
  `random.random()` generates a random float between 0 (inclusive) and 1 (exclusive):
  ```python
  rand_num_0_to_1 = random.random()  # Output: 0.0 <= rand_num_0_to_1 < 1.0
  ```
- Multiply `random.random()` to get numbers in any range:

  ```python
  random.random() * 5  # Output: 0 <= number < 5
  ```
- `random.uniform()` generates a random float between any two given numbers:
  
  ```python
  random_float = random.uniform(1, 10)  # Output: 1 <= number <= 10
  ```
  
### 3. Lists

[Lists](https://docs.python.org/3/tutorial/datastructures.html) in Python are versatile data structures that allow you to store a collection of items. They can hold mixed types (integers, strings, objects, etc.) and are mutable, meaning you can change their content.

1. Creation:
   
   A list is created by placing items inside square brackets [], separated by commas.
   ```python
    fruits = ["Apple", "Banana", "Cherry"]
   ```
3. Indexing:
   
   Lists are zero-indexed, meaning the first item is at index 0.
    ```python
    print(fruits[0])  # Output: Apple
    ```
4. Negative Indexing:
   
   You can access elements from the end of the list using negative indices.
   ```python
    print(fruits[-1])  # Output: Cherry
   ```
5. Slicing:
   
    You can retrieve a subset of a list using slicing.
    ```python
    print(fruits[0:2])  # Output: ['Apple', 'Banana']
    ```
5. Modification:
   
    Lists are mutable, so you can change, add, or remove items.
    ```python
    fruits[1] = "Blueberry"  # Change "Banana" to "Blueberry"
    ```
6. Adding Items:
   
    You can add items using `append(), insert(), extend()`.
    ```python
    fruits.append("Dragonfruit")  # Adds to the end
    fruits.insert(1, "Blackberry")  # Inserts at index 1
    fruits.extend(["Mango", "Banana"]) #multiple items inserted
    ```
7. Removing Items:
   
    Remove items using `remove(), pop(), or del`.
    ```python
    fruits.remove("Apple")  # Removes the first occurrence of "Apple"
    popped_fruit = fruits.pop()  # Removes the last item and returns it
    del fruits[0]  # Deletes the first item
    ```
8. Length:
   
    Get the number of items in a list using len().
    ```python
    print(len(fruits))  # Output: Number of items in the list
    ```
9. Membership:
  
    Check if an item exists in a list using the in keyword.
    ```python
    if "Cherry" in fruits:
        print("Cherry is in the list.")
    ```
10. Nested Lists:
  
    You can have lists inside other lists (2D lists).
    ```python
    nested_list = [["Apple", "Banana"], ["Carrot", "Spinach"]]
    ```
---
## Exercises <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bookmark%20Tabs.png" alt="Bookmark Tabs" width="25" height="25" />
### 1. Flip a Coin
  Simple coin flip using `random.randint():`
  ```python
  import random
  if random.randint(0, 1) == 0:
      print("Heads")
  else:
      print("Tails")
  ```

### 2.  Banker Roulette
  Pick a random name from a list:
  ```python
  import random
  friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
  print(random.choice(friends))
  ```
