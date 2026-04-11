import json

transactions = []

def show_menu():
    print("\n=== Personal Finance Tracker ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View History")
    print("5. Delete Transaction")
    print("6. View Summary")
    print("7. Exit")


def main():
    load_data()
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_income()

        elif choice == "2":
            add_expense()

        elif choice == "3":
            view_balance()

        elif choice == "4":
            view_history()


        elif choice == "5":
            delete_transaction()


        elif choice == "6":

            show_summary()

        elif choice == "7":
            print("\nExiting... Goodbye 👋")
            break

        else:
            print("\nInvalid choice. Please try again.")

def add_income():
    try:
        amount = float(input("Enter income amount: "))

        if amount <= 0:
            print("Amount must be greater than 0 ❌")
            return

        source = input("Enter income source (e.g. salary, gift): ").lower()

        transactions.append({
            "type": "income",
            "amount": amount,
            "category": source
        })

        save_data()
        print("Income added successfully ✅")

    except ValueError:
        print("Invalid amount ❌")


def add_expense():
    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than 0 ❌")
            return

        category = input("Enter category (e.g. food, transport): ").lower()

        transactions.append({
            "type": "expense",
            "amount": amount,
            "category": category
        })

        save_data()
        print("Expense added successfully ✅")

    except ValueError:
        print("Invalid amount ❌")

def view_balance():
    income_total = 0
    expense_total = 0

    for t in transactions:
        if t["type"] == "income":
            income_total += t["amount"]
        elif t["type"] == "expense":
            expense_total += t["amount"]

    balance = income_total - expense_total

    print("\n=== Balance Summary ===")
    print(f"Total Income : {income_total}")
    print(f"Total Expense: {expense_total}")
    print(f"Balance      : {balance}")

def view_history():
    if not transactions:
        print("\nNo transactions yet.")
        return

    print("\n=== Transaction History ===")

    for index, t in enumerate(transactions, start=1):
        t_type = t["type"].capitalize()
        amount = t["amount"]
        category = t.get("category", "N/A")

        print(f"{index}. {t_type:<8} | {amount:>8.2f} | {category}")

def save_data():
    with open("data.json", "w") as file:
        json.dump(transactions, file)

def load_data():
    global transactions
    try:
        with open("data.json", "r") as file:
            transactions = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        transactions = []

def delete_transaction():
    if not transactions:
        print("\nNo transactions to delete.")
        return

    view_history()

    try:
        index = int(input("Enter transaction number to delete: ")) - 1

        if index < 0 or index >= len(transactions):
            print("Invalid transaction number ❌")
            return

        removed = transactions.pop(index)
        save_data()

        print(f"Deleted {removed['type']} ({removed.get('category', 'N/A')}) - {removed['amount']} ✅")

    except ValueError:
        print("Invalid input ❌")

def show_summary():
    if not transactions:
        print("\nNo transactions available.")
        return

    summary = {}

    for t in transactions:
        if t["type"] == "expense":
            category = t.get("category", "other")

            if category in summary:
                summary[category] += t["amount"]
            else:
                summary[category] = t["amount"]

    if not summary:
        print("\nNo expense data to summarize.")
        return

    print("\n=== Expense Summary ===")

    total = 0
    for category, amount in summary.items():
        print(f"{category:<12}: {amount:.2f}")
        total += amount

    print(f"\nTotal Expense: {total:.2f}")

if __name__ == "__main__":
    main()