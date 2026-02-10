from dataclasses import fields

import easygui as eg

expenses = []
income_total = 0

eg.msgbox("Welcome to the Budget Tracker!",
          "Budget App",
          image="money.png")
name = eg.enterbox("Enter your name:", "User Info")
pin = eg.passwordbox("Create a PIN for your budget tracker:", "Security")

choice = eg.buttonbox("What would you like to do first?",
                      "Start Menu",
                      choices=["Add Income", "Add Expense"])
if choice == "Add Income":
    income = eg.integerbox("Enter Income Amount:", "Income Amount", lowerbound=0)
    if income:
        income_total += income
while True:
    action = eg.choicebox(
        f"{name}, select an action:",
        "Budget Menu",
        choices=["Add Expense", "View Expenses", "View Balance", "Category Spending", "Exit"]
    )
    if action == "Add Expense":
        fields = ["Expense Name", "Amount", "Category"]
        values = eg.multenterbox("Enter expense details:","New Expense", fields)
        if values:
            expense_name, amount, cateory = values
            expenses.append((expense_name, float(amount), cateory))
    elif action == "View Expenses":
        expense_text = "\n".join([f"{e[0]} - ${e[1]} ({e[2]})" for e in expenses])
        eg.textbox("Your expenses:", "Expense List", expense_text)
    elif action == "View Balance":
        total_expenses = sum(e[1] for e in expenses)
        balance = income_total - total_expenses
        eg.codebox("Balance Summary",
                   "Financial Overview",
                   f"Income: ${income_total}\nExpenses: ${total_expenses}\nBalance: ${balance}")
    elif action == "Category Spending":
        categories = list(set([e[2] for e in expenses]))
        selected = eg.multichoicebox("select a category:",
                                     "Categories",
                                     categories)
        if selected:
            filtered = [e for e in expenses if e[2] in selected]
            results = "\n".join([f"{e[0]} - ${e[1]}" for e in filtered])
            if eg.ynbox("Show selected category expenses?", "Confirm"):
                eg.msgbox(results, "Category Results")
    elif action == "Exit":
        confirm = eg.ynbox("Are you sure you want to exit?", "Continue")
        if confirm == 0:
            break
total_expenses = sum(e[1] for e in expenses)
balance = income_total - total_expenses
eg.msgbox(f"Final Balance: ${balance}", "Goodbye")