# codeselfstudy_django

Puzzle server.

# Development

## Installation

### Python

The Python version is in the `pyproject.toml` file. You can use something like `pyenv` or Docker to manage multiple Python versions.

Use Poetry to manage dependencies and the virtual environment.

Examples:

Run a command in the virtualenv:

```text
$ poetry run python manage.py runserver
```

Install a package:

```text
$ poetry add django
```

Install a dev dependency:

```text
$ poetry add -D pytest
```

Enter a shell in the virtualenv:

```text
$ poetry shell
```

Generate a secret key, and copy the example environment file for editing:

```text
$ poetry run python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Create the `.env` file if you don't have one:

```text
$ cp .env-example .env
```

Open the .env file and add the secret key to the `DJANGO_SECRET_KEY` line, and fill in the `DATABASE_NAME` you want to use, and any database credentials needed.

### Node.js

Make sure you're using Node 16, and then install the dependencies. The `nvm use` command will automatically switch to Node 12 by reading the `.nvmrc` file, if you installed Node with `nvm`.

```text
$ nvm use
$ npm install
```

### Database

**NOTE:** this section might be outdated.

If you don't have Postgres installed on your computer, you can run it from within a Docker container. See the [README.md](./server_development/docker/README.md) file in the `./server_development/docker/` directory.

After Postgres is running, create a database using the name you chose in your `.env` file, then migrate the database:

```text
$ python manage.py migrate
```

### Raku

[`TODO:` remove Raku and rewrite the parser in Python.]

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

**NOTE:** this section is probably outdated.

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
$ poetry run python manage.py runserver
```

Then visit `localhost:8000`.

To create a user account, run this command:

```text
$ poetry run python manage.py createsuperuser
```

Then log in at `localhost:8000/admin/`.

## Code Style

Please enable prettier.js in your editor so that it autoformats JavaScript/TypeScript/CSS/scss code according to the rules in the `.prettierrc` file.

If you're using Atom, install the `prettier-atom` package, and decide if you want to use `Format Files on Save` in the settings, or format manually.

If you're using VS Code and the formatting doesn't work automatically, try adding [this extension](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode).

If you're using VS Code, it should automatically give you formatting hints. If the Python linting rules are too strict, open a Github issue with the problem and we can modify the settings. (See the `tox.ini` file.)

If you use VS Code, you can also add [this extension](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig), and it will automatically follow this project's `.editorconfig` guidelines.

The Python code is formatted with Black.

```
$ poetry run black .
```

TODO: automate all the code formatting.
