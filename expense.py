
expenses = [
    {"item": "Lunch", "amount": "5.50", "category": "Food"},
    {"item": "MRT", "amount": "2.20", "category": "Transport"},
    {"item": "Notebook", "amount": "4.80", "category": "School"},
    {"item": "Dinner", "amount": "8.50", "category": "Food"},
    {"item": "Bus", "amount": "1.60", "category": "Transport"}
]

def calc_total_expenses(expenses):
    total = 0.0
    for i in range(len(expenses)):
        total += float(expenses[i]['amount'])
    return total
    
def get_highest_expense(expenses):
    highest = 0.0
    if len(expenses) > 0:
        for i in range(len(expenses)):
            if float(expenses[i]['amount']) >highest:
                highest = float(expenses[i]['amount'])
        return highest
    else:
        return None

def calc_average_expenses(expenses):
    avg = 0.0
    if len(expenses) > 0:
        avg = calc_total_expenses(expenses)/len(expenses)
    return avg

def get_expenses_by_category(expenses, category):
    ctg=[]
    for i in range(len(expenses)):
        if expenses[i][category]:
            ctg.append(expenses[i])
    return ctg

def format_total(total):
    t=float(total)
    print(f"Total Expenses: ${t:.3f}")

def main():
    print("----- Student Expense Tracker -----")
    print("1 - Display all expenses")
    print("2 - Display statistics")
    print("3 - Display highest expense")
    print("4 - Display food expenses")

    s = input("Enter selection => ")

    if s == "1":
        for e in expenses:
            print(e)

    elif s == "2":
        total = calc_total_expenses(expenses)
        avg = calc_average_expenses(expenses)
        print(format_total(total))
        print("Average:", avg)

    elif s == "3":
        print(get_highest_expense(expenses))

    elif s == "4":
        print(get_expenses_by_category(expenses, "Food"))

if __name__ == "__main__":
    main()