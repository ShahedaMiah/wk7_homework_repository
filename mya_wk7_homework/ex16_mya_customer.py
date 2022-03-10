from ex16_mya_person import Person

class Customer():

    def __init__(self, name, age, DOB, email, contact_no):
        super(Employee, self).__init__(name, age, DOB)
        self._email = email
        self._contact_no = contact_no