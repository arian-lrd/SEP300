# Lab 2 assignment in SEP300 course
# Student: Arian Amiri
# Student ID: 186610218

# A list, a Set, and a Dictionary
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
colors = {"red", "blue", "green", "yellow", "purple"}
scores = {"Alice": 80, "Bob": 90, "Alicia": 75}

# List comprehension
numbers_squared = [x**2 for x in numbers]
print(numbers_squared)


# dictionary comprehension
scores_increased = {k:v+5    for (k,v) in scores.items()}
print(scores_increased)


# Set comprehension:
colors_upper = [x.upper() for x in colors]
print(colors_upper)


# List comprehension: With if statement
numbers_odd = [x for x in numbers if x % 2 != 0]
print(numbers_odd)


# Dictionary comprehension: With if statement
scores_above_80 = {k:(v if v>= 80 else "F"
                      ) for (k,v) in scores.items()  }
print(scores_above_80)




