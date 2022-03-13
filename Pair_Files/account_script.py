import sys

from savings_account import Saving_Account
from accounts import Account
from account_exception import ZeroCreditError

def enough_money(*arguments):
    if Account.withdraw() > Account.getbalance():
        raise ZeroCreditError.in_credit()

def current_account(Saving_Account):
    try:
        acc1 = Saving_Account(4000, 2.5),
        acc1.set_holder_name("Charlotte Abbotts")
        acc1.deposit(10000)
        acc1.withdraw(20000)
        #enough_money()
    except ZeroCreditError.in_credit() as error:
        print("Oops: ", error, file=sys.stderr)
    finally:
        print(acc1, '\n', acc1.numCreated)

print(current_accountig)

