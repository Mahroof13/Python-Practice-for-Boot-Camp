# Lists
students = ["Alice", "Bob", "Charlie", "David"]

# Append
students.append("Eva")
print(f"Append: {students}")

# Insert
students.insert(2, "Frank")
print(f"Insert: {students}")

# Remove
students.remove("Bob")
print(f"Remove: {students}")

# Copy
students_shallow_copy = students.copy()
students_shallow_copy[0] = "Gabriella"
print(f"Shallow Copy: {students_shallow_copy}, Original: {students}")

# Deep Copy
import copy
students_deep_copy = copy.deepcopy(students)
students_deep_copy[0] = "Hannah"
print(f"Deep Copy: {students_deep_copy}, Original: {students}")

# Count
students.append("Alice")
alice_count = students.count("Alice")
print(f"Count of 'Alice': {alice_count}")

# Extend
more_students = ["Ivan", "Julia", "Kevin"]
students.extend(more_students)
print(f"Extend: {students}")

# Index
alice_index = students.index("Alice")
print(f"Index of 'Alice': {alice_index}")

# Sort
students.sort()
print(f"Sort: {students}")

# Reverse
students.reverse()
print(f"Reverse: {students}")

# Clear
students.clear()
print(f"Clear: {students}")

# Pop
more_students = ["Lucas", "Mia", "Nina"]
removed_student = more_students.pop()
print(f"Pop: {removed_student}, Remaining: {more_students}")

# Create a list of cities
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia"]

# Insert a new city at the beginning of the list
cities.insert(0, "San Francisco")
print("Insert at the Beginning:", cities)

# Insert a new city at the end of the list
cities.append("Dallas")
print("Insert at the End:", cities)

# Insert a new city at a specific position
cities.insert(3, "Washington D.C.")
print("Insert at a Specific Position:", cities)

# Tuples
x = ("Python", "Java", "C++", "JavaScript")
print(x)

# Tuple Length:
programming_languages = ("Python", "Java", "C++", "JavaScript", "Ruby", "Swift")
print(len(programming_languages))

tuple2 = (17, "hello", 3.14, False, "female")
print(tuple2)

q = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(q)

# Print the second item in the tuple:
w = ("apple", "banana", "cherry")
print(w[1])

# Return the third, fourth, and fifth item:
e = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(e[2:5])

# Return the items from the beginning to, but NOT included, "kiwi":
t = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(t[:4])

# Return the items from index -4 (included) to index -1 (excluded)
le = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(le[-4:-1])