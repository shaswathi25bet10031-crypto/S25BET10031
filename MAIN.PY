from user_management import create_user
from input_collector import collect_income, collect_expenses
from data_processing import validate_income_expenses
from budget_calculator import calculate_total_expenses, calculate_balance, suggest_savings
from reporting import print_report, save_report
from analytics import expense_breakdown, highest_expense
from utils import log_error

def main():
    try:
        user = create_user()
        income = collect_income()
        expenses = collect_expenses()
        validate_income_expenses(income, expenses)
        total_expenses = calculate_total_expenses(expenses)
        balance = calculate_balance(income, total_expenses)
        suggested = suggest_savings(balance)
        print_report(user, income, expenses, balance, suggested)
        save_report("budget_report.txt", user, income, expenses, balance, suggested)
        expense_breakdown(expenses)
        highest_expense(expenses)
    except Exception as e:
        log_error(str(e))

if __name__ == "__main__":
    main()
