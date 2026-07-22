class BankAccount:
    def __init__(self, opening_balance: float = 0) -> None:
        self.__balance = opening_balance

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount

account = BankAccount(100)
account.deposit(25)
print(account.balance)
