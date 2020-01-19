# If no arguments are provided, the function should return a random integer between 0 and 100.
# If only a max number is provided, the function should return a random integer between 0 and the max number.
# If only a min number is provided, the function should return a random integer between the min number and 100
# If both a min and max number are provided, the function should return a random integer between those 2 values.
# BONUS: account for any edge cases (eg. min > max, max < 0)


import random
def randInt(min=0 , max=100):
    if min > max:
        print("Min cant be greated then Max or vice versa")
        return
    num = random.randrange(min, max)
    return num

print(randInt(min=5, max=10))