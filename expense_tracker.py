# Expense Tracker - DecodeLabs Project 2

expenses = []
total = 0

print("===== Expense Tracker =====")
print("Enter your expenses one by one.")
print("Type 'quit' to finish.\n")

while True:
    entry = input("Enter expense: ")

    if entry.lower() == "quit":
        break

    try:
        expense = float(entry)

        if expense < 0:
            print("Expense cannot be negative!")
            continue

        expenses.append(expense)
        total += expense

        print(f"Expense Added: ₹{expense}")
        print(f"Current Total: ₹{total}\n")

    except ValueError:
        print("Invalid input! Please enter a valid number.\n")

print("\n===== Expense Summary =====")

if expenses:
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. ₹{expense}")

    print(f"\nTotal Spent: ₹{total}")
else:
    print("No expenses entered.")

print("Thank you for using Expense Tracker!")