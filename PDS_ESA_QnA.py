# ============================================================
#          PDS ESA – SECTION A: QUESTIONS & ANSWERS
#          Python Programs with Explanations
# ============================================================


# ============================================================
# 1(a) How are dictionaries different from lists in Python?
# ============================================================
# List: ordered, accessed by index, uses []
# Dictionary: key-value pairs, accessed by key, uses {}

a_list = [10, 20, 30]
print("List element at index 1:", a_list[1])   # 20

a_dict = {"name": "Ram", "age": 21}
print("Dict value for key 'name':", a_dict["name"])   # Ram


# ============================================================
# 1(b) What is a lambda function?
# ============================================================
# Lambda: anonymous, one-line function using the `lambda` keyword
# Regular function needs `def`, can have multiple lines.

square_lambda = lambda x: x * x
print("Lambda square of 5:", square_lambda(5))   # 25

def square_regular(x):
    return x * x

print("Regular square of 5:", square_regular(5))   # 25


# ============================================================
# 1(c) What is string immutability in Python?
# ============================================================
# Once a string is created, its characters cannot be changed.
# Any modification creates a NEW string instead.

s = "Python"
# s[0] = 'J'   # This would raise a TypeError
s = "Jython"   # New string created
print("New string:", s)


# ============================================================
# 1(d) Slice 'PythonProgramming' to get 'thonPro'
# ============================================================
# Syntax: string[start:end] -> characters from index start to end-1

s = "PythonProgramming"
print("Sliced string:", s[2:9])   # thonPro


# ============================================================
# 1(e) What does *args do in a function?
# ============================================================
# *args allows a function to accept any number of positional arguments.
# They are stored as a tuple inside the function.

def add(*args):
    return sum(args)

print("Sum with *args:", add(1, 2, 3, 4))   # 10


# ============================================================
# 2(a) How are sorted() and sort() used with lists?
# ============================================================
# sort()   -> modifies the original list, works only on lists
# sorted() -> returns a NEW sorted list, works on any iterable

a = [4, 1, 3]
a.sort()
print("After sort():", a)    # [1, 3, 4]

b = [4, 1, 3]
c = sorted(b)
print("After sorted():", c)  # [1, 3, 4]
print("Original b:", b)      # [4, 1, 3] — unchanged


# ============================================================
# 2(b) How can you get a random number in Python?
# ============================================================
# Use the built-in `random` module.

import random

print("Random integer (1-10):", random.randint(1, 10))
print("Random float (0-1):", random.random())


# ============================================================
# 2(c) What are map() and reduce() functions?
# ============================================================
# map()    -> applies a function to EVERY element of an iterable
# reduce() -> reduces the iterable to a SINGLE value

from functools import reduce

nums = [1, 2, 3, 4]

squared = list(map(lambda x: x * x, nums))
print("map() - squares:", squared)   # [1, 4, 9, 16]

total = reduce(lambda x, y: x + y, nums)
print("reduce() - sum:", total)       # 10


# ============================================================
# 2(d) Difference between reshape() and resize() in NumPy
# ============================================================
# reshape() -> returns a NEW array with the new shape
# resize()  -> modifies the ORIGINAL array in-place

import numpy as np

a = np.array([1, 2, 3, 4])

b = a.reshape(2, 2)
print("reshape() result:\n", b)
print("Original a after reshape():", a)   # unchanged

a.resize(2, 2)
print("Original a after resize():\n", a)  # modified in-place


# ============================================================
# 2(e) Difference between pivot_table and crosstab
# ============================================================
# pivot_table -> aggregation (sum, mean, etc.) on numerical data
# crosstab    -> frequency count of combinations (categorical data)

import pandas as pd

df = pd.DataFrame({
    "Region": ["North", "South", "North", "South"],
    "Gender": ["M", "F", "F", "M"],
    "Sales": [100, 200, 150, 250],
    "Result": ["Pass", "Fail", "Pass", "Pass"]
})

pivot = pd.pivot_table(df, values="Sales", index="Region", aggfunc="sum")
print("\nPivot Table (Sum of Sales):\n", pivot)

