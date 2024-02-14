class Address_Book:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        if not phone_number.isdigit():
            raise TypeError("the phone-number is not a number")
        if len(phone_number) != 10 :
            raise Exception("phone number is not length of exact 10")
        self.phone_number = phone_number
        self.email = email

    def display_contact(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Address:", self.address)
        print("City:", self.city)
        print("State:", self.state)
        print("Zip Code:", self.zip_code)
        print("Phone Number:", self.phone_number)
        print("Email:", self.email)

contact1 = Address_Book("sabari", "nathan", "HSR-Layout", "Bangalore", "Karnataka", "123456", "9344159588", "sabari123.@gmail.com")
contact1.display_contact()
