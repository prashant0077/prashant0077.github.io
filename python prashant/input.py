# userinput = input("name raknuhos = ")
# id = input("id pani rakdinuna = ")
# password = input("la euta last password chai rakdinu = ")

# if (userinput !="dad"):
#     print ("userinput wrong")
# elif (id !="9841"):
#     print ("id wrong")
# elif (password !="hello"):
#     print ("password wrong")
# else:
#     print ("access granted")


# username = "Admin123"
# password = "Admin"

# userInput = input("Enter Your Username")
# UserPassword = input("Enter Your Password")

# if(userInput!=username):
#     print("Username Wrong")
# elif(UserPassword!=password):
#     print("Password Wrong")
# else:
#     print("Welcome")


# name = "Admin"

# print(f"Welcome {name}")


# username = "Prashant"
# password = "Cheap"
# idnumber = "9999"
# userinput = input("Enter your name = ")
# userpassword = input("Enter your password = ")
# idpass = input("Enter your id = ")
# if userinput != username :
#     print("The username you put is wrong.The name you put is ",userinput )
# elif userpassword != userpassword :
#     print(f"The password you put is wrong.The password you put is {userpassword}")
# elif idpass != idnumber :
#     print(f"The id you put is wrong.The id you put is {idpass} ")
# else:
#     print(f"Welcome {username}")


Userinput = input("Enter your country = ")
if Userinput == "Nepal":
    Userstateinput = input("enter your state")
    if Userstateinput == "koshi":
        print("your a citizen of Koshi")
    elif Userstateinput == "madesh":
        print("your a citizen of Madesh")
    elif Userstateinput == "bagmati":
        print("your a citizen of Bagmati")
    elif Userstateinput == "gandaki":
        print("your a citizen of Gandaki ")
    elif Userstateinput == "lumbini":
        print("your a citizen of Lumbini")
    elif Userstateinput == "karnali":
        print("your a citizen of Karnali")  
    elif Userstateinput == "sudurpaschim":
        print ("your a citizen of Sudurpaschim")
    else :
        print("your not a Nepali citizen")
elif Userinput == "UK":
    Userstateinput = input("enter your state = ")

    if Userstateinput == "England":
        print("your a citizen of England")
    elif Userstateinput == "Wales":
        print("your a citizen of Wales")
    elif Userstateinput == "Scotland":
        print("your a citizen of Scotland")
    elif Userstateinput == "Ireland":
        print("your a citizen of Ireland ")
    else:
        print("your not a citizen of Uk")
else:
    print("your not a citizen of Nepal nor of Uk")
    
