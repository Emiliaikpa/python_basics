import json

a = input("user_id")
b = input("first_name")
c = input("last_name")
d = input("email")
e = input("password")

user_dict = {
        'user_id':a,
        'first_name':b,
        'last_name':c,
        'email':d,
        'password':e
        }

with open("015_register.json", "w") as json_file:
    json.dump(user_dict, json_file)

print("user_dict")
