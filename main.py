# Our first class teaches Python Data Types

# PRIMITIVE DATA TYPES- These are data types defined by the programming language
# -------------------------------------------------------------------------------------------------------------

# Strings - Any form of character written in quotes " "
name = "Atom"

# Integers - Whole numbers
age = 12

# Float - Decimal numbers
height = 23.2

# Boolean - True or False
my_age = 18
driving_age = my_age >= 18
print(driving_age)

# NON PRIMITIVE DATA TYPES- These are data types that are defined by the programmer.
# They are also called "reference variables" because they point to a memory location which stores the data
# ---------------------------------------------------------------------------------------------------------------

# Lists - Lists are used to store multiple items in a single variable.
data_types = [12, 23, 40, True, "Codex"]

# Arrays - They store a fixed number of items of the same data type in a single variable.
# Arrays work with python libraries like "NumPy"
ages = [10, 12, 15]

# Tuples - They used to store ordered pairs with unique identifiers / index numbers
names = ("frances", "Nwaka", "Ogochukwu")

# Dictionary - This stores key-value pairs which are unordered, changeable and does not all duplication
myInventory = {
    "item": "Air Jordan",
    "colour": "Black",
    "size": "42"
}

# Sets - A set is a collection which is both unordered and unindexed.
csc_students = {'kosi', 'atom', 'jb', 'frances', 'peter', 'sampson'}

# File - files are named locations on disks used to store related information permanently.
# open() read() etc
