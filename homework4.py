class Contact():
    def __init__(self, name ,phone_number):
        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def validate_phone_number(phone_number):
       if len(str(phone_number)) == 10:
           return True
       else:
           return False

class ContactList():
    all_contacts = []
    @classmethod
    def add_contact (cls,name, phone_number):
        if Contact.validate_phone_number(phone_number):
            das = Contact(name,phone_number)
            cls.all_contacts.append(das)
        else:
            print("ошибка!!!")

print(ContactList.all_contacts) # []

ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

# так как all_contacts является списком, можно пройти по нему циклом
for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)
    # Вася Пупкин 0700100200
    # Виктор Цой 0500123456

ContactList.add_contact("John Doe", "5551234")
# Error потому что количество цифр не подходит