cross = pd.crosstab(df["Gender"], df["Result"])
print("\nCross Table (Frequency):\n", cross)


# ============================================================
# 3(a) Difference between List and Tuple
# ============================================================
# List   -> mutable, uses [], slower
# Tuple  -> immutable, uses (), faster

my_list = [1, 2, 3]
my_list[0] = 10   # OK
print("Modified list:", my_list)

my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment


# ============================================================
# 3(b) Use of break and continue
# ============================================================
# break    -> exits the loop immediately
# continue -> skips the current iteration and moves to next

print("\nbreak example:")
for i in range(5):
    if i == 3:
        break
    print(i)   # 0 1 2

print("\ncontinue example:")
for i in range(5):
    if i == 3:
        continue
    print(i)   # 0 1 2 4


# ============================================================
# 3(c) What is a Dictionary in Python?
# ============================================================
# A dictionary stores data as key-value pairs, unordered, mutable.

student = {"name": "Ram", "age": 20}
print("\nDictionary:", student)
print("Value for 'name':", student["name"])


# ============================================================
# 3(d) Difference between append() and extend()
# ============================================================
# append() -> adds a SINGLE element (even a list as one item)
# extend() -> adds each element of an iterable individually

a = [1, 2]
a.append([3, 4])
print("\nappend():", a)   # [1, 2, [3, 4]]

b = [1, 2]
b.extend([3, 4])
print("extend():", b)    # [1, 2, 3, 4]


# ============================================================
# 4(a) What is NumPy?
# ============================================================
# NumPy is a Python library for fast numerical computing and
# multi-dimensional array operations.

import numpy as np

arr = np.array([1, 2, 3])
print("\nNumPy array:", arr)
print("Array type:", type(arr))


# ============================================================
# 4(b) What is Pandas?
# ============================================================
# Pandas is a Python library for data analysis and manipulation.
# It provides Series (1D) and DataFrame (2D) data structures.

import pandas as pd

data = {"Name": ["Ram", "Sam"], "Age": [20, 22]}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)


# ============================================================
# 4(c) Difference between Series and DataFrame
# ============================================================
# Series    -> 1-dimensional, single column
# DataFrame -> 2-dimensional, multiple columns

s = pd.Series([10, 20, 30])
print("\nSeries:\n", s)

df2 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print("\nDataFrame:\n", df2)


# ============================================================
# 4(d) Use of iloc[] and loc[] in Pandas
# ============================================================
# iloc[] -> integer position-based indexing
# loc[]  -> label-based indexing

df3 = pd.DataFrame({"Name": ["A", "B", "C"], "Marks": [80, 45, 90]})

print("\niloc[0] (first row by position):\n", df3.iloc[0])
print("\nloc[1] (row with label 1):\n", df3.loc[1])


# ============================================================
# 4(e) What is Data Visualization?
# ============================================================
# Displaying data graphically using charts, plots, etc.
# Common libraries: Matplotlib, Seaborn

