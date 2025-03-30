age = int(input("Enter Age: "))

if age < 13:
    print("you are a child.")

elif 13 <= age <= 19:
    print("you are a teenager.")

elif 20 <= age <= 59:
    print("you are an adult.")

else:
    print("you are a senior citizen.")
