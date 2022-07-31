# q1:

# ineuron
# ineuron ineuron
# ineuron ineuron ineuron
# ineuron ineuron ineuron ineuron#

n = 4

for i in range(n):

    for j in range(0, i + 1):
        print("ineuron", end=" ")
    print("\n")

# Q2:


# ineuron
# ineuron      ineuron
# ineuron   ineuron    ineuron
#   ineuron     ineuron
#         ineuron



 # Q3: Try to extract all the list entity

        for i in l:
            if type(i) == list:
                print(i)

#Q4: Try to extract all the list entities

for i in l:
    if type(i)==dict:
        print(i)


#Q5: Try to extract all the tuple entities

for i in l:
    if type(i)==tuple:
        print(i)

# Q7: Try to give summation for all the numeric data


l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 45, 4, 4, 5, 45, 45, 4, 5]),
     {"k1": "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data Science "]]

sum = 0
for i in l:

    if type(i) == list or type(i) == set or type(i) == tuple or type(i) == dict:
        if type(i) == dict:

            for j in i.items():

                for k in j:

                    if type(k) == int:
                        sum += k
                        print(k)
        else:
            for j in i:
                if type(j) == int:
                    sum += j
                    print(j)

print("Sum: ", sum)

# Q8 :Try to filter out all the odd values out all numberic data which is a part of a list

l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 45, 4, 4, 5, 45, 45, 4, 5]),
     {"k1": "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data Science "]]

for i in l:

    if type(i) == list or type(i) == set or type(i) == tuple or type(i) == dict:

        if type(i) == dict:

            for j in i.items():

                for k in j:

                    if type(k) == int and k % 2 != 0:
                        print(k)
        else:

            for j in i:
                if type(j) == int and j % 2 != 0:
                    print(j)


#Q9: Try to extract "ineuron" out of this data

for i in l:
    if type(i) == dict:
        for j in i :
            if i[j] == "ineuron" :
                print(i[j])

# Q10: Try to find out a number of occurences of all the data

l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 45, 4, 4, 5, 45, 45, 4, 5]),
     {"k1": "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data Science "]]

dCount = {}

for i in l:
    if type(i) == dict:
        for j in i.items():
            for k in j:
                if k in dCount:
                    dCount[k] += 1
                else:
                    dCount[k] = 1

    else:
        for j in i:
            if j in dCount:
                dCount[j] += 1
            else:
                dCount[j] = 1

print(dCount)

# Q11: Try to find out number of keys in dict element

l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 45, 4, 4, 5, 45, 45, 4, 5]),
     {"k1": "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data Science "]]

count = 0
for i in l:
    if type(i) == dict:
        for j in i.keys():
            count += 1
print(count)

# Q12 : try to filter out all the string data

l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 45, 4, 4, 5, 45, 45, 4, 5]),
     {"k1": "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data Science "]]

for i in l:
    for j in i:

        if type(j) == str:
            print(j)

# Q13 : to find out alphanum in data

l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 45, 4, 4, 5, 45, 45, 4, 5]),
     {"k1": "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data Science "]]

for i in l:
    if type(i) == dict:
        for j in i.items():
            for k in j:
                if type(k) == str:
                    for x in k:
                        if x.isdigit():
                            print(k)

    else:
        for j in i:
            if type(j) == str:
                for x in j:
                    if x.isdigit():
                        print(j)

# Q14 : to find out multiplication of all numeric value in the individual collection inside data set:

mul = 1
for i in l:

    if type(i) == list or type(i) == set or type(i) == tuple or type(i) == dict:
        if type(i) == dict:

            for j in i.items():

                for k in j:

                    if type(k) == int:
                        mul *= k
                        # print(k)
        else:
            for j in i:
                if type(j) == int:
                    mul *= j
                    # print(j)

print("mul: ", mul)

# Q15 : Try to unwrap all the collection inside a collection and create a flat list :


l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 45, 4, 4, 5, 45, 45, 4, 5]),
     {"k1": "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data Science "]]

items = []
for i in l:
    if type(i) == dict:
        for j in i.items():
            for k in j:
                items.append(k)

    else:
        for j in i:
            items.append(j)

print(items)


# 1. Write a Python Program to Find LCM?

def lcm(a, b):
    if a > b:
        max = a
    else:
        max = b
    while True:
        if max % a == 0 and max % b == 0:
            print("the lcm of {} and {} is {}".format(a, b, max))
            break
        max = max + 1

lcm(5,9)



