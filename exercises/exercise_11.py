# Exercise 11
# Your solution comes here

total_goods = int(input())
notes_500 = 0
notes_100 = 0
notes_10 = 0
notes_5 = 0
notes_2 = 0
notes_1 = 0

while total_goods >= 500:
	total_goods = total_goods - 500
	print(total_goods)
	notes_500 =+ 1

while total_goods >= 100:
	total_goods = total_goods - 100
	notes_100 += 1

while total_goods >= 10:
	total_goods = total_goods - 10
	notes_10 += 1

while total_goods >= 5:
	total_goods = total_goods - 5
	notes_5 += 1

while total_goods >= 2:
	total_goods = total_goods - 2
	notes_2 += 1

while total_goods >= 1:
	total_goods = total_goods - 1
	notes_1 += 1

print (notes_500, "(500)", notes_100, "(100)", notes_10,"(10)", notes_5,"(5)", notes_2,"(2)", "(1)", notes_1)
