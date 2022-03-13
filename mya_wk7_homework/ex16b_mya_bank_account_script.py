from ex16b_mya_savings_account import Saving_Account


tristan_saving = Saving_Account(1000, 1.5)
tristan_saving.set_holder_name("Tristan Wilkinson")
tristan_saving.deposit(750)
tristan_saving.withdraw(170)
print('Balance', tristan_saving.getbalance())
print(tristan_saving)


