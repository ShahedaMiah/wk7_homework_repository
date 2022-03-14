import sys
from savings_account import Saving_Account
#from account_exception import InsufficientFundsException


try:
    charlotte = Saving_Account(4000, 2.5)
    # charlotte.set_holder_name("Charlotte Abbotts")
    # charlotte.deposit(10000)
    charlotte.withdraw(20000)

    mya = Saving_Account(3000, 2.5)
    # mya.set_holder_name("Mya Miah")
    # mya.deposit(12000)
    mya.withdraw(2000)
except InsufficientFundsException.if_in_credit(Saving_Account.withdraw) as error:
    print("Oops: ", error, file=sys.stderr)
finally:
    print(charlotte, '\n', mya, '\nNumber of Accounts Created: ', Saving_Account.numCreated)

#print(charlotte, '\n', mya)