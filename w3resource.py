#Write a Python program to get the Python version you are using

import sys

print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

#Write a Python program to display the current date and time.

import datetime

now = datetime.datetime.now()
print("Current date time : ")
print(now.strftime("%Y-%M-%D %H:%M:%S"))

#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them

a = input("Enter your first name : ")
b = input("Enter your last name : ")

print(b + " "+ a)

# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

a = input("Enter comma seperated numbers")

li = a.split(",")
tu = tuple(li)

print(li)
print(tu)

#Write a Python program to accept a filename from the user and print the extension of that

filename = input("Enter a filename")

f_extns = filename.split(".")

print("The extension of the file is : " + repr(f_extns[-1]))


#Write a Python program to display the examination schedule.

examination_date=(11,5,2022)

print("the exam will start from : %i/%i/%i" %examination_date )

#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

a = int(input('Enter a number'))

n1 = int("%s" % a)

n2 = int("%s%s" % (a, a))

n3 = int("%s%s%s" % (a, a, a))

print(n1 + n2 + n3)








