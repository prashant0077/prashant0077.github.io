# import os
import json

def add_name():
    try:
        name=input("enter your name :")
        with open("info.json","r") as f:
            result = json.load(f) 
    except json.JSONDecodeError:
        result = []
        result.append({"name":name})

        with open("info.json", "w") as f:
            json.dump(result,f, indent=4)
        print("Json not found")
add_name()


# with open("name.json","r") as f:
#      result = json.load(f)
     

# if os.path.exists("name.json")and os.path.getsize("name.json"):
#     with open("name.json","r")as file:
#      json.load(file)
# else:
#    name = []

# name.append({"name": name})

# with open("names.json", "w") as file:
#         json.dump(name, file, indent=False)
