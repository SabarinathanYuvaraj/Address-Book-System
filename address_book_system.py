class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact_details):
        self.contacts.append(contact_details)
        print("The Contact Saved Successfully!!")

    def display_all_contacts(self):
        for contact in self.contacts:
            self.display_contact(contact)

    def edit_contact(self, first_name, last_name, new_details):
        for contact in self.contacts:
            if contact['first_name'] == first_name and contact['last_name'] == last_name:
                contact.update(new_details)
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, first_name, last_name):
        for contact in self.contacts:
            if contact['first_name'] == first_name and contact['last_name'] == last_name:
                self.contacts.remove(contact)
                print("The Contact is Deleted")
                return
        print("The Contact is not Found")
        
    def display_contact(self, contact):
        print("--------------------------")
        print("First Name:", contact['first_name'])
        print("Last Name:", contact['last_name'])
        print("Address:", contact['address'])
        print("City:", contact['city'])
        print("State:", contact['state'])
        print("Zip Code:", contact['zip_code'])
        print("Phone Number:", contact['phone_number'])
        print("Email:", contact['email'])
        print("--------------------------")


class AddressBookMain:
    def __init__(self):
        self.address_books = {}
        self.address_book = AddressBook()

    def add_new_address_book(self, name):
        if name not in self.address_books:
            self.address_books[name] = AddressBook()
            print(f"Address book '{name}' created successfully.")
            user_input = int(input("Enter The Number \n 0) To Create New AddressBook \n 1) To Add New Contact To The AddressBook  \n 2) To  Update  The AddressBook \n 3) To Delete Contact To The AddressBook  \n 4) To Display Contact in the AddressBook \n Enter Any Other Keys To Not Continue Any Operations: "))
            handle_user_input(user_input)
        else:
            print(f"Address book '{name}' already exists.")
            user_input = int(input("Enter The Number \n 0) To Create New AddressBook \n 1) To Add New Contact To The AddressBook  \n 2) To  Update  The AddressBook \n 3) To Delete Contact To The AddressBook  \n 4) To Display Contact in the AddressBook \n Enter Any Other Keys To Not Continue Any Operations: "))
            handle_user_input(user_input)

    def add_new_contact_from_console(self, name):           
        if name in self.address_books:
            address_book = self.address_books[name]
            number_of_contacts = int(input("Enter the number of contacts to be inserted: "))
            for _ in range(number_of_contacts):
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                address = input("Enter Address: ")
                city = input("Enter City: ")
                state = input("Enter State: ")
                zip_code = input("Enter Zip Code: ")
                phone_number = input("Enter Phone Number: ")
                if not phone_number.isdigit():
                    raise TypeError("The phone number is not a number")
                if len(phone_number) != 10:
                    raise ValueError("Phone number is not of length 10")
                email = input("Enter Email: ")
                print("--------------------------")

                new_contact = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'address': address,
                    'city': city,
                    'state': state,
                    'zip_code': zip_code,
                    'phone_number': phone_number,
                    'email': email
                }
                address_book.add_contact(new_contact)
                print("Contact added successfully.")
        else:
            print(f"Address book '{name}' does not exist.")

    def edit_contact_from_console(self, name):
        if name in self.address_books:
            address_book = self.address_books[name]
            first_name = input("Enter First Name of the contact to edit: ")
            last_name = input("Enter Last Name of the contact to edit: ")
            new_address = input("Enter New Address: ")
            new_city = input("Enter New City: ")
            new_state = input("Enter New State: ")
            new_zip_code = input("Enter New Zip Code: ")
            new_phone_number = input("Enter New Phone Number: ")
            if not new_phone_number.isdigit():
                raise TypeError("The new phone number is not a number")
            if len(new_phone_number) != 10:
                raise ValueError("New phone number is not of length 10")
            new_email = input("Enter New Email: ")

            new_details = {
                'address': new_address,
                'city': new_city,
                'state': new_state,
                'zip_code': new_zip_code,
                'phone_number': new_phone_number,
                'email': new_email
            }
            address_book.edit_contact(first_name, last_name, new_details)
            address_book.display_all_contacts()
        else:
            print(f"Address book '{name}' does not exist.")

    def delete_contact(self, name):
        if name in self.address_books:
            address_book = self.address_books[name]
            first_name = input("Enter the first name of user to delete : ")
            last_name = input("For security purpose, Enter the last name of user to delete : ")
            address_book.delete_contact(first_name, last_name)
            address_book.display_all_contacts()
        else:
            print(f"Address book '{name}' does not exist.")

    def display_all_contacts(self, name):
        if name in self.address_books:
            address_book = self.address_books[name]
            address_book.display_all_contacts()
        else:
            print(f"Address book '{name}' does not exist.")


address_book_main = AddressBookMain()
def handle_user_input(user_input):
    if user_input >= 0 and user_input <= 4:
        if user_input == 0:
            address_book_main.add_new_address_book("Friends")
            address_book_main.add_new_address_book("Family")
        if user_input == 1:
            address_book_main.add_new_contact_from_console("Friends")
            address_book_main.add_new_contact_from_console("Family")
        if user_input == 2:
            address_book_main.edit_contact_from_console("Friends")
        if user_input == 3:
            address_book_main.delete_contact("Friends")
        if user_input == 4:
            address_book_main.display_all_contacts("Friends")
            address_book_main.display_all_contacts("Family")
    else:
        print("The given user input is invalid")


user_input = int(input("Enter The Number \n 0) To Create New AddressBook \n 1) To Add New Contact To The AddressBook  \n 2) To  Update  The AddressBook \n 3) To Delete Contact To The AddressBook  \n 4) To Display Contact in the AddressBook \n Enter Any Other Keys To Not Continue Any Operations: "))
handle_user_input(user_input)