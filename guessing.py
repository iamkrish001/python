# guess game
import random
ranint = random.randint(1, 100)

num = int(input("enter a number between 1 and 100   "))
if (num == ranint):
 print("congratulations , you have won ")
else:
    while num != ranint:
        if num < ranint:
            num = int(input("enter a greater number than" + str(num)+ "= "))

        else:
            num = int(input("enter a smaller number than" + str(num)+ "= "))
    if (num == ranint):
        print("congratulations , you have won ")
