# Weather-Web-App

A simple Django-based weather forecast app using OpenWeatherMap API.

## Features

- Search weather by city name
- Displays temperature, description, and weather icon
- Shows current date
- Uses OpenWeatherMap API
- Basic CSS styling

## Screenshot

![Screenshot 2025-05-06 222357](https://github.com/user-attachments/assets/db7d2b05-c5fb-429b-a3df-43411a642de5)

## Technologies Used

- Django 5.2
- Basic HTML / CSS
- OpenWeatherMap API
- Python 3.x

## Installation

```
https://github.com/ridika-2004/Weather-Web-App.git
cd weatherapp
pip install -r requirements.txt
python manage.py runserver
```

## API Key
This app uses OpenWeatherMap API.
Replace the default key in `views.py` with your own:

```
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"
```

## Static Files
Make sure your CSS file is in the right place:
`weather/static/weatherapp/style.css`

In `settings.py`, ensure:
```
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

## Troubleshooting

- 404 for CSS? Check the static path and folder structure.
- Make sure `DEBUG = True` while in development.
- Use python `manage.py collectstatic` for deployment.

## Folder Structure
```
weather/
├── weather/
|   └──.....
├── weatherapp/
|   └──.....
├── static/
│   └── weatherapp/
│       └── style.css
├── templates/
│   └── weatherapp/
│       └── index.html
├── manage.py
```

