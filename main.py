import requests


def get_weather_forecast(location):
    payload = {
        "nTqM": "",
        "lang": "ru",
    }
    url_template = 'http://{domen}/{article}'
    url = url_template.format(domen='wttr.in', article=location)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


def main():
    locations = [
        "London",
        "svo",
        "Cherepovets",
    ]
    for location in locations:
        metcast = get_weather_forecast(location)
        print(metcast)


if __name__ == '__main__':
    main()
