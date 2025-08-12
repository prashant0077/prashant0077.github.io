
# def divide(num1,num2):
#     # if(num2==0):
#     #     print("the value cannot be divided")
#     # else:
#     #  result=num1/num2
#     result = num1/num2
#     print("the division is",result)
# num1 = float(input("enter first number"))
# num2 = float(input ("enter second number"))
# divide(num1,num2)


# try:
#     num1 = int(input("enter first number"))
#     num2 = int(input("enter second number"))
#     result = num1-num2
#     print(result)
# except ZeroDivisionError:
#     print("Can not divide by zero")
# except ValueError:
#     print("Please enter number")



# try:
#     num1 = float (input("enter the first number"))
#     num2 =float (input("enter the second number"))
#     result = num1*num2
#     print(result)
# except ZeroDivisionError:
#     print("0 value mildaina k input maa")
# except ValueError:
#     print("number nai raknu parxa houuu ")


# try:
#   a = float (input("enter the  first number"))
#   b = float(input("enter the second number"))
#   result = a*b
#   print (result)
# except ZeroDivisionError:
#     print("0 value is invalid")
# except TypeError:
#     print("number needed")




# try:
#     a = float(input("Enter the first number: "))
#     b = float(input("Enter the second number: "))
#     result = a * b
#     print("Result:", result)

# except ValueError:
#     print("Please enter valid numbers.")
# except ZeroDivisionError:
#     print("Zero value is invalid.")
# except TypeError:
#     print("A type error occurred.")

# try:
#     num1 = int(input("enter one number"))
#     num2 = int(input("enter anotehr number"))
#     result = num1+num2
# except Exception as e:
#     print("The Error Occurs", e)

try:
    a = int(input("enter your choice"))
    if a==0:
        raise ZeroDivisionError("The is anotehr")
    print("You entered", a)
except Exception as e:
    print("Error",e)