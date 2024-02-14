class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact_details):
        self.contacts.append(contact_details)

    def display_all_contacts(self):
        for contact in self.contacts:
            self.display_contact(contact)
        


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

    def display_all_contacts(self):
        self.address_book.display_all_contacts()


address_book_main = AddressBookMain()

number_of_contact_insert = int(input(" enter the number of contacts to inserted : "))
for i in range(number_of_contact_insert):
    address_book_main.add_new_contact_from_console()

address_book_main.display_all_contacts()
