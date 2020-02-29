# Table of Contents

- [Table of Contents](#table-of-contents)
  - [Tell me the weather](#tell-me-the-weather)
    - [Tecnologies](#tecnologies)
    - [Instalation and launch](#instalation-and-launch)
    - [Demo](#demo)

## Tell me the weather

This is an app created in Django that calls the [API Open Weather Map][1].

It allows you to know the current weather of an specific location.

### Tecnologies

The tecnologies used in this project are these:

- [Django 3.0.3][5]
- [Bulma 0.8][4], it is an impressive CSS framework, simple and easily customizable.
- [Pipenv][3]

### Instalation and launch

Because it uses [*pipenv*][3] for managing the environment, I included a scripts section for make the process easier.

For example during the development process I used this:

`pipenv run dev`

It is inside the *Pipfile* file:

```Pipfile
[scripts]
dev = "python manage.py runserver"
```

Then, in a dev environment, you can access <http://localhost:8000> to see the application running.

### Demo

[Go back to the top](#table-of-contents)

<!-- enlaces -->
[1]: https://openweathermap.org/api
[2]: https://openweathermap.org/appid
[3]: https://pipenv.readthedocs.io/en/latest/
[4]: https://versions.bulma.io/0.8.0/
[5]: https://docs.djangoproject.com/en/3.0/
