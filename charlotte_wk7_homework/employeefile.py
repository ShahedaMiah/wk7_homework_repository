from personfile import Person


class Employee(Person):

    num_of_employees = 0
    salary_increase = 1.05

    def __init__(self, first_name, last_name, age, gender, contact_number, job_title, salary, level):
        super().__init__(first_name, last_name, age, gender, contact_number)
        self.job_title = job_title
        self._salary = salary
        self.level = level

        Employee.num_of_employees += 1

    # salary getter
    def get_salary(self):
        return self._salary

    # salary setter
    def set_salary(self, value):
        if value != int(value):
            raise TypeError("salary must be an integer")
        if 0 <= value <= 250000:
            self._salary = int(value)
        else:
            raise ValueError("salary must be between 0 and 250000 inclusive")

    def show_details(self):
        return "Name: ", self.fullname, 'Salary: ', self._salary

    def work(self):
        print(f"{self.fullname}, 'is a', {self.job_title}")

    def calculate_salary(self):
        if self._gender == 'F':
            return int(self._salary * self.salary_increase)
        else:
            return self._salary

    # def requesting_holiday(self):
    #     print(self.fullname, 'is requesting holiday from', {} to {}.format(input(date), input(date)))
#         if
# else


emp_1 = Employee('Rosemary', 'Smith', 62, 'F', 44792999222, 'Software Developer', 50000, 'Junior')

emp_1.set_salary(40000)
print(emp_1.get_salary())
#
# emp_1.set_salary(300000)
# print(emp_1.get_salary())

emp_1.calculate_salary()
print(emp_1.calculate_salary())