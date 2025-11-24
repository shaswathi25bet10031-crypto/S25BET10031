def print_report(user, income, expenses, balance, suggested_savings):
    print("Budget Report")
    print(f"User: {user.name}")
    print(f"Income: {income:.2f}")
    print("Expenses:")
    for cat, amt in expenses.items():
        print(f" - {cat}: {amt:.2f}")
    print(f"Total Expenses: {sum(expenses.values()):.2f}")
    print(f"Balance: {balance:.2f}")
    print(f"Suggested Savings: {suggested_savings:.2f}")

def save_report(filename, user, income, expenses, balance, suggested_savings):
    with open(filename, "w") as f:
        f.write(f"User: {user.name}\n")
        f.write(f"Income: {income:.2f}\n")
        f.write("Expenses:\n")
        for cat, amt in expenses.items():f.write(f" - {cat}: {amt:.2f}")
        f.write(f"Total Expenses: {sum(expenses.values()):.2f}")
        f.write(f"Balance: {balance:.2f}")
        f.write(f"Suggested Savings: {suggested_savings:.2f}")
