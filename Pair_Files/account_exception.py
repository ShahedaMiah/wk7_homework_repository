from savings_account import Saving_Account
from accounts import Account

class ZeroCreditError(Exception):
    #pass

    def in_credit(self):
        if Account.withdraw() >= Account.getbalance():
            #Account.withdraw
            return "you are in credit"
        else:
            return "insufficient funds available"