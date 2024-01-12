import json
import os
from datetime import datetime

# Function to load data from JSON file
def load_data():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            return json.load(file)
    else:
        return {"expenses": [], "budget": 0}

# Function to save data to JSON file
def save_data(data):
    with open("expenses.json", "w") as file:
        json.dump(data, file, indent=2)

# Function to record an expense
def record_expense(data, category, amount):
    expense = {"date": str(datetime.now()), "category": category, "amount": amount}
    data["expenses"].append(expense)
    save_data(data)

# Function to display expenses
def display_expenses(data):
    print("\nExpense History:")
    for expense in data["expenses"]:
        print(f"{expense['date']} - {expense['category']}: ${expense['amount']}")

# Function to set budget
def set_budget(data, budget):
    data["budget"] = budget
    save_data(data)
    print(f"\nBudget set to: ${budget}")

# Function to generate a basic expense report
def generate_report(data):
    total_expenses = sum(expense["amount"] for expense in data["expenses"])
    remaining_budget = data["budget"] - total_expenses

    print("\nExpense Report:")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Remaining Budget: ${remaining_budget}")

# Main function
def main():
    data = load_data()

    while True:
        print("\nPersonal Finance Management Tool")
        print("1. Record an Expense")
        print("2. Display Expenses")
        print("3. Set Budget")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            record_expense(data, category, amount)
        elif choice == "2":
            display_expenses(data)
        elif choice == "3":
            budget = float(input("Enter your budget: "))
            set_budget(data, budget)
        elif choice == "4":
            generate_report(data)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
