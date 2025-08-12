import pandas as pd

# data = {
#     "Std_id":[12,13,14,16,17],
#     "Student Name":["Ram","Shyame","Hari","Sita","Nikita"],
#     "Age":[20,19,17,18,16]
# }

# df = pd.DataFrame(data)

# df.to_excel("excel.xlsx",index=4)

# # df = open("excel.xlsx")

# # pd.DataFrame(data)

df = pd.read_excel("excel.xlsx")

print(df)




# import pandas as pd

# data = {
#     "Std_id": [12, 13, 14, 16, 17],
#     "Student Name": ["Ram", "Shyame", "Hari", "Sita", "Nikita"],
#     "Age": [20, 19, 17, 18, 16]
# }

# df = pd.DataFrame(data)

# df.to_excel("excel.xlsx", index=False)