# TASK ONE
# Numbers and Variables

# 1. Create three variables in a single line and assign values to them
# in such a mannar that each one of them belongs to different data type.

a, b, c = 1, 2.01, 'vraj'
print(a, b, c)

# 2. Create a variable of type complex and swap it with another variable of type integer.


d = 1 + 2j
e = 3

d, e = e, d
print(d, e)

# 3. Swap two numbers using a third variable and do the same task without using any third variable.
# using third variable to swap. here we are using temp variable.
f, g = 2, 3
temp = f
f = g
g = temp
print(f, g)
# without using third variable swapping two variables
h = 2
i = 3

# using Addition and subtraction method to swap
h = h + i
i = h - i
h = h - i
# here h = 3 and i = 2 after swapping
print(h, i)

# using Multiplication and division method
# here we have h = 3 and i = 2 after getting swapped from first method.

h = h * i
i = h / i
h = h / i
# here h = 2 and i = 3 after swapping
print(h, i)

# 4. write a program that takes input from the user and print it using both Python 2.x and Python 3.x version.

# python 2.x version for printing user input
# txt = raw_input("Enter input for Python version 2.x")
# print "output in python 2.x version is = ", txt

# python3.x version for printing user input
txt1 = input("Enter input for Python 3.x")
print("out in python 3.x version is = ", txt1)

# 5. Ask users to enter any two numbers in between 1 - 10, add the two numbers and keep the sum
# in another variable called z. Add 30 to z and store the output in variable result and print result
# as the final output.

num1 = input(" Enter First number :")
num2 = input(" Enter second number :")
# Addition of numbers and string them in variable z
z = int(num1) + int(num2)
# Adding 30 to z and stoing in result variable
result = z + 30
print(result)


# 6. write a program to check the data type of the entered values.
# HINT: Printed output should say - the data type of input values

def isint(var):
    try:
        int(var)
        return True
    except:
        return False


def isfloat(var):
    try:
        float(var)
        return True
    except:
        return False


def isString(var):
    try:
        type(var) == str
        return True
    except:
        return False


def main():
    while True:
        v = input("Enter Number to check DataType: ")
        if isint(v):
            print("Entered Variable is integer")
            break
        elif isfloat(v):
            print("Entered variable is Float DataType")
            break
        elif isString(v):
            print("Entered variable is String DataType")


main()


# 7. Create Variable using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE
# Camel case
def camelCase(st):
    output = ''.join(x for x in st.title() if x.isalnum())
    return output[0].lower() + output[1:]


# snake Case
def change_case(st):
    res = [str[0].lower()]
    for c in str[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)

    return ''.join(res)


st1 = input("enter string")
camelCase(st1)
change_case(st1)



# 8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
# again. Will it change the value? If Yes then Why?
#answer: - yes we can assign in Python regardless to its current value.
#  Variable are essentially like an empty box, that can contains something
# like a String number ot other value. when we assign it a value, the box will contain that value
# and when we reassign it, it will empty out old value, and the new value will be placed inside of it.

# first we storing String data type in this variable

var1 = "hello"
print(var1)

# now reassigning with integer data type
var1 = 123
print(var1)