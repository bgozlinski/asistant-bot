from fields import Name, Phone, Birthday
from datetime import datetime, timedelta


class Record:
    def __init__(self, name, phones=None, birthday=None):
        self.name = Name(name)
        self.phones = [Phone(phone) for phone in (phones or [])]
        self.birthday = Birthday(birthday) if birthday else None

    def days_to_birthday(self):
        if not self.birthday:
            return None

        today = datetime.today()
        next_birthday = datetime(today.year, self.birthday.value.month, self.birthday.value.day)
        if today > next_birthday:
            next_birthday = datetime(today.year + 1, self.birthday.value.month, self.birthday.value.day)
        return (next_birthday - today).days

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break

    def to_json(self):
        return {
            'name': self.name.value,
            'phones': [phone.value for phone in self.phones],
            'birthday': self.birthday.value.strftime('%Y-%m-%d') if self.birthday else None
        }

    @classmethod
    def from_json(cls, json_data):
        name = json_data['name']
        phones = json_data['phones']
        birthday = datetime.strptime(json_data['birthday'], '%Y-%m-%d').date() if json_data['birthday'] else None
        return cls(name=name, phones=phones, birthday=birthday)
