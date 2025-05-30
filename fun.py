#!/usr/bin/env python3
from random import randint

#secret = 6
secret = randint(1, 10)
diff = secret
num = input("Please guess a number: ")
num = int(num)
count=0

while num != secret:
    temp = secret - num
    if abs(temp - diff) > 1:
        if count == 0:
            num = int(input("Sorry please try again: "))
        elif count !=0:
            num = int(input("Sorry, but you're getting colder: "))
    else:
        if count == 0:
            num = int(input("Sorry please try again: "))
        elif count !=0:
            num = int(input("Sorry, you're getting warmer: "))
    diff = temp
    count = count+1

print('Congratulation~!')
#if num == secret:
#    print('Congratulations you win!')
#else: 
#    print("Sorry, not correct.")


#while num != secret:
#    temp = secret - num
#    if abs(temp - diff) > 1:
#        num = int(input("Sorry, but you're getting colder: "))
#    else:
#        num = int(input("Sorry, you're getting warmer: "))
#    diff = temp
