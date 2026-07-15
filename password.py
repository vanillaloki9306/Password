IQ = 0
points = 0
point1 = False

question1 = input("If someone owns a piece of land, do they own it all the way to the center of the earth? ")

if question1 == "No":
    point1 = True
else:
    print("Wrong")
point2 = False

question2 = input("If humans evolved from apes or chimps, why are the chimps and apes still here?")

if question2 == "They aren't":
    point2 = True
else:
    print("Wrong")
point3 = False

question3 = input("If marbles are not made of marble, why are they called marbles?")

if question3 == "marble haha is funy":
    point3 = True
else:
    print("wrong")

if point1 == False:
   IQ = "40"
if point1 == True and point2 == False:
   IQ = "60"
if point1 == True and point2 == True:
    IQ = "80"
if point1 == True and point2 == True and point3 == True:
    IQ = "100"

print("calculating iq...")
import time
for i in range(0,10):
    time.sleep(1)
    print("loading...")

time.sleep(1)

import random


def random_number():
    randNum = random.randint(1,30)
    print(randNum + int(IQ))
random_number()

time.sleep(10)


