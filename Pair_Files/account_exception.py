from savings_account import Saving_Account
from accounts import Account

class InsufficientFundsException(Account):

    def __init__(self, initial, payment):
        super().__init__(initial)
        self._payment = payment

    def if_in_credit(self, amount):
        self.amount = amount
        if self.amount > self._balance:
            print("Error: Insufficient funds available, cannot process withdrawal")
        else:
            self._balance = self._balance - self.amount

# acc = InsufficientFundsException(1000, 5)
# acc.set_holder_name("Charlotte Abbotts")
# acc.deposit(500)
# acc.if_in_credit(400)
#
# print(acc)