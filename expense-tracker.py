expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount: "))
        expenses.append({"name": name, "amount": amount})
        print("Expense added.")

    elif choice == "2":
        print("\nExpenses:")
        total = 0

        for expense in expenses:
            print(f"{expense['name']}: ${expense['amount']:.2f}")
            total += expense["amount"]

        print(f"Total: ${total:.2f}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")