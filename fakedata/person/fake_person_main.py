from fakedata.person.passport_data.fake_pass_data_main import PassportDataFakePersonMain
from fakedata.person.personal_data.personal_data_main import PersonalDataFakePersonMain
from datetime import datetime


class FakePersonMain(PersonalDataFakePersonMain, PassportDataFakePersonMain):
    def __init__(self, country):
        super().__init__(country)

        self.data = dict()
        self.data.update(self.retrieve_passport_data())
        self.data.update(self.retrieve_personal_data())


class FakePerson(FakePersonMain):
    @property
    def get_all_data(self):
        return self.data

    @property
    def get_passport_data(self):
        return self.retrieve_passport_data()

    @property
    def get_personal_data(self):
        return self.retrieve_personal_data()

    @property
    def get_full_name(self):
        return self.data["full_name"]

    @property
    def get_sex(self):
        return self.data["sex"]

    @property
    def get_date_of_birth(self):
        return self.data["date_of_birth"]

    @property
    def get_age(self):
        date_of_birth = self.data["date_of_birth"]
        dob_object = datetime.strptime(date_of_birth, '%d %b %Y')
        current_date = datetime.now()

        age = current_date.year - dob_object.year - (
                (current_date.month, current_date.day) < (dob_object.month, dob_object.day))
        return age

    @property
    def get_passport_number(self):
        return self.data["passport_number"]

    @property
    def get_email(self):
        return self.data["email"]

    @property
    def get_address(self):
        return self.data["address"]

    @property
    def get_company(self):
        return self.data["company"]

    @property
    def get_phone_number(self):
        return self.data["phone_number"]
