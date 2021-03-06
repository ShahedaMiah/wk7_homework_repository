from personfile import Person
from employeefile import Employee
from customerfile import Customer

# print(help(Person))
# print(help(Employee))
# print(help(Customer))

# check for class inheritance
# print(issubclass(Employee, Person))     #True
# print(issubclass(Customer, Person))     #True


# # Person class

# # creating object of a class
# person_1 = Person('Sienna', 'Stevenson', 25, 'F', 44766555441)
# person_2 = Person('Mark', 'Wright', 54, 'M', 44777554499)
#
# # Access property decorator
# print(person_1.fullname)
# # property setter
# person_1.fullname = 'Georgia Farmer'
# print(person_1.fullname)
# # delete statement
# del person_1.fullname
# print(person_1.fullname)
#
# person_2.set_age(24)
# print(person_2)


# # Employee class
#
# # instantiating the employees
# emp_1 = Employee('Rosemary', 'Smith', 62, 'F', 44792999222, 'Software Developer', 50000, 'Junior')
# emp_2 = Employee('Fred', 'Williams', 25, 'M', 44922777111, 'Software Developer', 25000, 'Junior')
# emp_3 = Employee('Rachel', 'Meehan', 34, 'F', 44555271877, 'Cyber Security Analyst', 100000, 'Senior')
# emp_4 = Employee('Brian', 'Pointer', 55, 'M', 44287666544, 'Data Scientist', 150000, 'Senior')
# #
# # Trying out the methods in the Employee class
# emp_4.work()
# #
# # set salary
# emp_1.set_salary(40000)
# print(emp_1.get_salary())
#
# # to show that employees cannot have a salary > 250000
# # emp_1.set_salary(300000)
# # print(emp_1.get_salary())
#
# emp_1.calculate_salary_increase()
# emp_2.calculate_salary_increase()
# print(emp_1.calculate_salary_increase())
# print(emp_2.calculate_salary_increase())
#
# print(emp_3.show_details())
#
# print(Employee.num_of_employees)
#
# print(Employee.calculate_salary_increase(emp_3))
#



# Customer class
#
# customer_1 = Customer('Charlotte', 'Stevenson', 25, 'F', 44766555441, None)
# customer_2 = Customer('Rosie', 'Parkins', 17, 'F', 44666777100, None)
#
# # runs the add_to_shopping_list() and adds to shopping_list for customer_1
# Customer.add_to_shopping_list(customer_1)
# # print(customer_1.shopping_list)
# Customer.age_restriction_check(customer_1)
# Customer.calculate_shopping_cost(customer_1)
#
#
# Customer.add_to_shopping_list(customer_2)
# # print(customer_2.shopping_list
# Customer.age_restriction_check(customer_2)
# Customer.calculate_shopping_cost(customer_2)