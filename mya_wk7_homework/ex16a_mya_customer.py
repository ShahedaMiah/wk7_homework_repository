from ex16a_mya_person import Person

class Customer(Person):

    def __init__(self, name, gender, preferred_pronoun, email, contact_no, address):
        super().__init__(name, gender, preferred_pronoun)
        self._email_add = email
        self._contact_number = contact_no
        self._customer_address = address

    def customer_no(self, customer_no):
        self._customer_no = customer_no
        return '\n Customer No: ' + str(self._customer_no)

    def account_manager(self, mananger):
        self._account_mananger = manager
        return '\n Account Contact: ' + str(self._account_mananger)

    def delivery_address(self, address):
        self._delivery_address = address
        return '\n Delivery Address: ' + str(self._delivery_address)

    def card_details(self, card_type, card_no, end_date, security_code):
        self._card_type = card_type
        self._card_no = card_no
        self._end_date = end_date
        self._security_code = security_code
        return '\n Card Type: ' + str(self._card_type) + '\n Card No: ' + str(self._card_no) + '\n End Date: ' + str(self._end_date) + '\n Security Code: ' + str(self._security_code)

    def __str__(self):
        return super().__str__() + '\n' "Email Add: " + str(self._email_add) + '\n' "Contact No: " + str(
            self._contact_number) + '\n' "Home Address: " + str(self._customer_address)

def main():
    miah = Customer('Shay', 'female', 'she/her', 'mya.miah1980@hotmail.co.uk', '07932673910', '3 Kirton Close W4 5UD')

    print(miah, miah.customer_no(150), miah.delivery_address('2 Kirton Close W4 5UU'))

if __name__ == "__main__":
    main()
