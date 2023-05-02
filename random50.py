import random

for i in range(50):
    if i < 10:
        # Generate a number outside the range
        num = random.randint(-100, -1)
    elif i < 15:
        # Generate a number between 100 and 150
        num = random.randint(100, 300)
    else:
        # Generate a number between 0 and 100
        num = random.randint(0, 100)
    print(num)
