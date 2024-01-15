# FakePerson API

The **FakePerson API** provides a simple way to generate fake personal data for different countries. It is built using
the FastAPI framework.

![](.github/assets/cover.png)

---

## Welcome Message

Welcome to FakePerson API!

It's a simple API business logic of which uses `Faker` and the API is built on `FastAPI`.
The API is designed to provide fake data in request-response context.

---

## Supported methods and Response Examples:

*The base URL for the API is `/person/country_name/method`.*

The available methods are:
- `/passport_data`  : generates and returns a dictionary containing fake passport information of the provided country.
  Example of `/person/France/passport_data` response:
    ```json
  {
      "passport_data": {
          "full_name": "Eugène Dupont",
          "sex": "Male",
          "date_of_birth": "10 Jan 1970",
          "passport_validity": "23 Jul 2022 23 Jul 2027",
          "passport_number": "I35262664"
      }
  }
  ```
- `/personal_data`  :  generates and returns a dictionary containing fake personal information 
  Example of `/person/France/personal_data` response:
   ```json
  {
      "personal_data": {
          "email": "bernardadrienne@tiscali.fr",
          "address": "82, chemin Eugène Hoareau, 48836 Barthelemy",
          "company": "Turpin S.A."
      }
  } 
  ```

- `all_data` : generates and returns a dictionary containing fake personal and passport information 
  Example of `/person/France/all_data` response:
    ```json
  {
      "all_data": {
          "full_name": "Eugène Dupont", "sex": "Male", 
          "date_of_birth": "10 Jan 1970",
          "passport_validity": "23 Jul 2022 23 Jul 2027", 
          "passport_number": "I35262664",
          "email": "bernardadrienne@tiscali.fr", 
          "address": "82, chemin Eugène Hoareau, 48836 Barthelemy",
          "company": "Turpin S.A."
      }
  } 
  ```

**Here are some example URLs:**

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
{
  "Error": "Country not found"
}
```
