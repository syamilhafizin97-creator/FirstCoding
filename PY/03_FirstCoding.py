# name = input("Enter your name: ")
# height = float(input("Enter your height in meters: "))

# # Input Validation
# while True:
#     try:
#         age = int(input("Enter your age: "))
#         if age > 0:
#             break
#         else:
#             print("Age must be a positive number. Please try again.")
#     except ValueError:
#         print("Please enter a valid number!")


# # Output validation
# print(f"Hello, {name}! ")
# print(f"You are {age} years old and {height} meters tall.")

# while True:
#     try:
#         number1 = float(input("Enter a number: "))
#         number2 = float(input("Enter another number: "))
#         operation = input("Enter an operation (+, -, *, /): ")

#         if operation == "+":
#             result = number1 + number2
#         elif operation == "-":
#             result = number1 - number2
#         elif operation == "*":
#             result = number1 * number2
#         elif operation == "/":
#             if number2 != 0:
#                 result = number1 / number2
#             else:
#                 print("Error: Division by zero is not allowed.")
#                 continue
#         else:
#             print("Invalid operation. Please enter +, -, *, or /.")
#             continue

#         print(f"Result: {result}")
#         break

#     except ValueError:
#         print("Please enter valid numbers!")

#Question 2
score = 0

## Question 1
answer1 = input("What day is today? ")
if answer1.lower().strip() == "wednesday":
    print("Correct!")   
    score += 1  
else:
    print("Incorrect. The correct answer is Wednesday.")    

## Question 2
answer2 = input("What is my cat name? ")
if answer2.lower().strip() == "milo":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Milo.")

## Question 3
answer3 = input("What is my favorite color? ")
if answer3.lower().strip() == "blue":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Blue.")

print(f"Your final score is {score} out of 3.")
if score == 3:
    print("Excellent work!")          
elif score == 2:
    print("Good job!")
else:
    print("Better luck next time!") 