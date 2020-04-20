import random
number = random.randint(1, 10)
for i in range(10):
    playernumber = int(input())
    if playernumber == number:
        print("win")
    else:
        print("lose")
print("that's all folks")