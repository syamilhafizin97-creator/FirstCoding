# # Conditional Statements

# age = 20
# if age >= 18:
#     print("You are an adult.")  
# else: 
#     print("You are a minor.")

# # Score

# score = 50
# if score >=90:
#     grade = 'A'

# elif score >=80:
#     grade = 'B'
# elif score >=70:
#     grade = 'C'
# else:
#     grade = 'D'

# print(f"Your grade is {grade}.")    

# # and & or

# user_age = 25
# has_license = True

# if user_age >= 18 and has_license:
#     print("You can drive.")     
# else:
#     print("You cannot drive.")

# day = "Saturday"
# if day == "Saturday" or day == "Sunday":
#     print("It's the weekend!")      
# else:
#     print("It's a weekday.")    

# Excersice BMI Calculator


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in centimeters: "))
BMI = weight / ((height/100) ** 2)

if BMI < 18.5:
    category = "Underweight"    
elif 18.5 <= BMI < 24.9:
    category = "Normal weight"
elif 25 <= BMI < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

print(f"Your BMI is: {BMI:.4f}")
print(f"Your BMI category is: {category}")

