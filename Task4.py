# Task 4
# Traditional Functions, Anonymous function and Higher order Functions

# 1. Write a program to reverse a string.
# Sample input: "1234abcd"
# Expected output: “dcba4321”
from typing import Any, Iterator, List
import functools
import operator


def reverse(st):
    if len(st) == 0:
        return st
    else:
        return reverse(st[1:]) + st[0]


s = "1234abcd"
print("\n Original string :", s)
print("\n Reversed string :", reverse(s))


# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
# letters.
# Sample input: “abcSdefPghijQkl”
# Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12


def uplow(string):
    up = 0
    low = 0
    for i in string:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
        else:
            pass

    print("\n No. of Uppercase characters:", up)
    print("\n No. of Lowercase characters:", low)


st1 = "abcSdefPghijQkl"
print("\n Original String :", st1)
uplow(st1)


# 3. Create a function that takes a list and returns a new list with unique elements of the first list.
# here list will remove repeating elements of list and give unique output

def unique(l):
    x = []
    for i in l:
        if i not in x:
            x.append(i)
    return x


list1 = [1, 1, 1, 2, 2, 5, 0, 0, 8, 9, 9, 10]
print("\n Original List with repeating values:", list1)
print("\n List with all Unique values:", unique(list1))


# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.

def hyphen(items):
    values = items.split('-')
    values.sort()
    print('-'.join(values))


i = 'vraj-patel-consultadd-test'
print("\n Sequence of words with hyphen separated", i)
print("\n alphabetically sorted with hyphen separated")
hyphen(i)

# 5. Write a program that accepts a sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.
# Sample input: Hello world Practice makes man perfect
# Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT
a = input("enter lines to make it in upper case characters")
string1 = a.upper()
print("\n Origianl sentence ", a)
print(" Sentence in uppercase", string1)


# 6. Define a function that can receive two integral numbers in string form and compute their sum and
# print it in the console.
def calsum(a, b):
    s = int(a) + int(b)
    return s


# input will be in string form as input() takes values in string format
num1 = input("enter first value:")
num2 = input("enter second value:")
total = calsum(num1, num2)
print("Sum of two values :", total)


# 7. Define a function that can accept two strings as input and print the string with the maximum length
# in the console. If two strings have the same length, then the function should print both the strings line
# by line.

def length_of_string(str1, str2):
    if (len(str1) == len(str2)):
        print(str1)
        print(str2)

    elif (len(str1) < len(str2)):
        print(str2)

    else:
        print(str1)


stri1 = input(str("enter First String: "))
stri2 = input(str("enter Second String: "))

print("\n")

length_of_string(stri1, stri2)


# 8. Define a function which can generate and print a tuple where the values are square of numbers
# between 1 and 20 (both 1 and 20 included).
def squreTuple():
    l1 = [i ** 2 for i in range(1, 21)]
    print(tuple(l1))


print("Square number between 1 to 20 in tuple", squreTuple())


# 9. Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers.
# Sample input: show Numbers(3) (where limit=3)
# Expected output:
#   0 EVEN
#   1 ODD
#   2 EVEN
#   3 ODD

def showNumbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            print(i, end="")
            print("EVEN")
        else:
            print(i, end="")
            print("ODD")


showNumbers(3)

# 10. Write a program which uses filter() to make a list whose elements are even numbers between 1
# and 20 (both included)
list2 = range(1, 21)

eve_num = filter(lambda x: x % 2 == 0, list2)
print(list(eve_num))

# 11. Write a program which uses map() and filter() to make a list whose elements are squares of even
# numbers in [1,2,3,4,5,6,7,8,9,10].

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

eve_num1 = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, list3))

print(eve_num1)


# 12. Write a function to compute 5/0 and use try/except to catch the exceptions

def divide():
    return 5 / 0


try:
    divide()
except ZeroDivisionError as z:
    print("number is divided by Zero")
except:
    print("any other exception")

# 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().

list4 = [1, 2, 3, 4, 5, 6, 7]
list_flat = functools.reduce(operator.iconcat, list4, str)

print("Original List", list4)
print("Flattened List", list_flat)


# 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.

def div(n):
    for i in n:
        if (i % 3 != 0) & (i % 7 == 0):
            return i


list5 = range(1, 101)
res = list(map(div, list5))
print(res)


# 15. Write a program in Python to multiply the elements of a list by itself using a traditional function
# and pass the function to map() to complete the operation.

def squ(x):
    return x * x


num3 = [1, 2, 3, 4, 5]
num_squ = list(map(squ,num3))
print(num_squ)

#16. What is the output of the following codes:
# (i) def foo():
#      try:
#           return 1
#       finally:
#              return 2
#       k = foo()
#       print(k)

# it will retrun 2 because the finally block executes even there is a return statement in try block

# (ii) def a():
#       try:
#           f(x, 4)
#       finally:
#           print('after f')
#       print('after f?')
#       a()

# it will be "C" this function will throw erroe because "f" is not defined.
