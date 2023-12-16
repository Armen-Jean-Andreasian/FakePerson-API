# FakePerson API

The **FakePerson API** provides a simple way to generate fake personal data for different countries. It is built using the FastAPI framework.

---

### Welcome Message

The base URL for the API is `/person/country_name/method`. Here are some example URLs:

- [http://127.0.0.1:8000/person/France/all_data](http://127.0.0.1:8000/person/USA/all_data)
- [http://127.0.0.1:8000/person/Belgium/passport_data](http://127.0.0.1:8000/person/USA/passport_data)
- [http://127.0.0.1:8000/person/Canada/personal_data](http://127.0.0.1:8000/person/USA/personal_data)
---
### Available Methods

- `address`
- `age`
- `all_data`
- `company`
- `date_of_birth`
- `email`
- `full_name`
- `passport_data`
- `passport_number`
- `personal_data`
- `phone_number`
- `sex`
---
### Handling Errors

If the specified country is not found, the API will return an error message:

```json
{"Error": "Country not found"}
```
---

### Response Example

```json
{
  "all_data": {
    "full_name": "Francisco Font",
    "sex": "Male",
    "date_of_birth": "12 Apr 1951",
    "passport_validity": "10 Sep 2021 10 Sep 2026",
    "passport_number": "499483986",
    "email": "martinacoll@hotmail.com",
    "address": "1778 Bruno Dale, Segurafort, MI 36218",
    "company": "Montaña-Coll"
  }
}

```


