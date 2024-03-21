# Exercise 3
# Your solution comes here

num_seconds = int(input())
hours = num_seconds // 3600 % 24
minutes = (num_seconds % 3600) // 60
seconds = (num_seconds % 3600) % 60
print(f"{hours}:{minutes:02d}:{seconds:02d}")