class Person:
    # constructor
    def __init__(self, first_name, last_name, age, gender, contact_number):
        # data members
        self._first_name = str(first_name)
        self._last_name = str(last_name)
        self.__age = age
        self._gender = gender.upper()
        self.__contact_number = contact_number

    # @property decorator - declares the method as a property. @property decorator applied to the fullname() method.
    # This method must return the value of the property.
    # The fullname() method is used as a property to get the value of the _first_name and _last_name attributes.
    @property
    def fullname(self):
        return '{} {}'.format(self._first_name, self._last_name)

    # property name.setter decorator
    # the setter method must take in the name argument that can be used to assign to underlying private attribute.
    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(' ')
        self._first_name = first_name
        self._last_name = last_name
        # name = '{} {}'.format(self._first_name, self._last_name)

    # property name.deleter decorator
    @fullname.deleter
    def fullname(self):
        print('Deleting name...')
        self._first_name = None
        self._last_name = None

    # setter method
    def set_age(self, age):
        self.__age = age

    def __str__(self):
        return "Name: " + self._first_name + self._last_name + "Age: " + self.__age + "Gender: " + self._gender + "Contact number: " + self.__contact_number


person_1 = Person('Charlotte', 'Stevenson', 25, 'F', 44766555441)
#
# # Access property decorator
print(person_1.fullname)
# # property setter
person_1.fullname = 'Georgia Farmer'
print(person_1.fullname)
# # delete statement
# del person_1.fullname
# print(person_1.fullname)