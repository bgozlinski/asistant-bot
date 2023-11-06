from abc import ABC, abstractmethod


class UserInterface(ABC):
    @abstractmethod
    def display_menu(self):
        pass

    @abstractmethod
    def get_input(self, prompt):
        pass

    @abstractmethod
    def display_message(self, message):
        pass

    @abstractmethod
    def display_record(self, record):
        pass


class ConsoleInterface(UserInterface):
    def display_menu(self):
        print('\nMenu:')
        print('1. Add record')
        print('2. Add phone to record')
        print('3. Edit phone in record')
        print('4. Remove phone from record')
        print('5. Find record')
        print('6. Show all records')
        print('7. Save address book to file')

        print('\n8. Exit')

    def get_input(self, prompt):
        return input(prompt)

    def display_message(self, message):
        print(message)

    def display_record(self, record):
        days_to_birthday = record.days_to_birthday()
        birthday_msg = f", Days to birthday: {days_to_birthday}" if days_to_birthday is not None else ""
        print(f'Name: {record.name.value} Phones: {[phone.value for phone in record.phones]}{birthday_msg}')

