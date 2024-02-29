# Exercise 9
# Your solution comes here

hours = int(input())
minutes = int(input())
seconds = int(input())

degrees_hours = hours * 30
degrees_minutes = minutes * 0.5
degrees_seconds = seconds * 0.0083333

total_degrees = degrees_hours + degrees_minutes + degrees_seconds
print(total_degrees,"degrees")