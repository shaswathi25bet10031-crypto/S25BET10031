def collect_income():
    while True:
        try:
            income = float(input("Enter your total monthly income: "))
            if income < 0:
                print("Income cannot be negative.")
                continue
            return income
        except ValueError:
            print("Invalid input. Please enter a number.")

def collect_expenses():
    categories = ["Rent", "Utilities", "Groceries", "Transport", "Miscellaneous"]
    expenses = {}
    for category in categories:
        while True:
            try:
                amount = float(input(f"Enter your monthly expense for {category}: "))
                if amount < 0:
                    print("Expense cannot be negative.")
                    continue
                expenses[category] = amount
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return expenses