import matplotlib
matplotlib.use("Agg")  # Non-interactive backend for script environments
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o', color='blue', label='y = 2x')
plt.title("Simple Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.savefig("line_plot.png")  # Saves to file
plt.close()
print("\nLine plot saved as 'line_plot.png'")


# ============================================================
# 5(a) How to generate a random float between 0 and 1?
# ============================================================

import random
print("\nRandom float (0-1):", random.random())


# ============================================================
# 5(b) Difference between pop() and remove()
# ============================================================
# pop()    -> removes by INDEX, returns the removed element
# remove() -> removes by VALUE, returns nothing

a = [10, 20, 30]
removed = a.pop()
print("\npop() removed:", removed, "| List now:", a)  # 30

b = [10, 20, 30]
b.remove(20)
print("remove(20) | List now:", b)  # [10, 30]


# ============================================================
# 5(c) Purpose of filter() function
# ============================================================
# filter() filters elements from an iterable based on a condition.
# Returns an iterator; wrap in list() to see results.

nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print("\nEven numbers:", even)   # [2, 4, 6]


# ============================================================
# 5(d) Purpose of enumerate() function
# ============================================================
# enumerate() adds an automatic counter (index) to an iterable.
# Useful in loops when you need both index and value.

fruits = ["apple", "banana", "mango"]
print("\nenumerate() example:")
for index, value in enumerate(fruits):
    print(index, value)


# ============================================================
# 5(e) Difference between arange() and linspace() in NumPy
# ============================================================
# arange()  -> uses a STEP SIZE, may exclude endpoint
# linspace() -> uses NUMBER OF POINTS, includes endpoint by default

import numpy as np

print("\narange(0, 10, 2):", np.arange(0, 10, 2))     # [0 2 4 6 8]
print("linspace(0, 10, 5):", np.linspace(0, 10, 5))   # [0. 2.5 5. 7.5 10.]


# ============================================================
# 6(a) Select subset of rows using condition in Pandas
# ============================================================

df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Marks": [80, 45, 90]
})
result = df[df["Marks"] > 50]
print("\nRows with Marks > 50:\n", result)


# ============================================================
# 6(b) groupby() in Pandas
# ============================================================
# groupby() groups data by a column and applies aggregate functions.

df_dept = pd.DataFrame({
    "Dept": ["IT", "IT", "HR"],
    "Salary": [5000, 6000, 4000]
})
grouped = df_dept.groupby("Dept")["Salary"].mean()
print("\nAverage Salary by Dept:\n", grouped)


# ============================================================
# 6(c) How to remove missing data from a DataFrame?
# ============================================================
# dropna() removes rows with any NaN values.
# fillna() replaces NaN with a given value.

import numpy as np

df_miss = pd.DataFrame({"A": [1, None, 3], "B": [4, 5, None]})
print("\nOriginal DataFrame:\n", df_miss)

df_dropped = df_miss.dropna()
print("After dropna():\n", df_dropped)

df_filled = df_miss.fillna(0)
print("After fillna(0):\n", df_filled)


# ============================================================
# 6(d) Difference between apply() and map() in Pandas
# ============================================================
# apply() -> works on Series or DataFrame (row/column operations)
# map()   -> works element-wise on a Series only

df_marks = pd.DataFrame({"Marks": [70, 80, 90]})

df_marks["apply_result"] = df_marks["Marks"].apply(lambda x: x + 5)
df_marks["map_result"] = df_marks["Marks"].map(lambda x: x + 5)

print("\napply() vs map():\n", df_marks)


# ============================================================
# 6(e) How to reset the index of a DataFrame?
# ============================================================
# reset_index() resets the index to default (0, 1, 2...)
# The old index becomes a regular column unless drop=True.

df_idx = pd.DataFrame({"A": [10, 20]}, index=[5, 10])
print("\nOriginal DataFrame:\n", df_idx)
print("After reset_index():\n", df_idx.reset_index())


# ============================================================
# 7(a) What is type casting in Python?
# ============================================================
# Type casting = converting one data type to another.
# Implicit: Python does it automatically
# Explicit: Programmer does it manually using int(), float(), str()

a = "100"
b = int(a)        # Explicit casting: str -> int
print("\nType casting:", b, type(b))

x = 5
y = 2.5
z = x + y         # Implicit: int + float -> float automatically
print("Implicit casting:", z, type(z))


# ============================================================
# 7(b) What are *args and **kwargs?
# ============================================================
# *args   -> accepts variable number of POSITIONAL arguments (tuple)
# **kwargs -> accepts variable number of KEYWORD arguments (dict)

def demo(*args, **kwargs):
    print("\n*args:", args)
    print("**kwargs:", kwargs)

demo(1, 2, 3, name="Ram", age=20)


# ============================================================
# 7(c) Difference between del, clear(), remove(), pop()
# ============================================================

a = [1, 2, 3, 4, 5]
a.remove(3)      # removes first occurrence of value 3
print("\nAfter remove(3):", a)

a.pop(0)         # removes element at index 0
print("After pop(0):", a)

