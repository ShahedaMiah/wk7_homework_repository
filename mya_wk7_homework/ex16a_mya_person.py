class Person():

    def __init__(self, name, gender, preferred_pronoun):
        self._name = name
        self._gender = gender
        self._pronoun = preferred_pronoun

    def home_address(self, address):
        self._home_address = address
        return '\n Home Address: ' + str(self._home_address)

    def home_number(self, home_no):
        self._contact_number =  int(home_no)
        return '\n Home No: ' + str(self._contact_number)

    def mobile_number(self, mobile_no):
        self._contact_number = mobile_no
        return '\n Mobile No: ' + str(self._contact_number)

    def email_add(self, email):
        self._email_add = email
        return '\n Email Add: ' + str(self._email_add)

    def __str__(self):
        return "Name: " +  str(self._name) + '\n' "Gender: " + str(self._gender) + '\n' "Preferred Pronouns: " + str(self._pronoun)

def main():
    mya = Person('Mya', 'Female', 'she/her')
    mya.email_add("mya.miah1980@gmail.com")
    print(mya, mya.email_add("mya.miah1980@gmail.com"))


if __name__ == "__main__":
    main()