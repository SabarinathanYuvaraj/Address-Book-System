class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact_details):
        self.contacts.append(contact_details)

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

    def display_contact(self, contact):
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
        self.address_book = AddressBook()

    def add_new_contact_from_console(self):
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip_code = input("Enter Zip Code: ")
        phone_number = input("Enter Phone Number: ")
        if not phone_number.isdigit():
            raise TypeError("the phone-number is not a number")
        if len(phone_number) != 10 :
            raise Exception("phone number is not length of exact 10")
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
        self.address_book.add_contact(new_contact)

    def edit_contact_from_console(self):
        first_name = input("Enter First Name of the contact to edit: ")
        last_name = input("Enter Last Name of the contact to edit: ")
        new_address = input("Enter New Address: ")
        new_city = input("Enter New City: ")
        new_state = input("Enter New State: ")
        new_zip_code = input("Enter New Zip Code: ")
        new_phone_number = input("Enter New Phone Number: ")
        new_email = input("Enter New Email: ")

        new_details = {
            'address': new_address,
            'city': new_city,
            'state': new_state,
            'zip_code': new_zip_code,
            'phone_number': new_phone_number,
            'email': new_email
        }
        self.address_book.edit_contact(first_name, last_name, new_details)

    def display_all_contacts(self):
        self.address_book.display_all_contacts()
        
    def if_you_want_to_edit_contact(self):
        respone = input("enter yes or no to edit the existing contact")
        if respone.lower() == "yes" :
            
            address_book_main.edit_contact_from_console()
            



address_book_main = AddressBookMain()

number_of_contact_insert = int(input("Enter the number of contacts to be inserted: "))
for i in range(number_of_contact_insert):
    address_book_main.add_new_contact_from_console()

address_book_main.display_all_contacts()


address_book_main.if_you_want_to_edit_contact()


address_book_main.display_all_contacts()

