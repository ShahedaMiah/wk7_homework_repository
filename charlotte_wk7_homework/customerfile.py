class Customer:

    product_prices = {
        "alcohol": 20,
        "chocolate": 2,
        "pepper": 1,
        "cheese": 5
    }

    def __init__(self, first_name, last_name, age, gender, contact_number, shop_name, items_bought, no_of_items):
        super().__init__(first_name, last_name, age, gender, contact_number)
        self.age = None
        self.shop_name = shop_name
        self.items_bought = list[items_bought]
        self.no_of_items = int(no_of_items)

    def age_restriction_check(self, age):
        self.age = age
        if age > 18:
            print("You can buy this age-restricted product.")
        else:
            print("Unfortunately you cannot buy this age-restricted product.")


