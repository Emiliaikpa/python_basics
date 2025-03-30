age = int(input("Enter age: "))
nationality = input("Enter Nationality: ")


if age >= 18 and nationality == "Nigerian":
    print("you are eligible to vote in age in Nigeria.")

elif age < 18 and nationality == "Nigerian":
    print("you are too young to vote.")

else:
    print("you must be a Nigerian citizen to vote here.")
