# Task 6
# GENERATORS, LIST COMPREHENSION AND DECORATORS

# 1. Write a program in Python to find out the character in a string which is uppercase using list
# comprehension.

str1 = input(print("Enter string"))
print("Original string: ", str1)

res = [char for char in str1 if char.isupper()]

print("Upper case characters in String: ", res)

# 2. Write a program to construct a dictionary from the two lists containing the names of students and
# their corresponding subjects. The dictionary should map the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension.
# HINT - Use Zip function also
# Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
# Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}

students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']

dict1 = dict(zip(students, subjects))
print("Dictionary output using zip function")
print(dict1)


# 3. Learn More about Yield, next and Generators
#   1. yield and Generator
def yieldexample():
    yield 1
    yield 2


for value in yieldexample():
    print(value)

#   2. next
list1 = [1, 2, 3]
r1 = iter(list1)
print(next(r1))
print(next(r1))

# 4. Write a program in Python using generators to reverse the string.
# Input String = “Consultadd Training”

str2 = "Consultadd Training"

print("Original String: ", str2)


def revStr(st):
    length = len(st)
    for i in range(length - 1, -1, -1):
        yield st[i]


for ch in revStr(str2):
    print(ch)


# 5. Write an example on decorators.
def divide(func):
    def inner(a, b):
        if b == 0:
            print("enter valid numbers")
            return
        return func(a, b)

    return inner


@divide
def div(a, b):
    print(a / b)


i1 = int(input("Enter first number"))
i2 = int(input("Enter second Number"))

div(i1, i2)
