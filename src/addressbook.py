from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find_record(self, query):
        results = []

        for name, record in self.data.items():
            if query.lower() == name.lower():
                results.append(record)
                continue

            for phone in record.phones:
                if query == phone.value:
                    results.append(record)
                    break

        return results

    def iterator(self, N):
        records = list(self.data.values())
        for i in range(0, len(records), N):
            yield records[i:i+N]