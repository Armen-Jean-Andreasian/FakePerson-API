import random
from fakedata.abc_fake import Fake


class FakePassportDataBase(Fake):
    def __init__(self, country):
        super().__init__(country)
        self.passport: list = self.fake_object.passport_full().split()
        # ['David', 'Bailey', 'M', '17', 'Dec', '1990', '31', 'Mar', '2020', '31', 'Mar', '2030', 'C55019016']

        self.full_name = None
        self.sex = None
        self.date_of_birth = None
        self.passport_validity = None
        self.passport_number = None

    def __retrieve_full_name(self):
        self.full_name = " ".join(self.passport[0:2])
        return self

    def __retrieve_sex(self):
        self.sex = "Female" if self.passport[2] == "F" else "Male"
        return self

    def __retrieve_passport_validity(self):
        self.passport_validity = " ".join(self.passport[6:12])  # ['31', 'Jul', '2021', '31', 'Jul', '2031']
        return self

    def __retrieve_date_of_birth(self):
        year_of_birth = int(self.passport[5])
        passport_given = int(self.passport[8])
        age_of_consent = 16

        if passport_given - year_of_birth < age_of_consent:
            self.passport[5] = str(random.randint(1900, passport_given))

        self.date_of_birth = " ".join(self.passport[3:6])
        return self

    def __retrieve_passport_number(self):
        self.passport_number = self.passport[-1]
        return self

    def gain_data(self):
        self.__retrieve_full_name()
        self.__retrieve_sex()
        self.__retrieve_passport_validity()
        self.__retrieve_date_of_birth()
        self.__retrieve_passport_number()
        return self
