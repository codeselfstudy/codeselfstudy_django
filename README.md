# codeselfstudy_django

Puzzle server.

# Development

TODO: update this for Docker. (basically: `docker-compose -f docker-compose.dev.yml up --build`) It will be running on `localhost:5000` unless this README is out of date.

Example commands:

```bash
# start up the docker containers
docker-compose -f docker-compose.dev.yml up --build

# one-time setup
docker-compose -f docker-compose.dev.yml exec django python manage.py makemigrations
docker-compose -f docker-compose.dev.yml exec django python manage.py migrate
docker-compose -f docker-compose.dev.yml exec django python manage.py createsuperuser

# load seed data
docker-compose -f docker-compose.dev.yml exec django python manage.py loaddata apps/puzzles/fixtures/codewars.fixtures.json
docker-compose -f docker-compose.dev.yml exec django python manage.py loaddata apps/puzzles/fixtures/leetcode.fixtures.json
docker-compose -f docker-compose.dev.yml exec django python manage.py loaddata apps/puzzles/fixtures/projecteuler.fixtures.json
docker-compose -f docker-compose.dev.yml exec django python manage.py loaddata apps/languages/fixtures/languages.yaml

# shut down docker containers
docker-compose -f docker-compose.dev.yml down
```

## Installation

TODO: write new instructions for the docker-compose workflow.

TODO: add instructions about the `.env` files.

Generate a secret key, and copy the example environment file for editing:

```text
$ python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
$ cp .env-example .env
```

Open the .env file and add the secret key to the `DJANGO_SECRET_KEY` line, and fill in the `DATABASE_NAME` you want to use, and any database credentials needed.

### Raku

[`TODO:` make sure this section of the setup instructions works. This first draft is written from memory.]

The slash-command parser is written in a language called [Raku](https://raku.guide/#_introduction). You can install Raku with [rakubrew](https://rakubrew.org/):

```
$ rakubrew download
```

You'll also need the `zef` package manager:

```
$ rakubrew build-zef
```

After they are both installed, run this to install this site's only Raku dependecy:

```
$ zef install JSON::Tiny
```

## Testing

It uses pytest. There is an intro to pytest [here](https://djangostars.com/blog/django-pytest-testing/).

To run the tests, type:

```text
$ make test
```

## Running the Website

Run the frontend server by typing this in a terminal:

```text
$ npm start
```

Run the backend server by typing this in another terminal:

```text
$ python manage.py runserver
```

Then visit `localhost:8000`.

To create a user account, run this command:

```text
$ python manage.py createsuperuser
```

Then log in at `localhost:8000/admin/`.

## Code Style

Please enable prettier.js in your editor so that it autoformats JavaScript/TypeScript/CSS/scss code according to the rules in the `.prettierrc` file.

If you're using Atom, install the `prettier-atom` package, and decide if you want to use `Format Files on Save` in the settings, or format manually.

If you're using VS Code and the formatting doesn't work automatically, try adding [this extension](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode).

If you're using VS Code, it should automatically give you formatting hints. If the Python linting rules are too strict, open a Github issue with the problem and we can modify the settings. (See the `tox.ini` file.)

If you use VS Code, you can also add [this extension](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig), and it will automatically follow this project's `.editorconfig` guidelines.
