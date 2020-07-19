##########################################################################################
# Example 2:
# 
# Given a random variable x, where x is an interger and 0 <= x <= 100, please follows the rules:
# 1. If x < 50, please print out "You lose!"
# 2. If 55 < x < 80, please print out "You won the third prize!"
# 3. If x = 83, 89, 97, please print out "You won the first prize!!!"
# 4. Else, please print out "You won the second prize!!"
#  
##########################################################################################
import random

x = random.randint(0, 100)
print(f'x = {x}')

if x < 50:
    print("You lose!")
elif 60 < x < 80:
    print("You won the second prize!!")
elif x == 83 or x == 89 or x == 97:
    print("You won the first prize!!!")
else:
    print("You won the third prize!")

