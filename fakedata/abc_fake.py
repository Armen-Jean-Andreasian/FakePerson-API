from faker import Faker
from config import CountryData
from errors import CountryNotFoundError


class Fake:
    def __init__(self, country: str, language=None):
        if country not in CountryData.lang_initials_dict:
            raise CountryNotFoundError(country=country)

        country_initials: tuple = CountryData.lang_initials_dict[country]

        if language:
            country_initials = tuple(participant for participant in country_initials if language in participant)

        self.fake_object = Faker(country_initials[0])
