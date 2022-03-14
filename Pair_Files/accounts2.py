from account_exception2 import InsufficientFundsException

class Account:
    numCreated = 0
    def __init__(self, initial):

        self._balance = initial
        Account.numCreated += 1

    def deposit(self, amount):
        self._balance += amount
        print("You have deposited £{} into your account".format(amount))

    def withdraw(self, amount):
        # self._balance = self._balance - amount
        self.amount = amount
        if self.amount > self.__balance:
            raise InsufficientFundsException('-')
        return "You have £" + str(self._balance)
        else:
            self.__balance = self.__balance - amount

    def get_holder_name(self):
        return self.__holder_name

    def set_holder_name(self, name):
        self.__holder_name = name

    def getbalance(self):
        return self._balance

    def __str__(self):
        return 'Account has balance £' + str(self.getbalance())

    def __add__(self, other):
        return self.getbalance() + other.getbalance()

def main():
    homer = Account(350)
    homer.deposit(450)
    homer.withdraw(900)
    print('Homer Account: £', homer.getbalance())


if __name__ == "__main__":
    main()

# print(help(Person))
# print(help(Employee))
# print(help(Customer))

# check for class inheritance
# print(issubclass(Employee, Person))     #True
# print(issubclass(Customer, Person))     #True
