from bank_interface import BankInterface
from cuenta import BankAccount

# Doesn't work, please fix it 

# Create a bank account
bank_account = BankAccount('123456789', 1000, 'Acoidán')
ui = BankInterface(bank_account)
ui.run()