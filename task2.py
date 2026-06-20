total = 0

while True:

    expense = input("Enter expense (or type exit): ")

    if expense == "exit":
        break

    total = total + int(expense)

    print("Current total:", total)

print("Final total spent:", total)