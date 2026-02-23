from functools import reduce

def main():
        expenses = []
        print("Enter your monthly expenses.")
        print("Type 'Complete' when you are done entering.")


        while True :
            expense_type = input("Enter your expense type (or type 'complete'): ").lower()
            if expense_type == "complete":
                break
            try:
                amount = float(input("Enter your expense amount: $"))
                expenses.append({"type": expense_type, "amount": amount})
            except ValueError:
                print("Please enter a valid number for your expense.")

        if not expenses:
            print("No expenses entered... Please type in an expense.")
            return

        total = reduce(lambda acc, e: acc + e["amount"], expenses, 0)

        highest = reduce(
            lambda a, b: a if a["amount"] > b["amount"] else b,
            expenses
        )

        lowest = reduce(
            lambda a, b: a if a["amount"] < b["amount"] else b,
            expenses
        )


        print("--- Monthly Summary for Expenses---")
        print(f"Total Expenses are: ${total:.2f}")
        print(f"The Highest Expense is: ${highest['type']} - ${highest['amount']:.2f}")
        print(f"The Lowest Expense is: ${lowest['type']} - ${lowest['amount']:.2f}")

main()
        
