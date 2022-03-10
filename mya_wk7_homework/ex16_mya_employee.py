from ex16_mya_person import Person

class Employee():

    def __init__(self, name, age, DOB, employee_no, department):
        super(Employee, self).__init__(name, age, DOB)
        self._employee_no = employee_no
        self._department = department

