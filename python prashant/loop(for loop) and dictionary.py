#loop
# the repeation of block of code until the given condition is true. in python, there are two types of loop available.

#1 for loop 
# while loop 


#syntax of for loop 

# for i in range(1,5):
#     print(i)

# for num in range(1, 100, 4):
#     print(num)

# number = [1,2,3,4,5,6,7,8,9]


# for num in number:
#     print(num)

# students = ["Ram" , "Shyam" , "Hari" , "Laxman" , "Naresh"]
# for i in students:
#     print(i)

# for i in range(1, 11):
#     print(i*10)



# myname = ("Prashant")
# for i in myname:
#     print(i)


# Students = {
#     "name":"Prashant",
#     "country":"Nepal",
#     "district":"Lalitpur",
#     "number":9841999999,
#     "postal code":70000
#             }

# for info,value in Students.items():
#     print(info,value)



# Biography_of_Legend = {
#     "Name":": Laxmi Prasad Devkota",
#     "Title":": Mahakavi",
#     "Lived": ": 1909-1959",
#     "Job":": Poet",
#     "Best Creation":": Muna Madan, Sulochana, Kunjini, Bhikhari, and Shakuntala",
#     "Key Achievements and Awards":": Mahakavi Title, Saraswati Samman, Pioneer of Modern Nepali Poetry, Father of Modern Nepali Essay Writing"
# }
# for info,value in Biography_of_Legend.items():
#     print(info,value)


for i in range (1,4,):
    for j in range (1,6):
        for k in range (1,3):
            print(i,j,k)

 

    



    # attempt= 0
# maxattempt= 3

# while attempt <=3:
#     userinput = input("Enter Your Username")
#     Userpasswordinput = input ("Enter your Password")
#     if username == userinput and password == Userpasswordinput:
#      print ("Welcome Hero! You have successful logged into your Account in", maxattempt-attempt )
#     else:
#         print("you have",attempt,"left" )
# attempt+=1