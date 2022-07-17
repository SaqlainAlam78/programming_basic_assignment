#Q1 : Try to print this by using while loop

#*
#* *
#* * *
#* * * *
#* * * * *
#* * * * * *
#* * * * * * *
#* * * * * * * *
#* * * * * * * * *

n = 9
i = 1
while i <= n :
    j = 1
    while j <= i:
        print("*", end = " ")
        j = j + 1
    print()
    i = i + 1


#q3 : Try to print all the number divisible by 3 in between a range of 40 - 400


i = 40

while i < 401:
    if i % 3 == 0 :
        print(i)
    i=i+1

# Q4 : Try to filter out all the vowels form below text by using while loop :

str = ("""Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[36]""")

i = 0

while i < len(str):

    if str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u':
        print(str[i])
    i = i + 1



#q5 : Try to generate all the even number between 1- 1000



i = 1

while i < 1001:
    if i % 3 == 0 :
        print(i)
    i=i+1


# q9 : Write a code to send a mail to your friend

def email():
    a = """Hi Rajesh,
                       Hope You are doing well
             Thanks & Regards,

             Saqlain ALam"""
    print(a)


# q14 : you have to write a fun which will take string and return a len of
# it without using a inbuilt fun len

def length():
    l = 1

    n = input(" Enter a string ")

    for i in n:
        l += 1
        n += i

    return l


# q15 :write a fun which will be able to print an index of all premitive element which you will pass

def index():
    n = input(" Enter your data ")

    for i in n:
        z = print("Index of : ", [i], "=", n.index(i))

    return (z)


# q16 : Write a fun which will take input as a dict and give me out as a list of all the values
# even in case of 2 level nesting it should work .

def diction():
    n = input(" Enter your input as a dict")

    z = list(n)

    print(z)


# q17 : write a function which will take multiple list as an input and give me concatnation of all the element as and output

def concat():
    lst = []
    n = int(input("Enter number of elements : "))

    for i in range(0, n):
        ele = [input(), int(input())]
        lst.append(ele)

        print(lst)

    return ()


























