import expense
import pytest

def test_calc_total_amount():
    assert expense.calc_total_expenses(expense.expenses) == 22.60
def test_get_highest_expense():
    assert expense.get_highest_expense(expense.expenses) == ({"item": "Dinner", "amount": "8.50", "category": "Food"})
def test_calc_average_expenses():
    assert expense.calc_average_expenses(expense.expenses) == pytest.approx(4.52)
def test_get_expenses_by_category():
    assert expense.get_expenses_by_category(expense.expenses, "Food") == [{"item": "Lunch", "amount": "5.50", "category": "Food"},{"item": "Dinner", "amount": "8.50", "category": "Food"}]
def test_format_total():
    assert expense.format_total("12.5") == "Total expenses: $12.50"