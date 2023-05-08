print("Welcome to the quiz game!!!!!!")
print("INSTRUCTIONS:")
print("you'll get 2 questions and each question carries 1 point,\n the one with the higest points wins")
print("What is the longest river of the world?")
print("1.Nile 2.Amazon 3.Mississipi 4.Congo")
ans1 = input("enter your answer")
if ans1 == "1":
 print("Correct!!")
else:
 print("Incorrect")

print("which is the most beautiful country among the given options?")
print("1.Nepal 2.pakistan 3.Uzbekistan 4.afgnanistan")
ans2 = input("enter your answer")
if ans2=="1" :
 print("Correct!!")
else:
 print("Incorrect")

if ans1 == "1" and ans2=="1" :
    print("congratulations on your win") 
else :
    print("better luck next time")