
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
        print("Aucune depense enregistree.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']} - "
              f"{expense['amount']:.2f}")

def show_total():
    total = sum(item["amount"] for item in expenses)
    print(f"Total : {total:.2f}")
def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return

    show_expenses()

    try:
        number = int(input("Enter the number of the expense to delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            print(f"Expense '{deleted['description']}' deleted successfully!")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Show total")
        print("4. Delete expense")
        print("5. Show average")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            show_average() 
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


def show_average():
    if not expenses:
        print("No expenses recorded.")
        return

    total = sum(item["amount"] for item in expenses)
    average = total / len(expenses)
    print(f"Average expense: {average:.2f}")

if __name__ == "__main__":
    main()