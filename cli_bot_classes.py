from collections import UserDict


class Field:
    """Загальна логіка"""
    def __init__(self):
        self.dct_total = {}

    def dct_total_update(self, dct):
        """Оновлює словник, додаючи в нього нові пари ключ-значення"""
        self.dct_total.update(dct)
        return self.dct_total

    def dct_total_change(self, dct):
        """Виконює заміну вмісту словника"""
        self.dct_total = dct
        return self.dct_total


class AddressBook(UserDict):
    """Містить логіку пошуку в телефонній книзі"""

    def add_record(self, lst):
        """Додає Record у self.data"""
        self.data[lst[0]] = lst[1]
        return self.data

    def find_phone_by_name(self, dct, name):
        """Шукає телефон по імені"""
        for key, value in dct.items():
            if key == name:
                return f'{key}: {value}'


class Record:
    """
    Відповідає за логіку додавання/видалення/редагування необов'язкових
    полів та зберігання обов'язкового поля name
    """

    def add_new_contact(self, new_name, new_phone_lst):
        """Повертає ім'я та список телефонів"""
        lst = [new_name, new_phone_lst]
        return lst

    def del_phone(self, dct, phone_must_be_deleted):
        """Видаляє телефонний номер"""
        for value in dct.values():
            for i in value:
                if i == phone_must_be_deleted:
                    value.remove(i)
        return dct

    def edit_phone(self, dct, phone_must_be_edit, new_phone):
        """Редагує телефонний номер"""
        for value in dct.values():
            for i in value:
                if i == phone_must_be_edit:
                    value.remove(i)
                    value.append(new_phone)
        return dct


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
changing = Record()
lst_with_new_dates = changing.add_new_contact(user_1_name.name, user_1_phones.lst_phones)
address_book = AddressBook()
address_book_data = address_book.add_record(lst_with_new_dates)
# Оновимо словник класу Field (загальна телефона база даних)
total_dct = Field()
total_dct_f = total_dct.dct_total_update(address_book_data)
print(total_dct_f)
# Видалимо номер телефону "+111" (зміни відбудуться у словнику класу Field (загальна телефона база даних))
del_number = changing.del_phone(total_dct_f, '+111')
print(total_dct.dct_total_change(del_number))
# Замінемо телефон "+222" на "+2220"
edit_number = changing.edit_phone(total_dct_f, '+222', '+2220')
print(total_dct_f)

# Створимо та занесемо другого користувача до поля data
user_2_name = Name()
user_2_name.name = 'Tom'
user_2_phones = Phone()
user_2_phones.lst_phones = ['+333', '+444']
lst_with_new_dates = changing.add_new_contact(user_2_name.name, user_2_phones.lst_phones)
address_book_data = address_book.add_record(lst_with_new_dates)
print(total_dct.dct_total_update(address_book_data))

# Створимо та занесемо третього користувача до поля data
user_3_name = Name()
user_3_name.name = 'Babba'
user_3_phones = Phone()
user_3_phones.lst_phones = ['+555', '+777']
lst_with_new_dates = changing.add_new_contact(user_3_name.name, user_3_phones.lst_phones)
address_book_data = address_book.add_record(lst_with_new_dates)
print(total_dct.dct_total_update(address_book_data))

# Знайдемо в адрусній книзі телефони для імені 'Babba'
finding_number = address_book.find_phone_by_name(total_dct_f, 'Babba')
print(finding_number)

