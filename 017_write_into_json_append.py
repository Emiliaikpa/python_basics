import json

with open("016_data.json", "r") as json_file:
    my_list_dict = json.load(json_file)

a = input("user_id:")
b = input("first_name:")
c = input("last_name:")
d = input("email:")
e = input("password:")

data_dict = {
        "user_id":a,
        "first_name":b,
        "last_name":c,
        "email":d,
        "password":e
        }

my_list_dict.append(data_dict)

with open("016_data.json", "w") as json_file:
      json.dump(my_list_dict, json_file)