a.clear()        # removes all elements
print("After clear():", a)

b = [10, 20, 30]
del b[1]         # deletes element at index 1
print("After del b[1]:", b)


# ============================================================
# 7(d) What are list and dictionary comprehensions?
# ============================================================
# Comprehensions are a concise way to create lists/dicts from iterables.

squares_list = [x * x for x in range(5)]
print("\nList comprehension:", squares_list)   # [0, 1, 4, 9, 16]

squares_dict = {x: x * x for x in range(5)}
print("Dict comprehension:", squares_dict)    # {0:0, 1:1, 2:4, 3:9, 4:16}


# ============================================================
# 7(e) Negative indexing in Python
# ============================================================
# Negative index -1 refers to last element, -2 second last, etc.

a = [10, 20, 30, 40]
print("\nNegative indexing:")
print("a[-1]:", a[-1])   # 40
print("a[-2]:", a[-2])   # 30


# ============================================================
# 8(a) How to remove duplicates from a DataFrame?
# ============================================================

df_dup = pd.DataFrame({"A": [1, 2, 2, 3], "B": [4, 5, 5, 6]})
print("\nBefore drop_duplicates:\n", df_dup)
print("After drop_duplicates:\n", df_dup.drop_duplicates())


# ============================================================
# 8(b) Identify and handle missing values
# ============================================================

df_null = pd.DataFrame({"Name": ["A", None, "C"], "Score": [90, None, 70]})
print("\nisnull():\n", df_null.isnull())
print("dropna():\n", df_null.dropna())
print("fillna('Unknown'):\n", df_null.fillna("Unknown"))


# ============================================================
# 8(c) Ranking methods for Pandas Series
# ============================================================
# average -> mean rank for ties
# min     -> minimum rank for ties
# max     -> maximum rank for ties
# first   -> rank in order of appearance
# dense   -> like min but no gaps

s = pd.Series([100, 200, 200, 300])
print("\nRanking with method='dense':")
print(s.rank(method="dense"))

print("Ranking with method='average':")
print(s.rank(method="average"))


# ============================================================
# 8(d) How is vstack() different from hstack() in NumPy?
# ============================================================
# vstack() -> stack arrays vertically (row-wise)
# hstack() -> stack arrays horizontally (column-wise)

a = np.array([1, 2])
b = np.array([3, 4])

print("\nvstack:\n", np.vstack((a, b)))
print("hstack:", np.hstack((a, b)))


# ============================================================
# 8(e) Difference between sort_values() and sort_index()
# ============================================================
# sort_values() -> sorts by DATA values
# sort_index()  -> sorts by INDEX labels

s = pd.Series([30, 10, 20], index=["c", "a", "b"])
print("\nsort_values():\n", s.sort_values())
print("sort_index():\n", s.sort_index())


# ============================================================
# 9(a) Python is case-sensitive
# ============================================================

name = "Python"
Name = "Programming"
print("\nname:", name)
print("Name:", Name)   # Different variables!


# ============================================================
# 9(b) Implicit type casting examples
# ============================================================

# int + float -> float
a = 10
b = 5.5
c = a + b
print("\nImplicit (int + float):", c, type(c))

# bool + int -> int
x = True
y = 5
print("Implicit (bool + int):", x + y)   # 6


# ============================================================
# 9(c) Complex data type in Python
# ============================================================
# Complex numbers: a + bj

x = 4 + 5j
print("\nComplex number:", x)
print("Type:", type(x))
print("Real part:", x.real)
print("Imaginary part:", x.imag)


# ============================================================
# 9(d) Default parameter in user-defined function
# ============================================================
# A default parameter takes a preset value if no argument is passed.

def greet(name="Guest"):
    print("Hello,", name)

greet()          # Uses default
greet("Ram")     # Overrides default


# ============================================================
# 9(e) Arithmetic operators with strings
# ============================================================
# + -> concatenation (joining)
# * -> repetition (repeat the string n times)

a = "Python"
b = "Programming"

print("\nConcatenation (+):", a + " " + b)
print("Repetition (*):", a * 3)


