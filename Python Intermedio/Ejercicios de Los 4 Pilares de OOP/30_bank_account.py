class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit_money(self, deposited_amount):
        self.balance += deposited_amount
        return f"Confirmed {deposited_amount} deposit. Your new balance is: {self.balance}"
        
    def withdraw_money(self, withdrawn_amount):
        self.balance -= withdrawn_amount
        return f"Confirmed {withdrawn_amount} withdrawal. Your new balance is: {self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance

    def check_balance(self, withdrawn_amount):
        if self.balance - withdrawn_amount < self.min_balance:
            raise ValueError("Insufficient amount")
        return self.withdraw_money(withdrawn_amount)


def main():
    account1 = BankAccount(1000)
    print(account1.deposit_money(5000))

    savings1 = SavingsAccount(1000, 0)  
    print(savings1.check_balance(550))    
    print(savings1.check_balance(600))    

main()