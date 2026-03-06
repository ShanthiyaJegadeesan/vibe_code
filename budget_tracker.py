# budget_tracker.py

def main():
    print("--- Simple Budget Tracker (LKR) ---")
    
    # 1. Ask for the total monthly budget
    while True:
        try:
            budget_input = input("Enter your total monthly budget in LKR: ")
            total_budget = float(budget_input)
            break
        except ValueError:
            print("Please enter a valid number for the budget.")

    current_balance = total_budget
    expenses = []

    # 2. Allow the user to enter expenses repeatedly
    print("\nEnter your expenses one by one. Type 'done' to finish.")
    
    while True:
        entry = input("Enter expense amount (or 'done'): ").strip().lower()
        
        # 3. Stop entering if the user types "done"
        if entry == "done":
            break
        
        try:
            expense_amount = float(entry)
            
            # 4. Subtract the expense from the total budget
            current_balance -= expense_amount
            expenses.append(expense_amount)
            
            print(f"Recorded LKR {expense_amount:.2f}. Remaining balance: LKR {current_balance:.2f}")
            
            if current_balance < 0:
                print("Warning: You have exceeded your budget!")
                
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    # 5. Final Summary
    print("\n--- Final Budget Summary ---")
    print(f"Starting Budget: LKR {total_budget:.2f}")
    print(f"Total Expenses:  LKR {sum(expenses):.2f}")
    print(f"Final Balance:   LKR {current_balance:.2f}")
    
    if current_balance >= 0:
        print("Great job! You stayed within your budget.")
    else:
        print("Take care! You spent more than your allocated budget.")

if __name__ == "__main__":
    main()
