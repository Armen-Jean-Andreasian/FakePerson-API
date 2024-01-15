from fakedata import FakePerson
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from errors import CountryNotFoundError

app = FastAPI()


@app.get('/', response_class=PlainTextResponse)
async def main():
    fake_person_methods = [method[4:] for method in dir(FakePerson) if method.startswith('get_')]
    available_methods = ['\n\t-' + method for method in fake_person_methods]

    welcome_message = (
        f"Welcome to the FakePerson API!\n\n\n"
        f"Base URL: /person/country_name/method\n\n"
        f"Example URL: http://127.0.0.1:8000/France/all_data\n"
        f"Example URL: http://127.0.0.1:8000/Greece/passport_data\n"
        f"Example URL: http://127.0.0.1:8000/France/personal_data\n\n"

        f"Available methods for {FakePerson.__name__}:\n"
        f"{''.join(available_methods)}\n\n"

        f"Feel free to explore and have fun with the API!"
    )
    return welcome_message


@app.get('/{country}/{method}')
async def get_data(country: str, method: str):
    try:
        fake_person = FakePerson(country=country)
        result = getattr(fake_person, f"get_{method}")
        return {method: result}
    except CountryNotFoundError as error:
        return {"Error": str(error)}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
