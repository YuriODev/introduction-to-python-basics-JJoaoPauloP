# Exercise 4
# Your solution comes here

number = int(input())

number_1 = number // 1000
number_2 = number // 100 % 10
number_3 = number // 10 % 10
number_4 = number % 10

result = (number_1 == number_4) * (number_2 == number_3)
print(result)