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
x //= 2     # x = x // 2 (floor division - rounds down)
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


# Python Syntax - Additional Topics

## What Was Missing from the Main Cheatsheet

---

## 1. CLASSES & OBJECTS

### Basic Class
```python
class Dog:
    # Class variable (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def __repr__(self):
        return f"Dog(name='{self.name}', age={self.age})"

# Create instance
dog = Dog("Buddy", 3)
print(dog.bark())
print(dog)
```

### Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"
```

### Properties
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """Getter"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Setter"""
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def area(self):
        """Read-only property"""
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(circle.area)
circle.radius = 10  # Uses setter
```

### Static & Class Methods
```python
class Math:
    @staticmethod
    def add(a, b):
        """No access to self or cls"""
        return a + b
    
    @classmethod
    def from_string(cls, string):
        """Access to class, can create instances"""
        a, b = map(int, string.split(','))
        return cls(a, b)
```

### Magic Methods (Dunder)
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return self.x < other.x
    
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)
    
    def __getitem__(self, index):
        if index == 0: return self.x
        if index == 1: return self.y
        raise IndexError()
    
    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Uses __add__
print(p1[0])   # Uses __getitem__
```

### Dataclasses (Python 3.7+)
```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    hobbies: list = field(default_factory=list)
    
    def greet(self):
        return f"Hi, I'm {self.name}"

person = Person("Alice", 30)
print(person)  # Automatic __str__
```

---

## 2. DECORATORS

### Function Decorators
```python
# Basic decorator
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

# Same as: slow_function = timer(slow_function)

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello {name}")
```

### functools.wraps
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves original function metadata
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper
```

---

## 3. CONTEXT MANAGERS

### Using Context Managers
```python
# File handling (most common)
with open('file.txt') as f:
    data = f.read()

# Multiple context managers
with open('input.txt') as fin, open('output.txt', 'w') as fout:
    for line in fin:
        fout.write(line.upper())
```

### Creating Context Managers
```python
# Method 1: Class-based
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with FileManager('file.txt', 'r') as f:
    data = f.read()

# Method 2: contextlib
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    try:
        f = open(filename, mode)
        yield f
    finally:
        f.close()

with file_manager('file.txt', 'r') as f:
    data = f.read()
```

---

## 4. GENERATORS & ITERATORS

### Generators (Lazy Evaluation)
```python
# Generator function
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)  # 1, 2, 3, 4, 5

# Generator expression
gen = (x**2 for x in range(10))

# Infinite generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Use with next()
fib = fibonacci()
print(next(fib))  # 0
print(next(fib))  # 1
print(next(fib))  # 1

# Generator with send()
def echo():
    while True:
        value = yield
        print(f"Received: {value}")

gen = echo()
next(gen)  # Prime the generator
gen.send("Hello")
```

### Iterators
```python
class Countdown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for num in Countdown(5):
    print(num)  # 5, 4, 3, 2, 1
```

---

## 5. ADVANCED COMPREHENSIONS

### Nested Comprehensions
```python
# 2D matrix
matrix = [[i*j for j in range(5)] for i in range(5)]

# Flatten nested structure
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]

# Multiple conditions
[x for x in range(100) if x % 2 == 0 if x % 3 == 0]

# Nested loops in comprehension
[(x, y) for x in range(3) for y in range(3) if x != y]
```

### Dict Comprehension Advanced
```python
# Invert dictionary (swap keys/values)
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}

# Filter dictionary
filtered = {k: v for k, v in original.items() if v > 1}

# Transform values
squared = {k: v**2 for k, v in original.items()}
```

---

## 6. IMPORT VARIATIONS

```python
# Basic import
import math
print(math.pi)

# Import specific items
from math import pi, sqrt
print(pi)

# Import all (not recommended)
from math import *

# Import with alias
import numpy as np
import pandas as pd

# Import from package
from package.module import function

# Relative imports (within package)
from . import sibling
from .. import parent
from ..sibling import cousin

# Import module as variable
import importlib
module = importlib.import_module('module_name')
```

---

## 7. SLICING ADVANCED

```python
# Extended slicing
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list[::2]      # [0, 2, 4, 6, 8] - every 2nd
my_list[1::2]     # [1, 3, 5, 7, 9] - every 2nd starting at 1
my_list[::-1]     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - reverse
my_list[2:8:2]    # [2, 4, 6] - start:stop:step
my_list[-3:]      # [7, 8, 9] - last 3 items
my_list[:-3]      # [0, 1, 2, 3, 4, 5, 6] - all except last 3

# Slice assignment
my_list[2:5] = [20, 30, 40]  # Replace slice
my_list[2:5] = []             # Delete slice

# Slice object
s = slice(1, 5, 2)
my_list[s]  # Same as my_list[1:5:2]
```

