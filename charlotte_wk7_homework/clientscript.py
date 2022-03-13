from personfile import Person
from employeefile import Employee
from customerfile import Customer

# Person class

# creating object of a class
person_1 = Person('Charlotte', 'Stevenson', 25, 'F', 44766555441)

# Access property decorator
print(person_1.fullname)
# property setter
person_1.fullname = 'Georgia Farmer'
print(person_1.fullname)
# delete statement
del person_1.fullname
print(person_1.fullname)



# Employee class

# instantiating the employees
# emp_1 = Employee('Rosemary', 'Smith', 62, 'F', 44792999222, 'Software Developer', 50000, 'Junior')
# emp_2 = Employee('Fred', 'Williams', 25, 'M', 44922777111, 'Software Developer', 25000, 'Junior')
# emp_3 = Employee('Rachel', 'Meehan', 34, 'F', 44555271877, 'Cyber Security Analyst', 100000, 'Senior')
# emp_4 = Employee('Brian', 'Pointer', 55, 'M', 44287666544, 'Data Scientist', 150000, 'Senior')
#
# print(emp_1.work())
#
# emp_1.set_salary(40000)



# print(Employee.num_of_employees)
# print(Employee.salary_increase)
# This prints out None but I'm not sure why
# print(Employee.salary_raise(emp_1))

# print(help(Employee))




# Customer class

