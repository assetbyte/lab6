#1

arr = [1,2,3,4]
result = 1
for i in arr:
    result*=i
print(result)

#2

string = input()
upper = sum(1 for i in string if i.isupper())
lower = sum(1 for i in string if i.islower())
print(upper, lower)

#3

some_str = input()
length = len(some_str)
for i in range (length):
    if some_str[i] != some_str[length-i-1]:
        print("Not a palindrome")
        break
else:
    print("Palindrome")
    
#4

import time
import math
def delayed(number, delay):
    time.sleep(delay / 1000)  
    print(f"Square root of {number} after {delay} milliseconds is {math.sqrt(number)}")

delayed(25100, 2123)

#5

a = (True, True, True)
for i in a:
    if i == False:
        print("False")
        break
else:
    print("All are True")