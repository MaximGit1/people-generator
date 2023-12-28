from typing import List
import Fio
from random import randint as rnd
from string import ascii_uppercase
import datetime


class People:
    def __init__(self, sex: str = 'u', age: List[int] = [18, 28], payment_system: str = 'all'):
        """
        :param sex: str, 'u'-man/woman 'm'-man 'w'-woman
        :param age: List[int] - [from 'x' to 'y' years]. Age range
        :param payment_system: 'visa' - visa 'mc' - mastercard 'mir' - mir 'all' - visa/mastercard/mir systems
        """
        self.__sex = sex
        self.__age = age
        self.__payment_system = payment_system

    def generate(self) -> {}:
        fio = self.generate_fio()
        age = self.generate_age()
        phone = self.generate_phone_number()
        eng_fio = self.replace_abc(fio)
        birthday = self.generate_date_of_birth(age)
        email_ = self.generate_email({**eng_fio, **age, **birthday})
        card = self.generate_payment_card()
        # generate_hobby()
        # generate_address()
        return {**fio, **age, **phone, **eng_fio, **email_, **birthday, **card}

    def generate_fio(self):
        if self.__sex == 'u':
            sex = ['m', 'w'][rnd(0, 1)]
        else:
            sex = 'u'
        if self.__sex == 'm' or sex == 'm':
            name = Fio.man_name[rnd(0, len(Fio.man_name) - 1)]
            surname = Fio.surname[rnd(0, len(Fio.surname) - 1)]
            patronymic = self.__generate_patronymic('m')
        elif self.__sex == 'w' or sex == 'w':
            name = Fio.women_name[rnd(0, len(Fio.women_name) - 1)]
            surname = Fio.surname[rnd(0, len(Fio.surname) - 1)]
            patronymic = self.__generate_patronymic('w')
            if not surname in Fio.surname_exception: surname += 'а'
        else:
            raise TypeError('Very interesting error')
        sex = 'м' if sex == 'm' else 'ж'
        return {'name': name, 'surname': surname, 'patronymic': patronymic, 'sex': sex}

    @classmethod
    def __generate_patronymic(cls, sex: str) -> str:
        father_name = Fio.man_name[rnd(0, len(Fio.man_name) - 1)]
        if father_name[-1] in 'бвгджзклмнпрстфхцчшщ':
            patronymic = father_name + ('ович' if sex == 'm' else 'овна')
        elif father_name[-1] in 'ьй':
            patronymic = father_name[:-1] + ('евич' if sex == 'm' else 'евна')
        elif father_name[-1] in 'аеёиоуыэюя':
            patronymic = father_name[:-1] + ('ич' if sex == 'm' else 'ична')
        return patronymic

    def generate_age(self) -> dict:
        return {'age': rnd(self.__age[0], self.__age[1])}

    def generate_phone_number(self) -> dict:
        number = ''
        for i in range(9):
            number += str(rnd(0, 9))
        p_number = '89' + str(number)
        p_number_plus = '+79' + str(number)
        return {'phone_number': p_number, 'phone_number+': p_number_plus}

    @classmethod
    def generate_email(cls, fio: dict, email_type: tuple = ('@yandex.ru', '@mail.ru', '@gmail.com')) -> dict:
        rnd_symbols = '_019'
        rnd_ = rnd(0, 4)
        email_ = ''
        match rnd_:
            case 0:
                email_ += fio['en_surname'].lower() + fio['en_name'].lower()
            case 1:
                email_ += fio['en_surname'] + rnd_symbols[rnd(0, len(rnd_symbols) - 1)] + fio['en_name'].lower()
            case 2:
                email_ += fio['en_surname'] + fio['en_name'] + rnd_symbols[rnd(0, len(rnd_symbols) - 1)]
            case 3:
                email_ += fio['en_surname'] + ('_' if rnd(0, 1) else '') + fio['en_name'].lower() + str(fio['age'])
            case 4:
                email_ += fio['en_surname'] + ('_' if rnd(0, 1) else '') + fio['en_name'].lower() + str(
                    fio['birthday'][:4])
        email_ += email_type[rnd(0, (len(email_type) - 1))]
        return {'email': email_}

    @classmethod
    def replace_abc(cls, fio_dict: dict) -> dict:
        name, surname, patronymic = '', '', ''
        for i in fio_dict['name']:
            i = i.lower()
            name += Fio.ABC_REPLACE[i]
        for i in fio_dict['surname']:
            i = i.lower()
            surname += Fio.ABC_REPLACE[i]
        for i in fio_dict['patronymic']:
            i = i.lower()
            patronymic += Fio.ABC_REPLACE[i]
        fio = list(map(lambda i: i.capitalize(), [name, surname, patronymic]))
        return {'en_name': fio[0], 'en_surname': fio[1], 'en_patronymic': fio[2]}

    @classmethod
    def generate_date_of_birth(cls, age: dict) -> {}:
        today = datetime.date.today()
        year = today.year - age['age']
        mid_date = datetime.date(year=year, month=today.month, day=today.day)
        birthday = str(mid_date - datetime.timedelta(days=rnd(0, 265)))
        return {'birthday': birthday}

    def generate_payment_card(self) -> dict:
        number_card, payment, pin = '', '', ''
        if self.__payment_system == 'all':
            payment = ('mir', 'mc', 'visa')[rnd(0, 2)]
        if self.__payment_system == 'mir' or payment == 'mir':
            number_card += '22'
        elif self.__payment_system == 'mc' or payment == 'mc':
            number_card += '5'
        elif self.__payment_system == 'visa' or payment == 'visa':
            number_card += '4'
        else:
            raise NameError('There was an error selecting the card type')
        for _ in range(15):
            number_card += str(rnd(0, 9))
        if self.__payment_system == 'mir' or payment == 'mir':
            number_card = number_card[:16]
        for num in range(4):
            pin += str(rnd(0, 9))
        return {'number_card': number_card, 'pin': pin}
