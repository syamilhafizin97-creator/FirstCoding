# # Loop

# for i in range(5):      # Loop 0 1 2 3 4
#     print(i)

# for i in range(2, 7):   # Loop 2 3 4 5 6
#     print(i)        

# for i in range(11, 1, -1):  
#     print(i)    
  

# # while loop

# count = 0
# while count < 5:
#     print(count)
#     count += 1

# loop control statements

# for i in range(5,25):
#     if i in [5, 10, 15]:
#         continue
#     if i == 20:
#         break
#     print(i)

# #nested loop
# for i in range(3):
#     for j in range(2):
#         print(f"({i}, {j})")

# Create a multiplication table generator

# first_number = int(input("Enter a number: ")) 
# second_number = int(input("Enter another number: "))    

# for i in range(0, second_number + 1):
#     result = first_number * i
#     print(f"{first_number} x {i} = {result}")       

# Write a program that find all prime numbers up to a given number

limit = 20

for num in range(0, limit + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number")