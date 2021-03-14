# Task 3
# Data Structures
# 1. Create a list of 10 elements of four different data types like int, string, complex and float.
MixedList = [2, 3, 5.50, "StringDataType", 1 + 2j]
print(MixedList)

# 2. Create a list of size 5 and execute the slicing structure

SlicedList = [10, 20, 30, 40, 50]
# Slicing all elements of List
print(SlicedList[::])
# Slicing list from 1 to 3
print(SlicedList[1:3])


# 3. write a program to get the sum and multiply of all the items in giver list
def multiList(l):
    result = 1
    for x in l:
        result = result * x
    return result


def sumList(l, size):
    if (size == 0):
        return 0
    else:
        return l[size - 1] + sumList(l, size - 1)


list1 = [1, 2, 3, 4, 5, 6]
print("Multiply of List is: ", multiList(list1))
print("Sum of List is: ", sumList(list1, len(list1)))

# 4. Find the largest and smallest number from a given list.
list2 = [11, 5, 8, 22, 35, 37, 19, 29, 20, 15]
print("List :", list2)
print("Largest element in the list is: ", max(list2))
print("Smallest element in the list is: ", min(list2))

# 5. Create a new list which contains the specified numbers after removing the even
# numbers from a predefined list.

# we are using above list "list2" for this question
print("List with both even and odd numbers:", list2)
list3 = []
for x in list2:
    if x % 2 != 0:
        list3.append(x)

print("List after removing even numbers:", list3)


# 6. Create a list of elements such that it contains the squares of the first
# and last 5 elements between 1 and 30 (both included).

def squ():
    l = list()
    for i in range(1, 31):
        l.append(i ** 2)
    print("Square of first five elements:", l[:5])
    print("Square of last five elements:", l[-5:])


print("square of first and last 5 elements of list")
squ()

# 7. Write a program to replace the last element in a list with another list.
# Sample input: [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
l1 = [1, 3, 5, 7, 9, 10]
l2 = [2, 4, 6, 8]
l1[-1:] = l2
print("Final List after replacing last element of first list: ", l1)

# 8 Create a new dictionary by concatenating the following two dictionaries
# Sample input: a = {1:10, 2:20} b = {3:30, 4:40}
# Expected output: {1:10, 2:20, 3:30, 4:40}
a = {1: 10, 2: 20}
b = {3: 30, 4: 40}
d = {}
print("Dictionary a:", a)
print("Dictionary b:", b)
for i in (a, b): d.update(i)
print("Final Concatenated dictionary c:", d)

# 9. Create a dictionary that contain numbers in the form(x:x*x) where x takes
# all the values between 1 and n(both 1 and n included).
# Sample input: n = 5
# Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}

n = int(input("Enter Dictionary value: "))
dict1 = {}
for i in range(1, n + 1):
    dict1[i] = i * i

print("Final dictionary in the form(x:x*x) = ", dict1)

# 10. Write a program which accepts a sequence of comma-separated numbers from
# console and generates a list and a tuple which contains every number in the form of string.
# Sample input: 34, 67, 55, 33, 12, 98
# Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)

val = input("enter values with comma separated:")
l3 = val.split(",")
t1 = tuple(l3)
print("values in List : ", l3)
print("values in tuples:", t1)
