contacts = {}

def addcontact():
    contact_name = input('enter the name of the contact you want to add: ')
    contact_number = input('enter the number of the contact you want to add: ')
    contacts[contact_name] = contact_number
    print(f"{contact_name} added to the list of contacts with number {contact_number}")

def delete_contact():
    contact_name = input('enter the name of the contact you want to delete: ')
    if contact_name in contacts:
        del contacts[contact_name]
        print(f"contact {contact_name} deleted")
    else:
        print("no such contact exists")

def search_contacts():
    contact_name= input('enter the name of the contact you want to find: ')
    if contact_name in contacts:
        print(f"contact {contact_name}:{contacts[contact_name]}")
    else:
        print("no such contact exists")

def list_contacts():
    if not contacts:
        print('no contacts found')
    else:
        for contact_name,contact_number in contacts.items():
            print(f'{contact_name}:{contacts[contact_name]}')

while True:
    print("Welcome \nto add a contact press 1\nto remove a contact press 2\n"
          "to search a contact press 3\nto list all contacts press 4\nto quit 5")

    choice = input('please choose the desired operation: ')

    if choice == '1':
       addcontact()
    if choice == '2':
        delete_contact()
    if choice == '3':
        search_contacts()
    if choice == '4':
        list_contacts()
    if choice == '5':
        print("quitting")
        break