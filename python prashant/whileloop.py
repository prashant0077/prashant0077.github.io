# number = 1
# while number <= 200:
#     print("the number is",number)
#     number+=3


# for i in range(1, 100):
    
#     if i ==50:
#         break
#     print(i)


# for i in range(1,20):

#     if(i==10):
#         continue
#     print(i)


# number =0
# while number<=10:
#     print(number)
#     number+=1


# username = "Admin"

# UserInput = input("Enter Your Username")


# while UserInput !=username:
#     print("Try Again")
#     UserInput = input("Enter Your Username")


 

# username = "hello"
# password = "9999"

# userinput = input("enter your username")
# userpasswordinput = input("enter your password")
# while userinput!=username or userpasswordinput!=password:
#     print("try again")
#     userinput = input("enter your username")


# print("Welcome")


# username = "hello"
# password = 9999

# userinput = input("Enter your username: ")
# userpasswordinput = int(input("Enter your password: "))

# while userinput == username and userpasswordinput == password:
#     print("Try again.")
#     userinput = input("Enter your username: ")
#     userpasswordinput = int(input("Enter your password: "))  # <-- this was missing

# print("Welcome!")


# attempt =1
# input("enter your name : ")

# while attempt<=3:
#     input("enter your name : ")
#     attempt+=1


# attempt = 1
# username = ("hello")

# userinput = ("enter your name : ")

# while attempt <=3:
#     userinput !=username
#     print("ENter your name : ")
# attempt+=1




# attempt = 0
# max_attempt = 3

# username = "Admin"
# password = "Admin123"



# while attempt<=max_attempt:
#     userinput = input("Enter Your Name")
#     userpass = input("Enter your password")

#     if(userinput==username and password==userpass):
#         print("Welcome User. You have successfully login in", attempt, "Times")
#         break
#     else:
        
#         print("Incorrect Password or Username. You Have only", max_attempt-attempt,"left")
#         attempt+=1



# username="Power"   
# password="Ranger"
# id ="9999"

# attempt= 0
# maxattempt= 3

# while attempt <=3:
#      userinput = input("Enter Your Username :")
#      Userpasswordinput = input ("Enter your Password : ")
#      useridinput = input("Enter your ID : ")
#      if username == userinput and password == Userpasswordinput and id == useridinput:
#       print ("Welcome Hero! You have successful logged into your Account in", attempt )
#       break
#      else:
#          print("incorrect password or username.You have",maxattempt-attempt,"left" )
#          attempt+=1
# else:
#    print("You have ran out of all your attempts")



# name = "Stormace"
# password = "acemaster69" 
# id = "8888"
# power_level = "7"

# attempt = 1
# max_attempt = 3

# while attempt <=3:
#    userinput = input ("Speak thy name, brave soul, and let destiny take its course... ")
#    userpassinput = input ("Whisper the secret phrase, known only to the chosen... :")
#    useridinput = input ("Reveal thy ancient sigil, that we may know thee... : ")
#    userpower_levelinput = input ("Reveal thy power level, oh mighty one... so the realm may tremble! : ")
#    if name == userinput and password == userpassinput and id == useridinput and userpower_levelinput == power_level:
#       print("Welcome, Master! 🧙‍♂️ You have finally made it… after ", attempt, "valiant attempts! The realm has been waiting. 🏰✨ ")
#       break
#    else:
#         print("Access denied, Master. 🛑 You have failed gloriously…",max_attempt-attempt," attempt left. The gates remain closed… for now. 🕵️‍♂️🔒") 
#         attempt+=1
# else:
#     print ("Game over, Master. 💥 You have run out of attempts — the system has claimed victory. 🔒 No more chances... for now. 🕳️👀")

