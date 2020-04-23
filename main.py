import time
import random
from random import *
import string
start_time = 0 + 1
message = 'This process took ' + str(time.time() - start_time) + ' seconds to crack'
Guess = ""
password = input("Password: ")
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', string.ascii_letters, string.digits)

while Guess != password:
    Guess = ""
    for letter in password:
        Guessletter = letters[randint(0, 25)]
        Guess = str(Guessletter) + str(Guess)
        print(Guess)
print("password cracked")
print(message)
input("Press enter to exitS")
