from fields import Name, Phone


class Record:
    def __init__(self, name, phones=None):
        self.name = Name(name)
        self.phones = [Phone(phone) for phone in (phones or [])]

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break
