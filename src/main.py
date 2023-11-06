from addressbook import AddressBook
from ui import ConsoleInterface
from record import Record
from datetime import datetime


def main():
    ui = ConsoleInterface()
    address_book = AddressBook()
    address_book.load_from_file()

    while True:
        ui.display_menu()
        choice = input('Please choose an option: ')

        if choice == '1':
            name = ui.get_input('Enter name: ')
            phones = ui.get_input('Enter phones (comma separated): ').split(",")
            birthday_input = ui.get_input('Enter birthday (YYYY-MM-DD) or leave blank: ')
            birthday = None
            if birthday_input:
                birthday = datetime.strptime(birthday_input, '%Y-%m-%d').date()
            record = Record(name, phones, birthday)
            address_book.add_record(record)

        elif choice == '2':
            name = ui.get_input('Enter record name: ')
            if name in address_book.data:
                phone = ui.get_input('Enter new phone: ')
                address_book.data[name].add_phone(phone)
            else:
                ui.display_message('Record not found.')

        elif choice == '3':
            name = ui.get_input('Enter record name: ')
            old_phone = ui.get_input('Enter old phone: ')
            new_phone = ui.get_input('Enter new phone: ')
            if name in address_book.data:
                address_book.data[name].edit_phone(old_phone, new_phone)
            else:
                ui.display_message('Record not found.')

        elif choice == '4':
            name = ui.get_input('Enter record name: ')
            phone = ui.get_input('Enter phone to remove: ')
            if name in address_book.data:
                address_book.data[name].remove_phone(phone)
            else:
                ui.display_message('Record not found.')

        elif choice == '5':
            query = ui.get_input('Enter name or phone number to find: ')
            results = address_book.find_record(query)
            if not results:
                ui.display_message('Found None')
            else:
                for result in results:
                    ui.display_record(result)

        elif choice == '6':
            if address_book.data:
                for name, record in address_book.data.items():
                    ui.display_record(record)
            else:
                ui.display_message('No records found.')

        elif choice == '7':
            address_book.save_to_file()

        elif choice == '8':
            break

        else:
            ui.display_message('Invalid choice. Please try again.')


if __name__ == "__main__":
    main()
