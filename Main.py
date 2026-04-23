import json


class Finance:
    def __init__(self):
        self.expenses = self.load_data()

    def add_expense(self, title, amount, category):
        expense = {
            "title": title,
            "amount": amount,
            "category": category
        }

        self.expenses.append(expense)
        self.save_data()

    def show_expenses(self):
        if not self.expenses:
            print("No expenses yet.")
            return

        total = 0
        for exp in self.expenses:
            print(f"{exp['title']} - {exp['amount']} - {exp['category']}")
            total += exp["amount"]

        print(f"\nTotal spent: {total}")

    def show_summary(self):
        if not self.expenses:
            print("No data to analyze.")
            return

        summary = {}

        for exp in self.expenses:
            category = exp["category"]
            amount = exp["amount"]

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

        print("\n--- SPENDING BY CATEGORY ---")
        for category, total in summary.items():
            print(f"{category}: {total}")

    def save_data(self):
        with open("data.json", "w") as file:
            json.dump(self.expenses, file)

    def load_data(self):
        try:
            with open("data.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []


# ---------------- MAIN PROGRAM ----------------

finance = Finance()

while True:
    print("\n--- FINANCE SYSTEM ---")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Show summary")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Title: ")
        amount = float(input("Amount: "))
        category = input("Category: ")

        finance.add_expense(title, amount, category)
        print("Expense saved.")

    elif choice == "2":
        finance.show_expenses()

    elif choice == "3":
        finance.show_summary()

    elif choice == "4":
        print("Goodbye.")
        break

    else:
        print("Invalid choice")