from cuenta import BankAccount

# This class represents a bank interface where the user can perform operations on the bank account
class BankInterface:
    # Constants
    DEPOSIT = 1
    WITHDRAW = 2
    CHECK_BALANCE = 3
    EXIT = 4
    bank_account = None

    # Constructor
    def __init__(self, bank_account):
        self.bank_account = bank_account

    # Show the menu
    def show_menu(self):
        print("\n--- Bank Account Menu ---")
        print(f"{self.DEPOSIT}. Deposit money")
        print(f"{self.WITHDRAW}. Withdraw money")
        print(f"{self.CHECK_BALANCE}. Check balance")
        print(f"{self.EXIT}. Exit")
    
    # Get the user input
    def get_user_choice(self):
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if self.DEPOSIT <= choice <= self.EXIT:
                    return choice
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid choice. Please try again.")
    
    # Run the interface
    def run(self):
        while True:
            self.show_menu() # Show the menu
            choice = self.get_user_choice() # Get the user choice

            if choice == self.DEPOSIT:
                amount = float(input("Enter the amount to deposit: "))
                self.bank_account.deposit(amount)
            elif choice == self.WITHDRAW:
                amount = float(input("Enter the amount to withdraw: "))
                self.bank_account.withdraw(amount)
            elif choice == self.CHECK_BALANCE:
                print(self.bank_account)
            elif choice == self.EXIT:
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")