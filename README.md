# Initials Avatar API

Create an avatar based on the users' name using a simple Flask API.

> Note: This project is not being maintained and was written for fun on a rainy day.

## Generate an avatar

To make your first request, use your browser and navigate to the address of the development server like so:

### Basic usage

By default you will get a 64x64px image with a light grey background with dark grey text.

```
http://127.0.0.1:5000/avatar/?name=Tim+Fisicaro
```

### Custom parameters

You can customize some properties of the image by sending query parameters with the request.
For examples, see the [docs](docs/parameters.md).

#### Size

The size of the image can be changed by passing the `size` parameter. The value must be a number between `32` and `512`.

Default: `64`

#### Background color

The background color of the image can be changed by passing the `background` parameter.
Value must be either a valid web color or `random`.

Default: `lightgrey`

#### Shape

The shape of the image can be changed by passing the `shape` parameter.
Value must be either `circle` or `square`.

Default: `square`

#### Text color

The text color of the image can be changed by passing the `text` parameter.
Value must be a valid web color.

Default: `#282828`

## Run locally

### Prequisites

-   Python 3
-   Pipenv

### Local installation

```console
$ python -m pip install pipenv  # Install globally
```

Next step is to create said virtual environment using the package `Pipenv` that we've installed. If the virtualenv is already created the existing one will be activated instead.

```console
$ pipenv shell
```

Install all dependencies listed in `Pipfile.lock`.

```console
$ pipenv install
```

Everything is now setup and you are ready to start the local (development) server.

```console
$ flask run
```

> The server is now running on (default) port 5000

> You can optionally enable debugging by setting the FLASK_ENV environment variable to "development".

```console
$ export FLASK_ENV=development  # macOS & Linux
$ $env:FLASK_ENV="development"  # Windows
```
