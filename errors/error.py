from faker.providers.date_time import Provider


class CountryNotFoundError(Exception):
    country_list = [country.name for country in Provider.countries]
    country_list.sort()

    __slots__ = ["country"]

    def __init__(self, country):
        self.country = country

    def __str__(self):
        return f"Country '{self.country}' wasn't found. Available countries: {self.country_list}"
