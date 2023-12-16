from fakedata.abc_fake import Fake


class PersonalDataFakePersonMain(Fake):
    def retrieve_personal_data(self):
        personal_data = {
            "email": self.fake_object.free_email(),
            "address": self.fake_object.address().replace("\n", ", "),
            "company": self.fake_object.company(),
            # "phone_number": self.fake_object.basic_phone_number()
        }
        return personal_data
