# Exercise 1
# Your solution comes here

#get a 5 digit number from the user
number = int(input("Enter a five-digit number:"))

#first number is the sum of the first, third, and fifth digit
first_number = (number // 10000) + (number // 100 % 10) + (number % 10)

#second number is the sum of the second and fourth digit
second_number = (number // 1000 % 10) + (number // 10 % 10)

print(str(first_number) + str(second_number))