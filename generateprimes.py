import math
import random
import os


def check_prime(val):
    for i in range(2, int(math.sqrt(val)) + 1):
        if (val % i == 0):
            return False
    return True

def generate_prime(file):
    minVal = int("0xFFFFFFFF", 16)
    maxVal = int("0xFFFFFFFFFFFFFFFF", 16)
    for candidate in range(minVal, maxVal):
        if(check_prime(candidate)):
            file.write(str(candidate) + " ")

try:
    os.remove("primes.txt")
    file = open("primes.txt", "a")
except:
    file = open("primes.txt", "a")

generate_prime(file)
