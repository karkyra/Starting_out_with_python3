import employee
import pickle

# Global constant for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

 # Global concstant for the filename
FILENAME = 'employee.dat'

 # main function
def main():
     # Load the existing contact dictionary and assign it to mycontacts
    mycontacts = load_contacts()

     # Initialize a variable for the user's choice
    choice = 0

     #Process menu selections until user
     # wants to quit the program

    while choice != QUIT:
         # Get the user's menu choice
         choice = get_menu_choice()

         # Process the choice
         if choice == LOOK_UP:
             look_up(mycontacts)

         elif choice == ADD:
             add(mycontacts)

         elif choice == CHANGE:
             change(mycontacts)

         elif choice == DELETE:
             delete(mycontacts)

    # Save the mycontacts dictionary
    save_contacts(mycontacts)


def load_contacts():

    try:
        # Open the employee.dat file
        input_file = open(FILENAME, 'rb')

        # Unpicke the dictionary
        contact_dct = pickle.load(input_file)

        # Close the employee.dat file

        input_file.close()

    except IOError:
        # Could not open the file, so create
        # an empty dictionary
        contact_dct = {}

    # Return the dictionary
    return contact_dct

# The get_menu_choice function displays the menu
# and gets a validated choice from the user

def get_menu_choice():
    print()
    print("Menu")
    print("------------------------------------")
    print("1. Look up a emloyee information")
    print("2. Add a new emplyee")
    print("3. Change existing employee information")
    print("4. Delete a employee information")
    print("5. Quit the program")
    print()

    # Get the user's choice
    choice = int(input('Enter your choice: '))

    # validated the choice
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter a valid choice: "))

    # Return the user choice
    return choice


# The look_up function looks up item in the specified dictionary
def look_up(mycontacts):

    name = input("Enter a name: ")

    # Look it up in the dictionary
    print(mycontacts.get(name, "That name is not found."))


# The add function adds a new entry into the specified dictionary
def add(mycontacts):
    # Get the employee info
    name = input('Name: ')
    id_number = input("ID Number: ")
    department = input("Department: ")
    job_title = input("Job Title: ")

    # Create a employee objects named entry

    entry = employee.Employee(name, id_number, department, job_title)

    # If the name does not exist in the dictionary,
    # add it as a key with the entry objects as the associated value
    if name not in mycontacts:
        mycontacts[name] = entry
        print('The entry has been added.')
    else:
        print('That name alredy exist')

# The change function changes an existing entry in the specified dictionary
def change(mycontacts):
    # Get a name to look up
    name = input('Enter a name: ')

    if name in mycontacts:
        # Get a new id_number
        id_number = input("Enter the new ID number: ")

        # Get a new department
        department = input("Enter a new department: ")

        # Get a new job_title
        job_title = input("Enter a new job title: ")

        entry = employee.Employee(name, id_number, department, job_title)

        # update the entry
        mycontacts[name] = entry
    else:
        print('that name is not found.')

# The delete function deletes an entry from the specified dictionary
def delete(mycontacts):
    # Get the name to look_up
    name = input("Enter a name: ")

    # If the name is found, delete the entry

    if name in mycontacts:
        del mycontacts[name]
        print('Entry deleted')
    else:
        print("That name is not found.")

# The save save_contacts function pickle the specified
# object and saves it to the contacts file

def save_contacts(mycontacts):
    # open the files for writing
    output_file = open(FILENAME, 'wb')

    # Picke the dictionary and save it
    pickle.dump(mycontacts, output_file)

    output_file.close()


# Call the main function
main()
