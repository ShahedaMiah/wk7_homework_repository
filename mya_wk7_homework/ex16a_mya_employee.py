from ex16a_mya_person import Person

class Employee(Person):

    def __init__(self, name, gender, preferred_pronoun, dob, address, employee_no, department):
        super().__init__(name, gender, preferred_pronoun)
        self._dob = dob
        self._home_address = address
        self._employee_no = employee_no
        self._department = department


    def start_employment(self, date):
        self._start_date = date
        return "\n Employment Start Date: " + str(self._start_date)

    def end_employment(self, date):
        self._leave_date = date
        return '\n Employment End Date: ' + str(self.end_employment)

    def work_email(self, email):
        self._work_email = email
        return '\n Work Email: ' + str(self._work_email)

    def line_manager(self, manager):
        self._line_manager = manager
        return '\n Line Manager: ' + str(self._line_manager)

    def salary(self, salary):
        self._salary = salary
        return '\n Salary: ' + str(self._salary)

    def __str__(self):
        return super().__str__() + '\n' "DOB: " + str(self._dob) + '\n' "Home Address: " +str(self._home_address) + '\n' "Employee No: " + str(self._employee_no) + '\n' "Department: " + str(self._department)

def main():
    shaheda = Employee("Shaheda", "female", "she/her", "17/12/1980", "2 Kirton Close W4 5UU", "121", "development")

    print(shaheda, shaheda.start_employment(11/12/2022), shaheda.salary(45000))

if __name__ == "__main__":
    main()