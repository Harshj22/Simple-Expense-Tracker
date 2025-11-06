print("Welcome to Simple Expense Tracker")

expenses = []   

while True:
    print("\n1. Add Expense")
    print("2. View All Expenses")
    print("3. Show Total Expense")
    print("4. Delete an Expense")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    # 1. Add Expense
    if choice == '1':
        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter category (e.g. Food, Travel, Shopping): ")
        amount = float(input("Enter amount spent: "))
        note = input("Enter a short note (optional): ")

        expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "note": note
        }

        expenses.append(expense)
        print("✅ Expense added successfully!")

    # 2. View All Expenses
    elif choice == '2':
        if not expenses:
            print("\nNo expenses recorded yet.")
        else:
            print("\n--- All Expenses ---")
            for i, e in enumerate(expenses, start=1):
                print(f"{i}. Date: {e['date']} | Category: {e['category']} | Amount: ₹{e['amount']} | Note: {e['note']}")

    # 3. Show Total Expense
    elif choice == '3':
        if not expenses:
            print("\nNo expenses to calculate.")
        else:
            total = sum(e['amount'] for e in expenses)
            print(f"\n💸 Total Expenses: ₹{total}")

    # 4. Delete an Expense
    elif choice == '4':
        if not expenses:
            print("\nNo expenses to delete.")
        else:
            for i, e in enumerate(expenses, start=1):
                print(f"{i}. {e['date']} - {e['category']} - ₹{e['amount']}")
            delete_index = int(input("\nEnter the expense number to delete: ")) - 1

            if 0 <= delete_index < len(expenses):
                deleted_item = expenses.pop(delete_index)
                print(f"Deleted expense: {deleted_item['category']} ₹{deleted_item['amount']}")
            else:
                print("❌ Invalid number. Please try again.")

    # 5 Exit Program
    elif choice == '5':
        print("\nThank you for using Expense Tracker! 👋")
        break

    else:
        print("❌ Invalid choice! Please enter a number between 1 to 5.")

                                                                    