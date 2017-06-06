import random

print("Please enter a comma-seperated list of options: ")
choices = input().split(",")
random.seed(None)
value = random.randint(0,len(choices)-1)
print(choices[value].strip())
