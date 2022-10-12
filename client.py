import math
import random
import socket
import threading
import sys
#use localhost info
primes_file = open("primes.txt", "r")
primes = primes_file.read().split()


commands = [""]

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def select_prime():
    random.shuffle(primes)
    
def send_message(message, to):
    

private_key = -1

while(True):
    received_command = input("Enter Command: ")
    switch(received_command):
        case "QUIT":
            break
    break