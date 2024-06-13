import random

rand1 = random.randint(0, 10)
rand2 = random.randint(0, 10)
rand3 = random.randint(0, 10)

def add_vars():
    result = rand1+rand2+rand3
    print("rand1 is:",rand1)
    print("rand2 is:", rand2)
    print("rand3 is:", rand3)
    print("Result of rand1/2/3 is:",result)
    return result

