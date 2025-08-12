# def hloprint():
#     print("Hello Name")

# hloprint()
# hloprint()
# hloprint()
# hloprint()
# hloprint()
# hloprint()


# def hloname(name):
#     print("your name is", name)

# hloname("Mohan")
# hloname("Shahi")
# hloname("Ram")
# hloname("shahi")


# def hello(roll_no):
#     print ("your roll no is ",roll_no)
# hello("one")
# hello("two")
# hello("three")
# hello("four")
# hello("five")


# def multiply(a,b,c):
#     multiplyhehe=a*b*c
#     print("the mutiplication is",multiplyhehe)
# multiply(2,3,4)


# def add(a,b):
#     x=a+b
#     print("the addition is",x)
# def sub(a,b):
#     x=a-b
#     print("the subtract is",x)
# def multiply(a,b):
#     x=a*b
# def divide(a,b):
#     if(b==0):
#         print("the value cannot be divided")
#     else:
#         x=a/b
#     print("the division is",x)
# choice = input ("which calculation do you wanna do :")
# num1 = float(input("enter the first number:"))
# num2 = float(input("enter the second numver: "))
# if choice =="add":
#     add(num1,num2)
# elif choice=="sub":
#     sub(num1,num2)
# elif choice=="multiply":
#     multiply(num1,num2)
# elif choice =="divide":
#     divide(num1,num2)
# else:
#     print("invalid input")


def login():
    usernameinput = input("enter the username :")
    userpassinput = input("enter passwrod :")
def signup():
    usergmail = input ("entre your gmail :")
    userinput = input ("enter your new password :")
    userpassword = input ("enter your new password :")
print("Enter Login for loging in to account : ")
print ("enter signup for signing up : ")
while True:
    userchoice = (input("enter your choice : "))
    if userchoice == "Login":
     login()
    elif userchoice == "Signup":
     signup()
     break
    else:
     print ("Terminate loop")