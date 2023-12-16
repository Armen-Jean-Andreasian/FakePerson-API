from fakedata.person.passport_data.fake_pass_data import PassportDataFakePerson


class PassportDataFakePersonMain(PassportDataFakePerson):
    def retrieve_passport_data(self):
        self.gain_data()

        passport_data = {
            "full_name": self.full_name,
            "sex": self.sex,
            "date_of_birth": self.date_of_birth,
            "passport_validity": self.passport_validity,
            "passport_number": self.passport_number
        }
        return passport_data