---

## 8. UNPACKING ADVANCED

```python
# Basic unpacking
a, b = 1, 2

# With *rest
first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2,3,4], last=5

# Nested unpacking
(a, b), (c, d) = [(1, 2), (3, 4)]

# Unpacking in loops
for x, y in [(1, 2), (3, 4)]:
    print(x, y)

# Dict unpacking
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
merged = {**d1, **d2}  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# List unpacking
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [*list1, *list2]  # [1, 2, 3, 4, 5, 6]

# Function call unpacking
def func(a, b, c):
    return a + b + c

args = [1, 2, 3]
result = func(*args)

kwargs = {'a': 1, 'b': 2, 'c': 3}
result = func(**kwargs)
```

---

## 9. OPERATOR MODULE

```python
import operator

# Arithmetic
operator.add(1, 2)      # 3
operator.sub(5, 3)      # 2
operator.mul(3, 4)      # 12
operator.truediv(10, 3) # 3.333...
operator.floordiv(10, 3)# 3
operator.mod(10, 3)     # 1
operator.pow(2, 3)      # 8

# Comparison
operator.eq(1, 1)       # True
operator.ne(1, 2)       # True
operator.lt(1, 2)       # True
operator.le(1, 1)       # True
operator.gt(2, 1)       # True
operator.ge(2, 2)       # True

# Logical
operator.and_(True, False)  # False
operator.or_(True, False)   # True
operator.not_(True)         # False

# Item access
operator.getitem([1, 2, 3], 0)     # 1
operator.setitem(my_list, 0, 10)   # my_list[0] = 10
operator.delitem(my_list, 0)       # del my_list[0]

# Attribute access
operator.attrgetter('name')(obj)   # obj.name
operator.methodcaller('sort')(list) # list.sort()

# Use in sorting
from operator import itemgetter
students = [('Alice', 25), ('Bob', 20)]
sorted(students, key=itemgetter(1))  # Sort by age
```

---

## 10. MULTIPLE ASSIGNMENT FORMS

```python
# Parallel assignment
x, y = 1, 2

# Chained assignment
x = y = z = 0

# Augmented assignment
x += 5
x *= 2

# Conditional assignment
x = a if condition else b

# Assignment expressions (walrus := )
if (n := len(my_list)) > 10:
    print(f"List has {n} items")

while (line := file.readline()):
    process(line)

# Multiple targets
(a, b) = [c, d] = (1, 2)
```

---

## 11. ENUMERATE VARIATIONS

```python
# Basic
for i, val in enumerate(['a', 'b', 'c']):
    print(i, val)  # 0 a, 1 b, 2 c

# Custom start
for i, val in enumerate(['a', 'b', 'c'], start=1):
    print(i, val)  # 1 a, 2 b, 3 c

# With unpacking
data = [('Alice', 25), ('Bob', 30)]
for i, (name, age) in enumerate(data):
    print(f"{i}: {name} is {age}")
```

---

## 12. ZIP VARIATIONS

```python
# Basic zip
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(name, age)

# Multiple iterables
for a, b, c in zip(list1, list2, list3):
    print(a, b, c)

# Unzip
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
# numbers = (1, 2, 3)
# letters = ('a', 'b', 'c')

# zip_longest (from itertools)
from itertools import zip_longest
for a, b in zip_longest([1, 2, 3], ['a', 'b'], fillvalue='-'):
    print(a, b)  # 1 a, 2 b, 3 -
```

---

## 13. ASSERT & DEBUG

```python
# Assert statement
assert condition, "Error message"

# Examples
assert x > 0, "x must be positive"
assert len(data) > 0, "Data cannot be empty"

# Disable assertions with python -O
# or set PYTHONOPTIMIZE=1

# Type assertions (for documentation, not enforced)
def greet(name: str) -> str:
    return f"Hello, {name}"

# More complex types
from typing import List, Dict, Tuple, Optional, Union

def process(items: List[int]) -> Dict[str, int]:
    return {'count': len(items)}

def find(query: str) -> Optional[str]:
    return result if result else None
```

---

## 14. GLOBAL & NONLOCAL

