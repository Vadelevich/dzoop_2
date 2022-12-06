class Person:
    Min_age = 14
    Max_age = 150
    Min_weight = 25.0

    @classmethod
    def verify_ps(cls, arg):
        count_seria_nomer = 0
        count_space = 0
        for w in arg.split():
            if w.isdigit():
                count_seria_nomer += 1
                count_space += 1
                if count_seria_nomer == 2 and count_space == 1:
                    return arg
            else:
                raise ValueError('Серия и номер паспорта должны содержать только числа')
        if count_seria_nomer != 2: raise ValueError('Неверный формат паспорта')
        if count_space != 1: raise ValueError('Паспорт должен быть строкой')

    @classmethod
    def verify_weight(cls, arg):
        if type(arg) is float and cls.Min_weight <= arg:
            return arg
        else:
            raise ValueError('Вес должен быть вещественным числом от 25 и выше')

    @classmethod
    def verify_age(cls, arg):
        if type(arg) is int and cls.Min_age <= arg <= cls.Max_age:
            return arg
        else:
            raise ValueError('Возраст должен быть целым числом от 14 до 150')

    @classmethod
    def chek_fio(cls, arg):
        count_word = 0
        count_space = 0
        for w in arg.split():
            if w.isalpha():
                if len(w) < 1: raise ValueError('В ФИО должен быть хотя бы один символ')
                count_word += 1
                count_space += 1
                if count_word == 3 and count_space == 3:
                    return arg
            else:
                raise ValueError('В ФИО можно использовать только буквенные символы')
        if count_word != 3: raise ValueError('Неверный формат записи ФИО')
        if count_space != 3: raise ValueError('ФИО должно быть строкой')

    def __init__(self, fio, age, passport, weight):
        if self.chek_fio(fio):
            self.__fio = fio
        if self.verify_age(age):
            self.__age = age
        self.__passport = passport
        self.__weight = weight
    @property
    def fio(self):
        return self.__fio
    @fio.setter
    def fio(self, arg):
        self.__fio = arg
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, arg):
        self.__age = arg
    @property
    def passport(self):
        return self.__passport
    @passport.setter
    def passport(self, arg):
        self.__passport = arg
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, arg):
        self.__weight = arg


p = Person('Иванов Иван Иванович', 50, '0000 000000', 85.0)
p.passport = '1122 333444'
p.weight = 75.0
print(p.passport)
print(p.weight)