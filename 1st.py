from numpy import var


print("new one")
patient_name  = "john smith"
patient_bed_no = 12 
print(patient_bed_no , patient_name) 
name = input("what's the name of new patient? ")
print("my name is " + name)

# calculating the age 
person_age = input("what's is your birth year?")
age = 2022 - int(person_age)
print("the age of the person is " , age)

#addtion 
first = input("enter the first number ")
second = input("enter the second number")
sum = int(first) + int(second)
print ( sum)

string = ' hello'
print (string.replace('e' , '3'))