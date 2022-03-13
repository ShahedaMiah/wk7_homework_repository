from ex16b_mya_acccount import Account

# Saving_Account is a kind of account
# Saving_Account is a derived class (subclass)
# Account is a base class (Superclass)
class Saving_Account(Account):

    def __init__(self, initial, interest_rate):
        super().__init__(initial)
        self._interest_rate = interest_rate

    def __str__(self):
        saving_info = self.get_holder_name()
        saving_info += "'s Savings "
        saving_info += super().__str__()
        return saving_info

    def calculate_interest(self):
        return self.getbalance() * self._interest_rate