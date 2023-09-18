from addressbook import AddressBook
from record import Record


def main():
    address_book = AddressBook()

    while True:
        print('\nMenu:')
        print('1. Add record')
        print('2. Add phone to record')
        print('3. Edit phone in record')
        print('4. Remove phone from record')
        print('5. Find record')
        print('6. Show all records')
        print('\n7. Exit')

        choice = input('Please choose an option: ')

        if choice == '1':
            name = input('Enter name: ')
            phones = input('Enter phones (comma separated): ').split(",")
            record = Record(name, phones)
            address_book.add_record(record)

        elif choice == '2':
            name = input('Enter record name: ')
            if name in address_book.data:
                phone = input('Enter new phone: ')
                address_book.data[name].add_phone(phone)
            else:
                print('Record not found.')

        elif choice == '3':
            name = input('Enter record name: ')
            old_phone = input('Enter old phone: ')
            new_phone = input('Enter new phone: ')
            if name in address_book.data:
                address_book.data[name].edit_phone(old_phone, new_phone)
            else:
                print('Record not found.')

        elif choice == '4':
            name = input('Enter record name: ')
            phone = input('Enter phone to remove: ')
            if name in address_book.data:
                address_book.data[name].remove_phone(phone)
            else:
                print('Record not found.')

        elif choice == '5':
            query = input('Enter name or phone number to find: ')
            results = address_book.find_record(query)
            if not results:
                print('Found None')
            else:
                for result in results:
                    print(f'Found: {result.name.value}, Phones: {[phone.value for phone in result.phones]}')

        elif choice == '6':
            if address_book.data:
                for name, record in address_book.data.items():
                    print(f'Name: {name} Phones: {[phone.value for phone in record.phones]}')
            else:
                print('No records found.')
        elif choice == '7':
            break

        else:
            print('Invalid choice. Please try again.')


if __name__ == "__main__":
    main()
