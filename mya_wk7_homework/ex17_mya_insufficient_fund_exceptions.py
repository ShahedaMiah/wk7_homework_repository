from ex16b_mya_savings_account import Saving_Account

class InsufficientFundsException(Saving_Account):

    def __init__(self, initial, interest_rate):
        super().__init__(initial, interest_rate)

    def check_if_in_credit(self):