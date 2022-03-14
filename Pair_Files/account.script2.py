from account_exception import InsufficientFundsException

acc = InsufficientFundsException(1000, 2.5)
acc.set_holder_name("Charlotte Abbotts")
acc.deposit(500)
acc.if_in_credit(1600)

print(acc)

