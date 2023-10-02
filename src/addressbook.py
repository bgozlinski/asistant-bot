import json
from record import Record
from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find_record(self, query):
        results = []

        for name, record in self.data.items():
            if query.lower() in name.lower():
                results.append(record)
            else:
                for phone in record.phones:
                    if query in phone.value:
                        results.append(record)
                        break

        return results

    def iterator(self, N):
        records = list(self.data.values())
        for i in range(0, len(records), N):
            yield records[i:i+N]

    def save_to_file(self, filename='address_book.json'):
        with open(filename, 'w') as f:
            json_data = [record.to_json() for record in self.data.values()]
            json.dump(json_data, f)

    def load_from_file(self, filename='address_book.json'):
        try:
            with open(filename, 'r') as f:
                json_data = json.load(f)
                self.data = {record['name']: Record.from_json(record) for record in json_data}
        except FileNotFoundError:
            print(f"Warning: Could not find file '{filename}'. A new address book will be created.")