from personfile import Person


class Customer(Person):

    product_prices = {
        "alcohol": 20,
        "chocolate": 2,
        "pepper": 1,
        "cheese": 5
    }

    def __init__(self, first_name, last_name, age, gender, contact_number, shopping_list):
        super().__init__(first_name, last_name, age, gender, contact_number)
        self.shopping_list = shopping_list

    def add_to_shopping_list(self):
        self.shopping_list = []
        still_shopping = "yes"
        while still_shopping == "yes":
            grocery_item = input("What would you like to buy? chocolate, alcohol, pepper, cheese ")
            still_shopping = input("Are you still shopping? yes or no")
            self.shopping_list.append(grocery_item)

        if still_shopping == "no":
            print("Your shopping list is " + str(self.shopping_list))
        else:
            print("Please type yes or no")

    def age_restriction_check(self):
        while 'alcohol' in self.shopping_list:
            if self._age > 18:
                print("You can buy this age-restricted product.")
            else:
                print("Unfortunately you cannot buy this age-restricted product.")
            break

    # def calculate_shopping_cost(self):
    #     total_shop = 0
    #     for item in product_prices:
    #
    #     print(sum(self.shopping_list))