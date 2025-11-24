def expense_breakdown(expenses):
    print("Expense Breakdown:")
    total = sum(expenses.values())
    for cat, amt in expenses.items():
        percent = (amt / total * 100) if total else 0
        print(f" - {cat}: {amt:.2f} ({percent:.1f}%)")

def highest_expense(expenses):
    if not expenses:
        print("No expenses to analyze.")
        return
    category = max(expenses, key=expenses.get)
    print(f"Highest expense: {category} = {expenses[category]:.2f}")
