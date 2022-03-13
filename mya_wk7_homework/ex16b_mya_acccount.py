class Account:
    numCreated = 0 #Public class variable
    def __init__(self, initial):
    #constructor - a function calleed __init__()
    #the first parameter is 'self' is a very explicit parameter to the first instances
        self.__balance = initial
        self.semiPrivate = 'hello from account'
        Account.numCreated += 1
        self.__testItem = 'yes'

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance = self.__balance - amount

    # getter - read
    # translation
    def get_holder_name(self):
        return self.__holder_name

    # setter = write
    # validation logic
    def set_holder_name(self, name):
        self.__holder_name = name

    # property for description

    @property
    #the
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description


    # getter
    def getbalance(self):
        return self.__balance

    def __str__(self):
        return 'Account has balance ' + str(self.getbalance())

    def __add__(self, other):
        return self.getbalance() + other.getbalance()

def main():
    homer = Account(350)
    homer.deposit(450)
    print('Homer Account:', homer.getbalance())


if __name__ == "__main__":
# the function/s listed below will only
    main()