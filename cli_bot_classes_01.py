from collections import UserDict


class Field:
    """Загальна логіка"""
    def __init__(self):
        self.dct_total = {}

    def dct_total_update(self, dct):
        """Оновлює словник, додаючи в нього нові пари ключ-значення"""
        self.dct_total.update(dct)
        return self.dct_total

    def find(self, name):
        """Виконує пошук телефону по імені"""
        return self.dct_total[name]


class AddressBook(UserDict):
    """Містить логіку пошуку в телефонній книзі"""

    def __init__(self):
        super().__init__()
        self.data = {}

    def add_record(self, record):
        """Додає дані у self.data"""
        self.data[record.name] = record.data
        return self.data


class Record:
    """
    Відповідає за логіку додавання/видалення/редагування необов'язкових
    полів та зберігання обов'язкового поля name
    """

    def __init__(self, name, data):
        self.name = name
        self.data = data

    def update(self, data):
        """Оновлює self.data"""
        self.data = data
        return self.data


class Name:
    """Містить обов'язкове поле з ім'ям"""
    name = ''


class Phone:
    """Містить необов'язкове поле з телефоном"""
    lst_phones = []


# Створимо та занесемо першого користувача до поля data
user_1_name = Name()
user_1_name.name = 'Garry'
user_1_phones = Phone()
user_1_phones.lst_phones = ['+111', '+222']
changing = Record(user_1_name.name, user_1_phones.lst_phones)
address_book = AddressBook()
address_book.add_record(changing)
# Додамо дані до загального словника
total_dct = Field()
total_dct_f = total_dct.dct_total_update(address_book)
print(total_dct_f)

# Створимо та занесемо другого користувача до поля data
user_2_name = Name()
user_2_name.name = 'Tom'
user_2_phones = Phone()
user_2_phones.lst_phones = ['+333', '+444']
changing = Record(user_2_name.name, user_2_phones.lst_phones)
address_book = AddressBook()
address_book.add_record(changing)
# Додамо дані до загального словника
total_dct_f = total_dct.dct_total_update(address_book)
print(total_dct_f)

# Змінемо номери телефонів у user_2
changing.update(['+330', '+440'])
address_book.add_record(changing)
# Оновимо дані у загальному словнику
total_dct_f = total_dct.dct_total_update(address_book)
print(total_dct_f)

# Виконаємо пошук по адресній книзі
print(total_dct.find('Tom'))
print(total_dct.find('Garry'))
