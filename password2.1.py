IQ = 0
points = []
point1 = False

question1 = input("If someone owns a piece of land, do they own it all the way to the center of the earth? ")

if question1 == "No":
    point1 = True
    points.append(1)
else:
    print("Wrong")
point2 = False

question2 = input("If humans evolved from apes or chimps, why are the chimps and apes still here? ")

if question2 == "They aren't":
    point2 = True
    points.append(2)
else:
    print("Wrong")
point3 = False

question3 = input("If marbles are not made of marble, why are they called marbles? ")

if question3 == "marble haha is funy":
    point3 = True
    points.append(3)
else:
    print("wrong")

print(points)

if points == [1,2,3]:
    IQ = 100
elif points == [3] or [1,3]:
    IQ = 90
elif points == [2] or [1,2]:
    IQ = 80
elif points == [0] or [1] or []:
    IQ = 70

print("calculating iq...")
import time
for i in range(0,10):
    time.sleep(1)
    print("loading...")

time.sleep(1)

import random


def random_number():
    randNum = random.randint(0,30)
    print(randNum + int(IQ))
random_number()

time.sleep(10)


