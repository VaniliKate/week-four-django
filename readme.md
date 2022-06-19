# Neighbourhood
This is a Django app that allows its users to be kept in the loop of what is happening in the area, this could be news like meetings, security concerns and power shortages. 

## Technologies
The project is created with:
* HTML:5 for giving the structure of the webpage.
* CSS:3 for styling the webpage.
* Bootstrap for more styling of the webpage.
* Python Django for the functionality.

## Features

- User authentication(Sign up and sign in).
- Profile set up.
- Create posts.
- Update profile details.
- View details of specific neighbourhoods.

### Installation

- Make sure Python is installed.
- Clone https://github.com/VaniliKate/weekthree-django.git and cd into weekthree-django.
- Install requirements using following command.

```
pip install -r requirements.txt
```
### Usage

- Create a virtual environment.

```
python3 -m venv venv
. venv/bin/activate
```

- Declare following environment variables in the .env file.

```
> SECRET_KEY = 'secret key'
> DEBUG = True
> EMAIL_USERNAME = 'your email address'
> EMAIL_PASSWORD = 'your password'
```

- Make migrations.

```
python manage.py migrate
```

- Commit the migrations.

```
python manage.py makemigrations
```

- Create a super user.

```
python manage.py createsuperuser
```

- Run the app.

```
python manage.py runserver
```

- This opens the app at `localhost:8000` or `http://127.0.0.1:8000/`


## Authors

- **Kate Vanili(2022)**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details