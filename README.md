# codeselfstudy_django

Puzzle server.

# Development

## Installation

### Python

Create a Python virtual environment:

```text
$ python3 -m venv .venv
```

Activate the virtual environment:

```text
$ source .venv/bin/activate
```

Install the dependencies into the virtual environment:

```text
$ pip install -r requirements/development.txt
```

When you are finished working on the site, you can deactivate the virtual environment with:

```text
$ deactivate
```

For convenience, you can add this to your `.zshenv`, `.bashrc`, or `.aliases` file:

```bash
alias m='python manage.py'
```

If you do that, wherever you see `python manage.py` in this document, you can type `m` instead.

### Node.js

Make sure you're using Node 12, and then install the dependencies. The `nvm use` command will automatically switch to Node 12 by reading the `.nvmrc` file, if you installed Node with `nvm`.

```text
$ nvm use
$ npm install
```

### Database

If you don't have Postgres installed on your computer, you can run it from within a Docker container. See the [README.md](./development_server/docker/README.md) file in the `./development_server/docker/` directory.

After Postgres is running, migrate the database:

```text
$ python manage.py migrate
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

## Code Style

Please enable prettier.js in your editor so that it autoformats JavaScript/TypeScript/CSS/scss code according to the rules in the `.prettierrc` file. If you're using vscode and the formatting doesn't work automatically, try adding [this extension](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode).

If you're using vscode, it should automatically give you formatting hints. If the Python linting rules are too strict, open a Github issue with the problem and we can modify the settings. (See the `tox.ini` file.)

If you use vscode, you can also add [this extension](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig), and it will automatically follow this project's `.editorconfig` guidelines.
