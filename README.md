# Python Syntax Cheat Sheet
---
## 1. VARIABLES & ASSIGNMENT
### Basic Assignment
```python
x = 5
name = "John"
price = 99.99
is_valid = True

# Multiple assignment
a, b, c = 1, 2, 3
x = y = z = 0

# Swap variables
a, b = b, a

# Unpacking
first, *middle, last = [1, 2, 3, 4, 5]  # first=1, middle=[2,3,4], last=5
```

### Augmented Assignment
```python
x += 5      # x = x + 5
x -= 3      # x = x - 3
x *= 2      # x = x * 2
x /= 4      # x = x / 4
x //= 2     # x = x // 2 (floor division)
x %= 3      # x = x % 3 (modulo)
x **= 2     # x = x ** 2 (power)
```

### Walrus Operator (Assignment in Expression)
```python
# Assign and use in one line (Python 3.8+)
if (n := len(my_list)) > 10:
    print(f"List is too long ({n} elements)")

# In while loop
while (line := file.readline()) != "":
    process(line)
```

---

## 2. LOOPS

### For Loop
```python
# Basic for loop
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 10):      # 1 to 9
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 (step by 2)
    print(i)

# Loop through list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Loop with index
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Loop with index starting at 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# Loop through dictionary
prices = {'apple': 1.20, 'banana': 0.80}
for key, value in prices.items():
    print(f"{key}: ${value}")

# Loop through keys only
for key in prices.keys():
    print(key)

# Loop through values only
for value in prices.values():
    print(value)

# Reverse loop
for i in reversed(range(5)):
    print(i)  # 4, 3, 2, 1, 0

# Loop through two lists simultaneously
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

### While Loop
```python
# Basic while
count = 0
while count < 5:
    print(count)
    count += 1

# While with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
    print(f"You entered: {user_input}")

# While with continue
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip even numbers
    print(count)
```

### Loop Control
```python
# Break - exit loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4

# Continue - skip to next iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Prints 1, 3, 5, 7, 9

# Else clause (runs if loop completes without break)
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed normally")  # This will print
```

---

## 3. CONDITIONALS

### If/Elif/Else
```python
# Basic if
if x > 0:
    print("Positive")

# If-else
if x > 0:
    print("Positive")
else:
    print("Non-positive")

# If-elif-else
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# Inline if (ternary)
result = "Positive" if x > 0 else "Non-positive"
status = "adult" if age >= 18 else "minor"

# Multiple conditions
if x > 0 and y > 0:
    print("Both positive")

if x > 0 or y > 0:
    print("At least one positive")

if not is_empty:
    print("Not empty")

# Check membership
if 'apple' in fruits:
    print("Found apple")

if x not in [1, 2, 3]:
    print("x is not 1, 2, or 3")

# Check None
if variable is None:
    print("Variable is None")

if variable is not None:
    print("Variable has a value")

# Check empty
if not my_list:  # Empty list = False
    print("List is empty")

if my_string:    # Non-empty string = True
    print("String has content")
```

---

## 4. COMPREHENSIONS

### List Comprehension
```python
# Basic
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# With if-else
labels = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
# ['even', 'odd', 'even', 'odd', 'even']

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
# [1, 2, 3, 4, 5, 6]
```

### Dictionary Comprehension
```python
# Basic
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# From two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(keys, values)}
# {'a': 1, 'b': 2, 'c': 3}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Swap keys and values
original = {'a': 1, 'b': 2}
swapped = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b'}
```

### Set Comprehension
```python
# Basic
unique_evens = {x for x in [1, 2, 2, 3, 4, 4, 5] if x % 2 == 0}
# {2, 4}
```

### Generator Expression
```python
# Like list comprehension but lazy (memory efficient)
gen = (x**2 for x in range(10))

# Use in functions
sum_of_squares = sum(x**2 for x in range(10))

# Convert to list if needed
squares_list = list(gen)
```

---

## 5. FUNCTIONS

### Basic Functions
```python
# Simple function
def greet():
    print("Hello!")

greet()

# With parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# With return
def add(a, b):
    return a + b

result = add(3, 5)

# Multiple return values
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

min_val, max_val, avg = get_stats([1, 2, 3, 4, 5])

# Default arguments
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Uses default
greet("Bob", "Hi")         # Overrides default

# Keyword arguments
def describe_pet(animal, name, age=None):
    print(f"{name} is a {animal}")
    if age:
        print(f"Age: {age}")

describe_pet(animal="dog", name="Buddy", age=3)
describe_pet(name="Whiskers", animal="cat")  # Order doesn't matter

