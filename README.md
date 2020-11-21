# codeselfstudy_django

New site.

# Development

## Installation

```text
$ python3 -m venv .venv
$ pip install -r requirements/development.txt
$ npm install
```

For convenience, add to your `.zshenv`, `.bashrc`, or `.aliases` file:

```bash
alias m='python manage.py'
```

Wherever you see `m` in this document, it means `python manage.py`.

## Running

Run the frontend and backend servers

```text
$ npm start
$ m runserver
```

(`m runserver` is the alias for Django's `python manage.py runserver` -- see above.)
