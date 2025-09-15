# Python List Data Type
languages = ["Python", "Dart", "Web", 23]
print(languages)
print(languages[0]) # Accessing the first element
print(languages[1:3]) #slicing the list

# Python Tuple Data Type
fruits = ("Mango", "Banana", "Orange")
print(fruits)

products = ('XBox', 499.99, "Habibi", 23)
print(products)

# python set data type
car_brands = {"BMW", "Toyota", "Honda"}
print(car_brands)

student_ids = {112, 114, 117, 113}
print(student_ids)

# Python Dictionary Data Type
person = {
    "name" : "Lynn",
    "age" : 25,
    "city" : "Nairobi"}
print(person)

capital_city = {"Kenya": "Nairobi", "Nigeria": "Lagos"}
print(capital_city)
    # week1
# Here are some fun and beginner-friendly project ideas you can try at this stage:

# 1. Personalized Greeting App 👋
# Create a program that asks for the user’s name and favorite color, then prints a personalized greeting like: “Hello, [Name]! Your favorite color, [Color], is awesome!”
# 2. Simple Quiz Game 🎮
# Create a multiple-choice quiz with questions about Python, movies, or any fun topic! Display scores at the end and allow the user to play again. 🏆
# 3. Random Joke Generator 🤣
# Build a program that stores a list of jokes and randomly selects one to display every time the user runs it. Add a fun twist with jokes about Python or programming! 🐍💡

          #week 2
# Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
#Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
#Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

# Coding Challenges for basic control flows and functions




# 1. Large Power

# Create a method that tests whether the result of taking the power of one number to another number provides an answer which is greater than 5000. We will use a conditional statement to return True if the result is greater than 5000 or return False if it is not. In order to accomplish this, we will need the following steps:

# Define the function to accept two input parameters called base and exponent
# Calculate the result of base to the power of exponent
# Use an if statement to test if the result is greater than 5000. If it is then return True. Otherwise, return False




# Coding Question

# Create a function named large_power() that takes two parameters named base and exponent.

# If base raised to the exponent is greater than 5000, return True, otherwise return False



# 2.Divisible By Ten

# Create a function that determines whether or not a number is divisible by ten. A number is divisible by ten if the remainder of the number divided by 10 is 0. Using this, we can complete this function in a few steps:

# Define the function header to accept one input num
# Calculate the remainder of the input divided by 10 (use modulus)
# Use an if statement to check if the remainder was 0. If the remainder was 0, return True, otherwise, return False




# Coding question

# Create a function called divisible_by_ten() that has one parameter named num.

# The function should return True if num is divisible by 10, and False otherwise. Consider using modulo operator % to check for divisibility.


# 🔹 Challenge: Create a program that reads a text file, processes its content, and writes the results to a new file.

# 📌 Task Requirements:
# Create a file called input.txt and write at least five lines of text into it.
# Write a Python script to:
# Read the contents of input.txt.
# Count the number of words in the file.
# Convert all text to uppercase.
# Write the processed text and the word count to a new file called output.txt.
# Print a success message once the new file is created.