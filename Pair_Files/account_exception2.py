class InsufficientFundsException(Exception):

    def __init__(self, *args):
        if not all(*args):
            raise InsufficientFundsException('You have insufficient funds, cannot execute withdrawal')

    def __str__(self):
        self.message = ("You do not have money to make that withdrawal")
        return self.message