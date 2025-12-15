print("----- SMART EXPENSE ANALYZER -----")

# Input income
income = float(input("Enter your monthly income: ₹ "))

# Expense inputs
food = float(input("Enter food expense: ₹ "))
rent = float(input("Enter rent expense: ₹ "))
travel = float(input("Enter travel expense: ₹ "))
shopping = float(input("Enter shopping expense: ₹ "))
others = float(input("Enter other expenses: ₹ "))

# Store expenses in dictionary
expenses = {
    "Food": food,
    "Rent": rent,
    "Travel": travel,
    "Shopping": shopping,
    "Others": others
}

# Calculations
total_expense = sum(expenses.values())
savings = income - total_expense
savings_percent = (savings / income) * 100

# Highest expense category
highest_category = max(expenses, key=expenses.get)

# Output
print("\n----- RESULT -----")
print("Total Expense: ₹", total_expense)
print("Total Savings: ₹", savings)
print("Savings Percentage:", round(savings_percent, 2), "%")
print("Highest Spending Category:", highest_category)

# Smart Advice
print("\n----- SMART ADVICE -----")
if savings_percent >= 30:
    print("Excellent saving! Keep it up 👍")
elif savings_percent >= 15:
    print("Good saving, but you can improve 💡")
else:
    print("Your expenses are too high! Try reducing", highest_category)