# *args - variable number of positional arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10

# **kwargs - variable number of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")
```

### Lambda Functions
```python
# Basic lambda
square = lambda x: x**2
print(square(5))  # 25

# Multiple arguments
add = lambda x, y: x + y
print(add(3, 5))  # 8

# Use with map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# Use with filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]

# Use with sorted
students = [('Alice', 25), ('Bob', 20), ('Charlie', 30)]
sorted_by_age = sorted(students, key=lambda x: x[1])
# [('Bob', 20), ('Alice', 25), ('Charlie', 30)]
```

---

## 6. DATA STRUCTURES

### Lists
```python
# Create
my_list = [1, 2, 3, 4, 5]
empty_list = []
mixed = [1, "hello", 3.14, True]

# Access
first = my_list[0]        # 1
last = my_list[-1]        # 5
slice = my_list[1:3]      # [2, 3]
slice = my_list[:3]       # [1, 2, 3]
slice = my_list[2:]       # [3, 4, 5]
slice = my_list[::2]      # [1, 3, 5] (every 2nd element)
reversed = my_list[::-1]  # [5, 4, 3, 2, 1]

# Modify
my_list[0] = 10           # Change first element
my_list.append(6)         # Add to end
my_list.insert(0, 0)      # Insert at position
my_list.extend([7, 8])    # Add multiple
my_list.remove(3)         # Remove first occurrence
popped = my_list.pop()    # Remove and return last
popped = my_list.pop(0)   # Remove and return at index
my_list.clear()           # Remove all

# Operations
length = len(my_list)
count = my_list.count(2)  # Count occurrences
index = my_list.index(3)  # Find index
my_list.sort()            # Sort in place
my_list.reverse()         # Reverse in place
sorted_list = sorted(my_list)  # Return sorted copy

# Check membership
if 3 in my_list:
    print("Found")

# Copy
shallow_copy = my_list.copy()
also_shallow = my_list[:]
```

### Tuples (Immutable)
```python
# Create
my_tuple = (1, 2, 3)
single = (1,)             # Note the comma
empty = ()

# Access (same as lists)
first = my_tuple[0]
slice = my_tuple[1:3]

# Unpack
a, b, c = my_tuple
first, *rest = my_tuple

# Named tuples (more readable)
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
```

### Dictionaries
```python
# Create
my_dict = {'name': 'Alice', 'age': 30}
empty_dict = {}
also_dict = dict(name='Bob', age=25)

# Access
name = my_dict['name']              # Raises KeyError if not found
age = my_dict.get('age')            # Returns None if not found
age = my_dict.get('age', 0)         # Returns 0 if not found

# Modify
my_dict['city'] = 'NYC'             # Add new key
my_dict['age'] = 31                 # Update existing
my_dict.update({'country': 'USA'})  # Add multiple
del my_dict['city']                 # Remove key
popped = my_dict.pop('age')         # Remove and return
my_dict.clear()                     # Remove all

# Operations
length = len(my_dict)
keys = my_dict.keys()               # dict_keys(['name', 'age'])
values = my_dict.values()           # dict_values(['Alice', 30])
items = my_dict.items()             # dict_items([('name', 'Alice'), ...])

# Check membership
if 'name' in my_dict:
    print("Key exists")

# Default values
counts = {}
for letter in 'hello':
    counts[letter] = counts.get(letter, 0) + 1

# Or use defaultdict
from collections import defaultdict
counts = defaultdict(int)
for letter in 'hello':
    counts[letter] += 1
```

### Sets (Unique, Unordered)
```python
# Create
my_set = {1, 2, 3, 4, 5}
empty_set = set()                   # NOT {} (that's a dict)
from_list = set([1, 2, 2, 3, 3])   # {1, 2, 3}

# Operations
my_set.add(6)                       # Add element
my_set.remove(3)                    # Remove (raises error if not found)
my_set.discard(3)                   # Remove (no error if not found)
my_set.clear()                      # Remove all

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b                       # {1, 2, 3, 4, 5, 6}
intersection = a & b                # {3, 4}
difference = a - b                  # {1, 2}
symmetric_diff = a ^ b              # {1, 2, 5, 6}

# Check membership
if 3 in my_set:
    print("Found")
```

---

## 7. STRING OPERATIONS

### String Methods
```python
s = "Hello World"

# Case
s.upper()                # "HELLO WORLD"
s.lower()                # "hello world"
s.capitalize()           # "Hello world"
s.title()                # "Hello World"
s.swapcase()             # "hELLO wORLD"

