# file = open("example.excel", "w")
# file.write("Hello Python")


# file = open("example.txt", "r")
# result = file.read()
# print(result)


# file = open ("Ronaldo.txt","w")
# file.write("Cristiano Ronaldo dos Santos Aveiro is a Portuguese professional footballer who plays as a forward for and captains both Saudi Pro League club Al-Nassr and the Portugal national team. ")

try:
    file = open ("ronalsdo.txt","r")
    intro = file.read()
    print(intro)
except FileNotFoundError as e:
    print ("file name already in use",e)





    