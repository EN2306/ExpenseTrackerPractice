import expense

def test_calc_total_amount():
    assert expense.calc_total_expenses(expense.expenses) == 22.60