import random
import math
playing=True
print("This is a number guessing game.")
print("Guess the number to win.")
lucky_num=str(random.randint(0,9))
while playing:
    user_number=(input("Your Guess:"))
    if user_number==lucky_num:
        print(f"Congratulations you found the number which was {lucky_num}")
        break
    else:
        print("Sorry try again.")
print("The floor and celling value of 19.09 are:"+ str(math.ceil(19.09))+","+ str(math.floor(19.09)))
x=9
y=-12
print("The value of x after copying the sign from y is"+ str(math.copysign(x,y)))
print("Absolute value of -37 and 78 are:"+ str(math.fabs(-37))+","+ str(math.fabs(78)))
print("GCD of 92 and 86 is:"+ str(math.gcd(24,56)))