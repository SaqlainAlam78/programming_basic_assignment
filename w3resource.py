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

#Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).

print(abs.__doc__)

#Write a Python program to print the calendar of a given month and year.

import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))


#13. Write a Python program to print the following 'here document'.

print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")


#14. Write a Python program to calculate number of days between two dates

from datetime import date
l_date = date(2022, 8, 9)
f_date = date(2022, 8, 6)

number_of_days = l_date - f_date
print(number_of_days.days)

#15. Write a Python program to get the volume of a sphere with radius 6.

vol = (4/3)*(22/7)*6*6*6

#16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

def diff(n) :
    if n <= 17 :
        return(17 - n)
    else :
        return(n - 17)*2

# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum

a = int(input("Enter a number"))
b = int(input("Enter a number"))
c = int(input("Enter a number"))

if a == b == c :
    sum = a+b+c
    mul = 3 * sum
    print(mul)

#Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

g_string = input(" Enter a string ")

if 'Is' == g_string[0:2]:
    print(g_string)

else:
    print("Is " + g_string)

#Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def larger_string(str ,n) :
    result = ""
    for i in range(n):
        result = result + str
    return result


#Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

n = int(input("Enter a number"))
if n % 2 == 0 :
    print("number is even")
else :
    print("number is odd")


#Write a Python program to count the number 4 in a given list

li = [1,4,5,8,4,8,4,5,4,4]

count = 0
for i in li :
    if i == 4:
        count = count + 1
print("count of 4 is ", count)

#Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2

def larger_string(a ,n) :
    result = ""
    for i in range(n):
        if len(a) > 2:
            result = result + a[0:2]
        else :
            result = result + a
    return result


# Write a Python program to test whether a passed letter is a vowel or not

def check(char) :
    all_vowels = 'aeiou'
    return char in all_vowels

#Write a Python program to check whether a specified value is contained in a group of values.

def check_value(group_data , n) :
    for i in group_data :
        if i == n :
            return "Present"
    return "Absent"
#Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.


numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]

for x in numbers:
    if x == 237:
        print(x)
        break;
    elif x % 2 == 0:
        print(x)




























