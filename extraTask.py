# Extra Task
# Data Structures
import sys

# 1. Create a list of given structure and get the Access list as provided below:
# x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# Access list: [1, 2, 3, 4]Access list: [600, 700]
# Access list: [100, 300, 500, 600, 800]
# Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
# Access list: [10]
# Access list: [ ]

x = [100, 200, 300, 400, 500, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 600, 700, 800]
l1 = [x[index] for index in [0, 2, 4, 6, 8]]

print("Access List:", x[5][0:4])
print("Access List:", x[-3:-1])
print("Access List:", l1)
print("Access List:", x[::-1])
print("Access List:", x[5][5][0])

# 2. Create a list of thousand numbers using range and xrange and see the difference between each
# other.
# (For reference:https://www.techbeamers.com/python-xrange-range/)

a = range(1, 1000)
# b = xrange(1, 1000)
#  In Python 3, there is no xrange ,
#  but the range function behaves like xrange in Python 2

print(type(a))
# print(type(b))

# 3. How Tuple is beneficial as compared to the list?
# Tuple execution can be faster then operations in list

# 4. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
# the number which is divisible by 3 and is a multiple of 2.
print("the number which is divisible by 3 and is a multiple of 2")
l2 = []
for i in range(1, 100):
    if ((i % 3 == 0) & (i % 2 == 0)):
        l2.append(i)

print(l2)


# 5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
# string with their index.

def rev_vowels(st):
    vowels = ""
    for c in st:
        if c in "aeiouAEIOU":
            vowels += c
    res_str = ""
    for c in st:
        if c in "aeiouAEIOU":
            res_str += vowels[-1]
            vowels = vowels[:-1]
        else:
            res_str += c
    return res_str


str1 = "USA"
st12 = "world"

print("not reversed string ", rev_vowels(st12))
print("Reversing vowels index: ", rev_vowels(str1))

# 6. Write a program in Python to iterate through the string “hello my name is abcde” and print the
# string which is having an even length.

s = input("enter string")


def eve_length(s):
    s = s.split(' ')
    for word in s:
        if len(word) % 2 == 0:
            print(word)


eve_length(s)

# 7. Write a program in python to print the pair of numbers whose sum is equal to the result
# number that is let's say 8.
# x=[1,2,3,4,5,6,7,8,9,-1]

z = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]


def sum_pair(arr, n, s):
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] == s):
                print("(", arr[i],
                      ",", arr[j],
                      ")", sep="")


n = len(z)

sum_pair(z, n, 8)

# 8. Write a program in Python to complete the following task:
# Create two lists such as even_list and odd_list
# Ask user to enter a number in the range of 1,50 and make sure if the entered number is
# even, append it to the even_list and if the entered number is odd append it to the odd_list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you enter all the 5 elements, calculate the sum of the list and return the
# maximum of the list.


lst = []
size_list = 10

for i in range(0, size_list):
    num = int(input("enter number between 0 and 50: "))
    if 0 <= num <= 50:
        lst.append(num)
    else:
        print("please enter again")

print(lst)


def even_odd(lsele):
    ev = []
    od = []
    count_even = 0
    count_odd = 0
    for k in lsele:
        if k % 2 == 0:
            if count_even <= 5:
                ev.append(k)
                count_even += 1
        elif count_odd <= 5:
            od.append(k)
            count_odd += 1
    print("even list:", ev)
    print("odd list", od)
    print("sum of even list", sum(ev))
    print("sum of odd list", sum(od))


even_odd(lst)

# 9. Write a program to find out the occurrence of a specific character from an alphanumeric string.
# Sample input: 12abcbacbaba344ab
# Expected output: a=5 b=5 c=2
# NOTE: Make sure to avoid counting the occurrence of numeric values in the string.

input_str = "12abcbacbaba344ab"
print("sample input for occurrence:", input_str)

out_str = {y: input_str.count(y) for y in set(input_str) if y.isalpha()}

print("Expected Output: \n" + str(out_str))


# 10. Generate and print another tuple whose values are even numbers in the given tuple
# (1,2,3,4,5,6,7,8,9,10).

tp = (1,2,3,4,5,6,7,8,9,10)
list1 = list()

for t in tp:
    if t%2 == 0:
        list1.append(t)
tp1 = tuple(list1)
print(tp1)