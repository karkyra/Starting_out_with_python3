from employee import Employee
def main():

    header = Employee('Name', 'ID Number', 'Department', 'Job Title')
    emp1 = Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
    emp2 = Employee('Mark Jones', 39119, 'IT', 'Programmer')
    emp3 = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')

    print("___________________________________________________________________________________")
    print(header.get_name(),'\t\t\t', header.get_id_number(),'\t', header.get_department(),'\t\t',header.get_job_title())
    print("___________________________________________________________________________________")
    print(emp1.get_name(),'\t\t', emp1.get_id_number(),'\t\t', emp1.get_department(),'\t\t',emp1.get_job_title())
    print(emp2.get_name(),'\t\t', emp2.get_id_number(),'\t\t', emp2.get_department(),'\t\t\t',emp2.get_job_title())
    print(emp3.get_name(),'\t\t', emp3.get_id_number(),'\t\t', emp3.get_department(),'\t\t',emp3.get_job_title())
    print("___________________________________________________________________________________")


main()
