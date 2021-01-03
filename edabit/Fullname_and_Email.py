# Create the instance attributes fullname and email in the Employee class.
# Given a person's first and last names:
# Form the fullname by simply joining the first and last name together,
# separated by a space.
# Form the email by joining the first and last name together with a .
# in between, and follow it with @company.com at the end.
# Make sure the entire email is in lowercase.

class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = self.firstname + " " + self.lastname
        self.email = self.firstname.lower() + "." + self.lastname.lower() + "@company.com"


emp_1 = Employee("John", "Smith")
print(emp_1.firstname)
print(emp_1.lastname)
print(emp_1.fullname)
print(emp_1.email)
