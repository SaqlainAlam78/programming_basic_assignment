# q1 : Try to print a prime number in between 1 to 1000


for num in range(1, 1000):

    for i in range(2, num):

        if (num % i == 0):
            break
    else:

        print(num)


# q2 : Try to write a function which  is equivalent  to print function in python


def print_(*arg):
    '''
    Prints the values
    '''

    print(*arg)


# q3 : Try to write a function which is a replica of list append , extend and pop function

# append

def append_():
    '''append objects to the end of list'''

    a = []
    b = []

    a = list(map(int, input().split(',')))
    b = list(map(int, input().split(',')))

    sum = a + b

    return ([sum])


print(append_())


# extend

def extend_():
    '''append objects to the end of list'''

    a = []
    b = []

    a = list(map(int, input().split(',')))
    b = list(map(int, input().split(',')))

    sum = a + b

    return ([sum])


print(extend_())


# pop

def pop_():
    l = [1, 2, 3, 4, 5, 6]
    l1 = []
    n = int(input("Enter the item you want to pop"))
    for i in range(len(l)):
        if l[i] != n:
            l1.append(l[i])
    return l1


print(pop_())

#q4 : Try to write a lambda function which can return a concatination of all the string that we will pass


n = lambda str1,str2 : str1 + str2


#q5 : Try to write a lambda function which can return list of square of all the data between 1-100

n = lambda : [i * i for i in range(1,101)]

# q6 : Try to write a 10 Different example of lambda function with a choice of your taks


#1

add = lambda x, y: x + y

#2
sub = lambda x, y: x - y

#3
mul = lambda x, y: x * y

#4

div = lambda x, y: x / y

#5
rem = lambda x, y: x % y

#6
sq = lambda x: x * x

#7
cube = lambda x: x * x *x

#8
x = [1,2,58,6,1,84,3,5]
filtered_result = filter (lambda x: x > 4, x)

#9

s = input("enter your data")
lambda s : s.lower()
print(s)

#10

s = input("enter your data")
lambda s : s.upper()
print(s)

# q7 : Try to write a funtion which can perform a read operation from .txt file

def read_() :
    my_file = open(C/Documents/Python/test.txt, r)
    print(my_file.read())