
expenses = []

def add_expense():
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))

    expense = {
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")


def show_expenses():
    if not expenses:
        print("No expenses recorded.")
    else:
        for expense in expenses:
            print(expense["description"], "-", expense["amount"])


def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print("Total expenses:", total)


def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Show total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
