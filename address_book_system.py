class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact_details):
        first_name = contact_details['first_name']
        last_name = contact_details['last_name']
        phone_number = contact_details['phone_number']
        
        for contact in self.contacts:
            if (contact['first_name'] == first_name and
                contact['last_name'] == last_name and
                contact['phone_number'] == phone_number):
                print("The contact already exists.")
                return

        self.contacts.append(contact_details)
        print("The Contact Saved Successfully!!")
        # print(self.contacts)

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
                return "The Contact is Deleted"
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
    address_book_name = ""
    person=[]
    person_by_city={}
    person_by_state={}

    def __init__(self):
        self.address_books = {}
        self.address_book = AddressBook()
        

    def add_new_address_book(self):
        name = input("Enter The New AddressBook Name : ")
        AddressBookMain.address_book_name = name
        if AddressBookMain.address_book_name not in self.address_books:
            self.address_books[AddressBookMain.address_book_name] = AddressBook()
            print(f"Address book '{AddressBookMain.address_book_name}' created successfully.")
            user_input = int(input("Enter The Number \n 0) To Create New AddressBook \n 1) To Add New Contact To The AddressBook \n 2) To Update  Contact in The AddressBook \n 3) To  Delete The Contact in The AddressBook  \n 4) To Display Contact in the AddressBook \n 5)search person by city and state \n Enter Any Other Keys To Not Continue Any Operations: "))
            handle_user_input(user_input)
        else:
            print(f"Address book '{AddressBookMain.address_book_name}' already exists.")
            user_input = int(input("Enter The Number \n 0) To Create New AddressBook \n 1) To Add New Contact To The AddressBook \n 2) To Update  Contact in The AddressBook \n 3) To  Delete The Contact in The AddressBook  \n 4) To Display Contact in the AddressBook \n 5)search person by city and state \n Enter Any Other Keys To Not Continue Any Operations: "))
            handle_user_input(user_input)

    def add_new_contact_from_console(self):           
        if AddressBookMain.address_book_name in self.address_books:
            address_book = self.address_books[AddressBookMain.address_book_name]
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
            user_input = int(input("Enter The Number \n 0) To Create New AddressBook \n 1) To Add New Contact To The AddressBook \n 2) To Update  Contact in The AddressBook \n 3) To  Delete The Contact in The AddressBook  \n 4) To Display Contact in the AddressBook \n 5)search person by city and state \n Enter Any Other Keys To Not Continue Any Operations: "))
            handle_user_input(user_input)

                
        else:
            print(f"Address book '{AddressBookMain.address_book_name}' does not exist.")

    def edit_contact_from_console(self):
        if AddressBookMain.address_book_name in self.address_books:
            address_book = self.address_books[AddressBookMain.address_book_name]
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
            user_input = int(input("Enter The Number \n 0) To Create New AddressBook \n 1) To Add New Contact To The AddressBook \n 2) To Update  Contact in The AddressBook \n 3) To  Delete The Contact in The AddressBook  \n 4) To Display Contact in the AddressBook \n 5)search person by city and state \n Enter Any Other Keys To Not Continue Any Operations: "))
            handle_user_input(user_input)

        else:
            print(f"Address book '{AddressBookMain.address_book_name}' does not exist.")

    def delete_contact(self):
        if AddressBookMain.address_book_name in self.address_books:
            address_book = self.address_books[AddressBookMain.address_book_name]
            first_name = input("Enter the first name of user to delete : ")
            last_name = input("For security purpose, Enter the last name of user to delete : ")
            address_book.delete_contact(first_name, last_name)
            address_book.display_all_contacts()
            user_input = int(input("Enter The Number \n 0) To Create New AddressBook \n 1) To Add New Contact To The AddressBook \n 2) To Update  Contact in The AddressBook \n 3) To  Delete The Contact in The AddressBook  \n 4) To Display Contact in the AddressBook \n 5)search person by city and state \n Enter Any Other Keys To Not Continue Any Operations: "))
            handle_user_input(user_input)

        else:
            print(f"Address book '{AddressBookMain.address_book_name}' does not exist.")

    def display_all_contacts(self):
        if AddressBookMain.address_book_name in self.address_books:
            address_book = self.address_books[AddressBookMain.address_book_name]
            address_book.display_all_contacts()
            user_input = int(input("Enter The Number \n 0) To Create New AddressBook \n 1) To Add New Contact To The AddressBook \n 2) To Update  Contact in The AddressBook \n 3) To  Delete The Contact in The AddressBook  \n 4) To Display Contact in the AddressBook \n 5)search person by city and state \n Enter Any Other Keys To Not Continue Any Operations: "))
            handle_user_input(user_input)

        else:
            print(f"Address book '{AddressBookMain.address_book_name}' does not exist.")
            
    def search_person_by_state_or_city_name(self, state_name, city_name):
        found = False
        print("Search Results:")
        for address_book_name, address_book in self.address_books.items():
            for contact in address_book.contacts:
                if contact['state'] == state_name and contact['city'] == city_name:
                    found = True
                    self.address_book.display_contact(contact)
        if not found:
            print("No contacts found in the specified location.")
        user_input = int(input("Enter The Number \n 0) To Create New AddressBook \n 1) To Add New Contact To The AddressBook \n 2) To Update  Contact in The AddressBook \n 3) To  Delete The Contact in The AddressBook  \n 4) To Display Contact in the AddressBook \n 5)search person by city and state \n Enter Any Other Keys To Not Continue Any Operations: "))
        handle_user_input(user_input)

    def view_persons_by_City_and_State(self):
        self.person_by_state = {}
        self.person_by_city = {}

        for address_book_name, address_book in self.address_books.items():
            for contact in address_book.contacts:
                if contact['state'] not in self.person_by_state:
                    self.person_by_state[contact['state']] = []
                self.person_by_state[contact['state']].append(contact['first_name'])
                
                if contact['city'] not in self.person_by_city:
                    self.person_by_city[contact['city']] = []
                self.person_by_city[contact['city']].append(contact['first_name'])

        print("Persons by State:")
        print(self.person_by_state)

        print("Persons by City:")
        print(self.person_by_city)


                

address_book_main = AddressBookMain()
def handle_user_input(user_input): 
    if user_input >= 0 and user_input <= 6:
        if user_input == 0:
            address_book_main.add_new_address_book()            
        if user_input == 1:
            address_book_main.add_new_contact_from_console()
        if user_input == 2:
            address_book_main.edit_contact_from_console()
        if user_input == 3:
            address_book_main.delete_contact()
        if user_input == 4:
            address_book_main.display_all_contacts()
        if user_input == 5:
            state_name = input("Enter the State name : ")
            city_name = input("Enter the City name : ")
            address_book_main.search_person_by_state_or_city_name(state_name,city_name)
        if user_input == 6:
            address_book_main.view_persons_by_City_and_State()
    else:
        print("The given user input is invalid")


user_input = int(input("Enter The Number \n 0) To Create New AddressBook \n 1) To Add New Contact To The AddressBook \n 2) To Update  Contact in The AddressBook \n 3) To  Delete The Contact in The AddressBook  \n 4) To Display Contact in the AddressBook \n 5)search person by city and state \n Enter Any Other Keys To Not Continue Any Operations: "))
handle_user_input(user_input)