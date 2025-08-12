

import json
import os
# with open("file1.json","r") as f:
#     result = json.load(f)
#     print(result["Class"])

# import json

# with open("file1.json", "w") as f:
#     data = {
#         "Location":"Lalitpur",
#         "Class":"SEE",
#         "Roll No:":21,
#         "Height":5.5
#     }

#     json.dump(data,f, indent=4)

def view_bio():
    if os.path.exists("bio.json")and os.path.getsize("bio.json")>0:
      with open("bio.json","r")as file:
         return json.load(file)
    else: 
      return{}

def viewbio():
   view=view_bio()
   view[data]= question
   if view:
      for data in view_bio():
         print(f"{data}")
      

username= "prashant"
password = "gautam"
result = view_bio
username1 = input("Enter your name")
userpass1 = input("Enter your password")

if username== username1 and password == userpass1:
    print("1.Name\n2.nickname\n3.DOB\nPolitics\n4elected PM\n5resigned PM\n6elected times")
    choice=int(input("Enter which verification you wnat to choice"))
    if choice ==1:
       

# with open("bio.json","w")as f:
#     data = {
#         "name":"Puspa kamal dahal",
#         "nickname":"prachanda",
#         "DOB ": "December 11, 1954",
#         "Politics:": "1970s",
#         "Elected PM": "2008",
#         "resigned PM": "2009",
#         "elected times":"3"
#     }
#     json.dump(data,f,indent=5)



    

    
    

