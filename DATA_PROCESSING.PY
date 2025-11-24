def validate_income_expenses(income, expenses):
    if income < 0:
        raise ValueError("Income must be non-negative.")
    for cat, value in expenses.items():
        if value < 0:
            raise ValueError(f"Expense for {cat} cannot be negative.")
    return True
