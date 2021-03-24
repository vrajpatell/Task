# Task 5
# File Handling and Exception Handling

import sys


# 1. Write a program in Python to allow the error of syntax to be handled using exception handling.
# Use SyntaxError
def fun1(n):
    try:
        eval('n***2')
    except SyntaxError:
        print("Syntax Error")


n = print("enter value")
fun1(n)

# 2. Write a program in Python to allow the user to open a file by using the argv module. If the
# entered name is incorrect throw an exception and ask them to enter the name again. Make sure
# to use read only mode.

# try:
#   with open(sys.argv[1], 'r') as file1:
#      print(file1.read())
# except FileNotFoundError:
#   print("Enter Valid name of File")

# 3. Write a program to handle an error if the user entered a number more than four digits it should
# return “The length is too short/long !!! Please provide only four digits”

while True:
    try:
        num1 = input("enter number")
        if (len(num1) == 4):
            print("enter number is four digit only")
            break
    except ValueError:
        print("Enter number with only four digits")

# 4. Create a login page backend to ask users to enter the username and password. Make sure to
# ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
# should not be more than 3 times.

print("Enter username and password")
count = 0
while count < 4:
    try:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if password == "Pass123" and username == "admin123":
            print("Logged In")
            break
        else:
            count += 1
            raise Exception

    except Exception:
        print("Please try again")

# 6. Read doc.txt file using Python File handling concept and return only the even length string from
# the file. Consider the content of doc.txt as given below:
# Hello I am a file
# Where you need to return the data string
# Which is of even length
# Make sure you return the content in The same link as it is present.

print('reading characters of files')
char_list = []
with open('demo.txt', "r") as f:
    for line in f:
        char_list.extend(line.split())

# print(char_list)
store_char = []


def evenLenght(s):
    for word in s:
        if len(word) % 2 == 0:
            store_char.append(word)


evenLenght(char_list)
print(store_char)

with open('evenDemo.txt', 'w') as file1:
    for listitem in store_char:
        file1.write('%s\n' % listitem)

file1 = open('evenDemo.txt', 'r')
print(file1.read())
file1.close()
