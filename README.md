# codeselfstudy_django

New site.

# Development

## Installation

```text
$ python3 -m venv .venv
$ pip install -r requirements/development.txt
```

Make sure you're using Node 12, and then install the dependencies. The `nvm use` command will automatically switch to Node 12 by reading the `.nvmrc` file, if you installed Node with `nvm`.

```text
$ nvm use
$ npm install
```

For convenience, add to your `.zshenv`, `.bashrc`, or `.aliases` file:

```bash
alias m='python manage.py'
```

Wherever you see `m` in this document, it means `python manage.py`.

If you don't have Postgres installed on your computer, you can run it from within a Docker container. See the [README.md](./docker/README.md) file in the `./docker/` directory.

After Postgres is running, migrate the database and run the app:

```text
m migrate
m runserver
```

## Code Style

Please enable prettier.js in your editor so that it autoformats JavaScript/TypeScript/CSS/scss code according to the rules in the `.prettierrc` file.

Please lint the Python with `flake8`. If the Python linting rules are too strict, open a Github issue with the problem and we can modify the settings. (See the `tox.ini` file.)

TODO: automate formatting/linting with a git hook or similar method.

## Running

Run the frontend and backend servers

```text
$ npm start
$ m runserver
```

(`m runserver` is the alias for Django's `python manage.py runserver` -- see above.)
