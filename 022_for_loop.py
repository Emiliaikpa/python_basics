x = int(input("Enter starting number: "))

y = int(input("Enter ending number: "))


print("Even numbers in the given range:")

for num in range(x, y + 1):
    
    if num % 2 == 0:
        print(num)