# Check
s.startswith("Hello")    # True
s.endswith("World")      # True
s.isalpha()              # False (has space)
s.isdigit()              # False
s.isalnum()              # False
s.isspace()              # False
"   ".isspace()          # True

# Find/Replace
s.find("World")          # 6 (index)
s.index("World")         # 6 (raises error if not found)
s.count("l")             # 3
s.replace("World", "Python")  # "Hello Python"

# Split/Join
words = s.split()        # ['Hello', 'World']
words = s.split(",")     # Split by comma
joined = "-".join(words) # "Hello-World"

# Trim
"  hello  ".strip()      # "hello"
"  hello  ".lstrip()     # "hello  "
"  hello  ".rstrip()     # "  hello"

# Format
name = "Alice"
age = 30
f"Hello, {name}! You are {age} years old."
"Hello, {}! You are {} years old.".format(name, age)
"Hello, {0}! You are {1} years old.".format(name, age)
"Hello, {name}! You are {age} years old.".format(name=name, age=age)

# Multi-line
multi = """
This is a
multi-line
string
"""

# Raw strings (no escape)
path = r"C:\Users\name\file.txt"
```

---

## 8. FILE OPERATIONS

### Reading Files
```python
# Method 1: with statement (recommended)
with open('file.txt', 'r') as f:
    content = f.read()              # Read entire file
    # File automatically closed

with open('file.txt', 'r') as f:
    line = f.readline()             # Read one line

with open('file.txt', 'r') as f:
    lines = f.readlines()           # Read all lines as list

with open('file.txt', 'r') as f:
    for line in f:                  # Read line by line (memory efficient)
        print(line.strip())

# Method 2: traditional (need manual close)
f = open('file.txt', 'r')
content = f.read()
f.close()
```

### Writing Files
```python
# Write (overwrites)
with open('file.txt', 'w') as f:
    f.write("Hello\n")
    f.write("World\n")

# Append
with open('file.txt', 'a') as f:
    f.write("New line\n")

# Write multiple lines
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('file.txt', 'w') as f:
    f.writelines(lines)
```

### File Modes
```python
'r'  # Read (default)
'w'  # Write (overwrites)
'a'  # Append
'r+' # Read and write
'b'  # Binary mode ('rb', 'wb')
```

---

## 9. EXCEPTION HANDLING

```python
# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    value = int(input("Enter number: "))
    result = 10 / value
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Catch all exceptions
try:
    risky_operation()
except Exception as e:
    print(f"Error: {e}")

# Else clause (runs if no exception)
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print(f"Result: {result}")

# Finally clause (always runs)
try:
    f = open('file.txt')
    # do something
except IOError:
    print("File error")
finally:
    f.close()  # Always closes file

# Raise exceptions
if age < 0:
    raise ValueError("Age cannot be negative")

# Custom exceptions
class CustomError(Exception):
    pass

raise CustomError("Something went wrong")
```

---

## 10. USEFUL BUILT-IN FUNCTIONS

```python
# Type conversion
int("123")           # 123
float("3.14")        # 3.14
str(123)             # "123"
bool(0)              # False
bool(1)              # True
list((1, 2, 3))      # [1, 2, 3]
tuple([1, 2, 3])     # (1, 2, 3)
set([1, 2, 2, 3])    # {1, 2, 3}

# Math
abs(-5)              # 5
pow(2, 3)            # 8 (2^3)
round(3.7)           # 4
round(3.14159, 2)    # 3.14
min(1, 2, 3)         # 1
max(1, 2, 3)         # 3
sum([1, 2, 3])       # 6

# Sequences
len([1, 2, 3])       # 3
sorted([3, 1, 2])    # [1, 2, 3]
reversed([1, 2, 3])  # reversed object (use list() to see)
enumerate(['a', 'b', 'c'])  # [(0, 'a'), (1, 'b'), (2, 'c')]
zip([1, 2], ['a', 'b'])     # [(1, 'a'), (2, 'b')]

# Filters
all([True, True, False])    # False (all must be True)
any([False, False, True])   # True (at least one True)
filter(lambda x: x > 0, [-1, 0, 1, 2])  # [1, 2]
map(lambda x: x**2, [1, 2, 3])          # [1, 4, 9]

# Type checking
type(123)            # <class 'int'>
isinstance(123, int) # True

# Object info
dir(my_object)       # List all attributes/methods
help(function)       # Show documentation
```

---

## 11. COMMON PATTERNS

### Checking if Variable Exists
```python
# Check if defined
if 'variable_name' in locals():
    print("Variable exists locally")