# ============================================================
# 10(a) Features of NumPy
# ============================================================
# - Fast numerical computations
# - Multi-dimensional arrays (ndarray)
# - Math and statistical functions
# - Broadcasting support
# - Memory efficient

a = np.array([[1, 2, 3], [4, 5, 6]])
print("\nNumPy 2D array:\n", a)
print("Shape:", a.shape)
print("Mean:", a.mean())


# ============================================================
# 10(b) NumPy random package
# ============================================================

print("\nnp.random.rand(3):", np.random.rand(3))           # 3 random floats [0, 1)
print("np.random.randint(1, 10, 5):", np.random.randint(1, 10, 5))  # 5 random ints


# ============================================================
# 10(c) Delete rows and columns from a DataFrame
# ============================================================

df_del = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Marks": [80, 90, 70],
    "Grade": ["B", "A", "B"]
})

print("\nOriginal DataFrame:\n", df_del)
print("After dropping row 0:\n", df_del.drop(0))
print("After dropping column 'Grade':\n", df_del.drop("Grade", axis=1))


# ============================================================
# 10(d) How to rank rows of a DataFrame?
# ============================================================

df_rank = pd.DataFrame({"Marks": [90, 70, 80]})
print("\nDataFrame with ranks:\n", df_rank.rank())


# ============================================================
# 11. Identity Matrix using NumPy
# ============================================================
# Identity matrix: square matrix with 1s on diagonal, 0s elsewhere.

identity = np.eye(3)
print("\n3x3 Identity Matrix:\n", identity)


# ============================================================
# 12. split() for NumPy arrays
# ============================================================
# np.split(array, n) -> divides array into n equal sub-arrays

a = np.array([1, 2, 3, 4, 5, 6])
parts = np.split(a, 3)
print("\nnp.split into 3 parts:", parts)


# ============================================================
# 13. How to count occurrences of an element in a list?
# ============================================================

a = ["a", "b", "a", "c", "a"]
print("\nCount of 'a':", a.count("a"))   # 3


# ============================================================
# 14. Global keyword in Python
# ============================================================
# global allows a function to modify a variable in global scope.

x = 10

def modify():
    global x
    x = 99

modify()
print("\nAfter modifying global x:", x)   # 99


# ============================================================
# 15. find() vs index() in strings
# ============================================================
# find()  -> returns -1 if substring not found (safe)
# index() -> raises ValueError if not found (risky)

s = "Python Programming"

print("\nfind('gram'):", s.find("gram"))       # 12
print("index('gram'):", s.index("gram"))       # 12
print("find('xyz'):", s.find("xyz"))           # -1
# print("index('xyz'):", s.index("xyz"))       # ValueError!


# ============================================================
# 16. How to change value of a key in dictionary?
# ============================================================

student = {"name": "Ram", "age": 20}
student["age"] = 25   # Direct assignment updates the value
print("\nUpdated dictionary:", student)


# ============================================================
# 17. How to combine DataFrames using concat(), merge(), join()
# ============================================================

df1 = pd.DataFrame({"Name": ["A", "B"], "Score": [80, 90]})
df2 = pd.DataFrame({"Name": ["C", "D"], "Score": [70, 85]})

# concat() -> stacks DataFrames (like row/column append)
combined = pd.concat([df1, df2], ignore_index=True)
print("\nconcat result:\n", combined)

# merge() -> joins on common columns (like SQL JOIN)
df3 = pd.DataFrame({"Name": ["A", "B"], "Grade": ["B", "A"]})
merged = pd.merge(df1, df3, on="Name")
print("merge result:\n", merged)


# ============================================================
# 18. Categorical data in Pandas
# ============================================================
# Categorical dtype saves memory for repeated labels.

data = pd.Series(["High", "Low", "Medium", "High", "Low"], dtype="category")
print("\nCategorical Series:\n", data)
print("Categories:", data.cat.categories.tolist())


# ============================================================
# END OF FILE
# ============================================================
print("\n✅ All PDS ESA questions executed successfully!")
