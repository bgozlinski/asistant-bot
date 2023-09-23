class Field:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


class Name(Field):
    pass


class Phone(Field):

    @Field.value.setter
    def value(self, new_value):
        self._value = new_value


class Birthday(Field):
    @Field.value.setter
    def value(self, new_value):
        self._value = new_value