if 'variable_name' in globals():
    print("Variable exists globally")

# Or use try-except
try:
    my_variable
except NameError:
    my_variable = default_value
```

### Default Values
```python
# Dictionary default
value = my_dict.get('key', 'default')

# Or with setdefault
value = my_dict.setdefault('key', 'default')  # Also sets it

# Function argument default
def function(arg=None):
    if arg is None:
        arg = []  # Don't use [] as default in signature!
```

### Swapping
```python
# Swap two variables
a, b = b, a

# Rotate values
a, b, c = b, c, a
```

### Finding Min/Max with Key
```python
students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78}
]

# Find student with highest score
best = max(students, key=lambda x: x['score'])
worst = min(students, key=lambda x: x['score'])
```

### Flatten Nested Lists
```python
nested = [[1, 2], [3, 4], [5, 6]]

# Method 1: List comprehension
flat = [item for sublist in nested for item in sublist]

# Method 2: itertools
from itertools import chain
flat = list(chain(*nested))

# Method 3: sum (for small lists only)
flat = sum(nested, [])
```

### Remove Duplicates While Preserving Order
```python
# Using dict (Python 3.7+)
items = [1, 2, 2, 3, 3, 4]
unique = list(dict.fromkeys(items))

# Using seen set
def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
```

### Counting Items
```python
from collections import Counter

items = ['a', 'b', 'a', 'c', 'b', 'a']
counts = Counter(items)
# Counter({'a': 3, 'b': 2, 'c': 1})

most_common = counts.most_common(2)  # [('a', 3), ('b', 2)]
```

### Grouping Items
```python
from itertools import groupby

data = [
    {'type': 'fruit', 'name': 'apple'},
    {'type': 'fruit', 'name': 'banana'},
    {'type': 'vegetable', 'name': 'carrot'}
]

# Must be sorted first!
data.sort(key=lambda x: x['type'])

for key, group in groupby(data, key=lambda x: x['type']):
    print(f"{key}: {list(group)}")
```

---

## 12. DATETIME

```python
from datetime import datetime, timedelta, date, time

# Current date/time
now = datetime.now()
today = date.today()

# Create datetime
dt = datetime(2024, 1, 15, 14, 30)

# Format datetime
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
formatted = now.strftime("%B %d, %Y")  # January 15, 2024

# Parse string to datetime
dt = datetime.strptime("2024-01-15", "%Y-%m-%d")

# Date arithmetic
tomorrow = today + timedelta(days=1)
last_week = now - timedelta(weeks=1)
in_3_hours = now + timedelta(hours=3)

# Extract components
year = now.year
month = now.month
day = now.day
hour = now.hour
weekday = now.weekday()  # 0=Monday, 6=Sunday
```

---

## 13. REGULAR EXPRESSIONS (Basics)

```python
import re

# Search
match = re.search(r'\d+', 'Order 123')  # Finds '123'
if match:
    print(match.group())

# Find all
numbers = re.findall(r'\d+', 'Order 123, Item 456')  # ['123', '456']

# Replace
text = re.sub(r'\d+', 'X', 'Order 123')  # 'Order X'

# Split
parts = re.split(r'[,\s]+', 'a, b  c')  # ['a', 'b', 'c']

# Match entire string
if re.match(r'^\d{3}-\d{4}$', '123-4567'):
    print("Valid format")

# Common patterns
r'\d'      # Digit
r'\w'      # Word character
r'\s'      # Whitespace
r'.'       # Any character
r'+'       # One or more
r'*'       # Zero or more
r'?'       # Zero or one
r'{3}'     # Exactly 3
r'{2,5}'   # 2 to 5
r'[abc]'   # a, b, or c
r'[^abc]'  # Not a, b, or c
r'^'       # Start of string
r'$'       # End of string
```

---

## 14. USEFUL IDIOMS

```python
# Check if list is empty
if not my_list:
    print("Empty")

# Get first/last items safely
first = my_list[0] if my_list else None
last = my_list[-1] if my_list else None

# Multiple comparisons
if 0 < x < 10:
    print("x is between 0 and 10")

# Conditional assignment
value = a if condition else b

# One-liner if
if condition: action()

# Dictionary get with computation
result = cache.get(key) or expensive_computation()

# Print with separator
print(*items, sep=', ')

# Unpack with rest
first, second, *rest, last = [1, 2, 3, 4, 5]

# Quick debugging print
print(f"{variable=}")  # Prints: variable=value
```

---

This covers 90% of Python syntax you'll use in practical programming. Keep this as a quick reference!
