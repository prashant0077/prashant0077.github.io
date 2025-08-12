# file = open("new.txt","w")
# file.write ("we will keep on adding to this")
# file.close



# file = open("new.txt","r")
# result = file.read()
# print(result)


# football=["mancity","liverpool","arsenal","chelsea","spurs","manunited"]
# with open ("football.txt","w") as f:
#     for ball in football:
#         f.write(ball+"\n")
# with open ("football.txt","r") as f:
#     foot = f.read()
#     print(foot)



with open ("football.txt","w") as f:
    for i in f:
        # f.read(i+"\n")
     print (i.strip())

