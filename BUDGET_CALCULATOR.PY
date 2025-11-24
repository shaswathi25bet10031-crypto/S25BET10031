def calculate_total_expenses(expenses):
    return sum(expenses.values())

def calculate_balance(income, total_expenses):
    return income - total_expenses

def suggest_savings(balance):
    # Suggest 20% of balance as savings if balance is positive
    return balance * 0.2 if balance > 0 else 0