attempt = 1
max_attempt = 3
while attempt<=max_attempt:
    name = input ("Enter your name")
    #print("You are a nobody... You have ",max_attempt-attempt," attempts left. Choose your path wisely. ⚡")
    #attempt+=1
    if  name == "Prashant":
        playername = "Stormace"
        password = "acemaster69" 
        id = "8888"
        power_level = "7"
        oattempt = 1 
        omax_attempt = 3

        while oattempt <=3:
            userinput = input ("Speak thy name, brave soul, and let destiny take its course... ")
            userpassinput = input ("Whisper the secret phrase, known only to the chosen... :")
            useridinput = input ("Reveal thy ancient sigil, that we may know thee... : ")
            userpower_levelinput = input ("Reveal thy power level, oh mighty one... so the realm may tremble! : ")
            if playername == userinput and password == userpassinput and id == useridinput and userpower_levelinput == power_level:
                print("Welcome, Master! 🧙‍♂️ You have finally made it… after ", oattempt, "valiant attempts! The realm has been waiting. 🏰✨ ")
                break
            else:
                print("Access denied, Master. 🛑 You have failed gloriously…",omax_attempt-oattempt," attempt left. The gates remain closed… for now. 🕵️‍♂️🔒") 
                oattempt+=1
        else:
            print ("Game over, Master. 💥 You have run out of attempts — the system has claimed victory. 🔒 No more chances... for now. 🕳️👀")
    elif name == "Prabhakar":
        playername = "Stormbreaker"
        password = "stormbreaker69" 
        id = "9999"
        power_level = "8"
        attempt = 1 
        max_attempt = 3

        while attempt <=3:
            userinput = input ("Speak thy name, brave soul, and let destiny take its course... ")
            userpassinput = input ("Whisper the secret phrase, known only to the chosen... :")
            useridinput = input ("Reveal thy ancient sigil, that we may know thee... : ")
            userpower_levelinput = input ("Reveal thy power level, oh mighty one... so the realm may tremble! : ")
            if playername == userinput and password == userpassinput and id == useridinput and userpower_levelinput == power_level:
                print("Welcome, Master! 🧙‍♂️ You have finally made it… after ", attempt, "valiant attempts! The realm has been waiting. 🏰✨ ")
                break
            else:
                print("Access denied, Master. 🛑 You have failed gloriously…",max_attempt-attempt," attempt left. The gates remain closed… for now. 🕵️‍♂️🔒") 
                attempt+=1
        else:
            print ("Game over, Master. 💥 You have run out of attempts — the system has claimed victory. 🔒 No more chances... for now. 🕳️👀")
    elif name == "Johnny":
        playername = "malkova"
        password = "jean" 
        id = "6666"
        power_level = "10"
        attempt = 1 
        max_attempt = 3

        while attempt <=3:
            userinput = input ("Speak thy name, brave soul, and let destiny take its course... ")
            userpassinput = input ("Whisper the secret phrase, known only to the chosen... :")
            useridinput = input ("Reveal thy ancient sigil, that we may know thee... : ")
            userpower_levelinput = input ("Reveal thy power level, oh mighty one... so the realm may tremble! : ")
            if playername == userinput and password == userpassinput and id == useridinput and userpower_levelinput == power_level:
                print("Welcome, Master! 🧙‍♂️ You have finally made it… after ", attempt, "valiant attempts! The realm has been waiting. 🏰✨ ")
                break
            else:
                print("Access denied, Master. 🛑 You have failed gloriously…",max_attempt-attempt," attempt left. The gates remain closed… for now. 🕵️‍♂️🔒") 
                attempt+=1
        else:
            print ("Game over, Master. 💥 You have run out of attempts — the system has claimed victory. 🔒 No more chances... for now. 🕳️👀")
    elif name == "Ronaldo":
        playername = "cristiano"
        password = "CR7" 
        id = "7777"
        power_level = "100"
        attempt = 1 
        max_attempt = 3

        while attempt <=3:
            userinput = input ("Speak thy name, brave soul, and let destiny take its course... ")
            userpassinput = input ("Whisper the secret phrase, known only to the chosen... :")
            useridinput = input ("Reveal thy ancient sigil, that we may know thee... : ")
            userpower_levelinput = input ("Reveal thy power level, oh mighty one... so the realm may tremble! : ")
            if playername == userinput and password == userpassinput and id == useridinput and userpower_levelinput == power_level:
                print("Welcome, Master! 🧙‍♂️ You have finally made it… after ", attempt, "valiant attempts! The realm has been waiting. 🏰✨ ")
                break
            else:
                print("Access denied, Master. 🛑 You have failed gloriously…",max_attempt-attempt," attempt left. The gates remain closed… for now. 🕵️‍♂️🔒") 
                attempt+=1
        else:
            print ("Game over, Master. 💥 You have run out of attempts — the system has claimed victory. 🔒 No more chances... for now. 🕳️👀")
    else:
        print("Invalld Name")
        print("You are a nobody... You have ",max_attempt-attempt," attempts left. Choose your path wisely. ⚡")
        attempt+=1
else:
    print("You have reached your attempt")