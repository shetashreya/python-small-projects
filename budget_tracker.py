class Category:
    def __init__(self, name):
        self.name = name
        self.transactions = []

    def add_transaction(self, description, amount, transaction_type):
        transaction = Transaction(description, amount, transaction_type)
        self.transactions.append(transaction)
        print("Transaction added successfully.")

    def get_total(self):
        total = sum(transaction.amount for transaction in self.transactions)
        return total

    def get_transactions(self):
        return self.transactions

class Transaction:
    def __init__(self, description, amount, transaction_type):
        self.description = description
        self.amount = amount
        self.transaction_type = transaction_type

class BudgetTracker:
    def __init__(self):
        self.categories = {}

    def add_category(self, category_name):
        if category_name not in self.categories:
            self.categories[category_name] = Category(category_name)
            print("Category added successfully.")
        else:
            print("Category already exists.")

    def add_transaction(self, category_name, description, amount, transaction_type):
        if category_name in self.categories:
            category = self.categories[category_name]
            category.add_transaction(description, amount, transaction_type)
        else:
            print("Category not found.")

    def view_category_report(self, category_name):
        if category_name in self.categories:
            category = self.categories[category_name]
            total = category.get_total()
            transactions = category.get_transactions()

            print(f"Category: {category_name}")
            print(f"Total Amount: ${total:.2f}")

            if transactions:
                print("Transactions:")
                for transaction in transactions:
                    print(f"{transaction.description} - ${transaction.amount:.2f} ({transaction.transaction_type})")
            else:
                print("No transactions in this category.")
        else:
            print("Category not found.")

def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\nMenu:")
        print("1. Add Category")
        print("2. Add Transaction")
        print("3. View Category Report")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            category_name = input("Enter category name: ")
            budget_tracker.add_category(category_name)

        elif choice == "2":
            category_name = input("Enter category name: ")
            description = input("Enter transaction description: ")
            amount = float(input("Enter transaction amount: "))
            transaction_type = input("Enter transaction type (Income/Expense): ").capitalize()
            budget_tracker.add_transaction(category_name, description, amount, transaction_type)

        elif choice == "3":
            category_name = input("Enter category name to view report: ")
            budget_tracker.view_category_report(category_name)

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
