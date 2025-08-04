import json
import os

# List to hold expenses (each as a dict: {'amount': 10.5, 'description': 'Coffee'})
expenses = []

# Function to show menu and get choice
def show_menu():
    print("\nPersonal Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Quit")
    return input("Enter your choice: ")

# Function to load expenses from file
def load_expenses():
    global expenses
    if os.path.exists('expenses.json'):
        with open('expenses.json', 'r') as file:
            expenses = json.load(file)
        print("Loaded existing expenses.")
    else:
        print("No saved expenses found.")

# Function to save expenses to file
def save_expenses():
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file)
    print("Expenses saved.")

# Helper function to display expenses with indices and return total
def display_expenses():
    if not expenses:
        print("No expenses yet.")
        return 0
    total = 0
    print("\nExpenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['description']}: ${exp['amount']:.2f}")
        total += exp['amount']
    print(f"Total: ${total:.2f}")
    return total

# Call load at start
load_expenses()

# Main loop
while True:
    choice = show_menu()
    if choice == '1':
        try:
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            expenses.append({'amount': amount, 'description': description})
            print("Expense added!")
        except ValueError:
            print("Invalid amount, must be a number.")
    elif choice == '2':
        display_expenses()
    elif choice == '3':
        if not expenses:
            print("No expenses to update.")
            continue
        display_expenses()
        try:
            index = int(input("Enter the number of the expense to update: ")) - 1
            if 0 <= index < len(expenses):
                print(f"Updating: {expenses[index]['description']}: ${expenses[index]['amount']:.2f}")
                new_amount_str = input("Enter new amount (leave blank to keep current): ")
                if new_amount_str:
                    expenses[index]['amount'] = float(new_amount_str)
                new_desc = input("Enter new description (leave blank to keep current): ")
                if new_desc:
                    expenses[index]['description'] = new_desc
                print("Expense updated!")
                save_expenses()
            else:
                print("Invalid number.")
        except ValueError:
            print("Invalid input, must be a number.")
    elif choice == '4':
        if not expenses:
            print("No expenses to delete.")
            continue
        display_expenses()
        try:
            index = int(input("Enter the number of the expense to delete: ")) - 1
            if 0 <= index < len(expenses):
                confirm = input(f"Delete '{expenses[index]['description']}'? (y/n): ").lower()
                if confirm == 'y':
                    del expenses[index]
                    print("Expense deleted!")
                    save_expenses()
                else:
                    print("Deletion canceled.")
            else:
                print("Invalid number.")
        except ValueError:
            print("Invalid input, must be a number.")
    elif choice == '5':
        save_expenses()
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")