```python
# Global keyword
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # 1

# Nonlocal (for nested functions)
def outer():
    count = 0
    
    def inner():
        nonlocal count
        count += 1
    
    inner()
    return count

print(outer())  # 1
```

---

## 15. PASS, ELLIPSIS, NONE

```python
# Pass (do nothing)
def not_implemented():
    pass

for i in range(10):
    if i % 2 == 0:
        pass  # TODO: handle evens
    else:
        print(i)

# Ellipsis (... literal)
def function_stub():
    ...

# Can be used as a placeholder
def multiply(a: int, b: int) -> int:
    ...

# None
x = None

def function():
    return None  # or just: return

# Check for None
if x is None:
    print("x is None")
```

---

## 16. WITH STATEMENTS ADVANCED

```python
# Suppress exceptions
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('file.txt')  # No error if file doesn't exist

# Redirect stdout
from contextlib import redirect_stdout
import io

f = io.StringIO()
with redirect_stdout(f):
    print("Hello")
output = f.getvalue()  # "Hello\n"

# ExitStack (manage multiple context managers dynamically)
from contextlib import ExitStack

with ExitStack() as stack:
    files = [stack.enter_context(open(f)) for f in filenames]
    # All files closed automatically
```

---

## 17. MATCH/CASE (Python 3.10+)

```python
# Structural pattern matching
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500 | 501 | 502:
            return "Server Error"
        case _:
            return "Unknown"

# Match with patterns
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y-axis at {y}")
    case (x, 0):
        print(f"X-axis at {x}")
    case (x, y):
        print(f"Point at {x}, {y}")

# Match with conditions
match value:
    case x if x < 0:
        print("Negative")
    case x if x == 0:
        print("Zero")
    case x if x > 0:
        print("Positive")
```

---

## 18. ASYNC/AWAIT (Basics)

```python
import asyncio

# Async function
async def fetch_data():
    await asyncio.sleep(1)  # Simulate IO
    return "data"

# Run async function
async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())

# Multiple async tasks
async def main():
    results = await asyncio.gather(
        fetch_data(),
        fetch_data(),
        fetch_data()
    )
    print(results)
```

---

## 19. TYPE HINTS (Extended)

```python
from typing import (
    List, Dict, Set, Tuple,
    Optional, Union, Any,
    Callable, TypeVar, Generic
)

# Basic types
def greet(name: str, age: int) -> str:
    return f"{name} is {age}"

# Collections
def process(items: List[int]) -> Dict[str, int]:
    return {'sum': sum(items)}

# Optional (can be None)
def find(query: str) -> Optional[str]:
    return result if exists else None

# Union (multiple types)
def parse(value: Union[int, str]) -> int:
    return int(value)

# Callable
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

# Generic types
T = TypeVar('T')

def first(items: List[T]) -> Optional[T]:
    return items[0] if items else None
```

---

## 20. COMMONLY MISSED BUILTINS

```python
# any() and all()
any([False, False, True])   # True
all([True, True, False])    # False

# divmod()
quotient, remainder = divmod(17, 5)  # (3, 2)

# bin(), oct(), hex()
bin(10)  # '0b1010'
oct(10)  # '0o12'
hex(10)  # '0xa'

# chr() and ord()
chr(65)  # 'A'
ord('A') # 65

# eval() and exec() (dangerous!)
eval("2 + 2")           # 4
exec("x = 2 + 2")       # Creates variable x

# globals() and locals()
globals()  # Dict of global variables
locals()   # Dict of local variables

# hasattr(), getattr(), setattr()
hasattr(obj, 'name')           # Check if attribute exists
getattr(obj, 'name', 'default') # Get attribute with default
setattr(obj, 'name', 'value')  # Set attribute

# id()
id(obj)  # Memory address

# isinstance() and issubclass()
isinstance(5, int)              # True
issubclass(bool, int)           # True

# vars()
vars(obj)  # __dict__ of object
```

---

## Summary of What's Still Missing

Even this extended list doesn't cover:
- **Metaclasses** (rarely needed)
- **Descriptors** (advanced)
- **Abstract Base Classes** (typing.ABC)
- **Coroutines** (advanced async)
- **Memory views** (advanced)
- **Weak references** (garbage collection)
- **ctypes** (C interop)
- **multiprocessing** (parallel processing)
- **threading** (concurrent programming)
- **sockets** (network programming)
- **pickle/json/yaml** (serialization)
- **argparse** (CLI arguments)
- **logging** (better than print)
- **pathlib** (modern file paths)
