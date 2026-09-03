# Python Expense Tracker

expenses = []

def add_expense(category, amount):
    expenses.append({
        "category": category,
        "amount": amount
    })

def show_expenses():
    print("\n--- Expense List ---")

    if not expenses:
        print("No expenses recorded.")
        return

    for expense in expenses:
        print(f"{expense['category']}: ₹{expense['amount']:.2f}")

def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expense: ₹{total:.2f}")


# Sample expenses
add_expense("Food", 150)
add_expense("Travel", 80)
add_expense("Stationery", 120)
add_expense("Food", 100)

print("PERSONAL EXPENSE TRACKER")
print("------------------------")

show_expenses()
show_total()