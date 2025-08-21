"""
assignment 3 count down app
Count down:
I have a bomb that I want to detonate at Aptech but I dont want to be caught in the blast 

Help me design and develop a countdown timer that counts down from 10 to 1
"""

import time 

count = 10  

while count >= 1:
    print(count)
    time.sleep(1) 
    count = count - 1

print("Boom! Countdown finished you are dead GOODBYE.")
