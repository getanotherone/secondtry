import random

bullets = [0 for i in range(6)]
bullets[0] = 1

a = input(("Введи 1 для начала игры и 0 для окончания: "))

while a != "0":
    if random.choice(bullets) == 0:
        print("Победа!")
    else:
        print("Поражение...")
    a = input(("Если по какой-то причине тебе понравилась игра, введи 1 для начала игры и 0 для окончания: "))