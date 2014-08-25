# Project Groat

## For develompent

* Clone the repo
* Get the [Heroku Toolbelt](https://toolbelt.heroku.com/)
* push to your heroku account. [Calvin](https://github.com/calvingiles) is keeper of the keys for this one for now.

### requirements.txt and virtualenv

To set up a veritual env locally, `cd` to the root of the project and run:

```bash
$ virtualenv venv
```

This will reate a `venv` folder with virtualenv wrapped python and pip executables. To activate them in the current shell, use:

```bash
$ source venv/bin/activate
```

To install the requirements from the existing `requirements.txt` file, run:

```bash
$ pip install -r requirements.txt --allow-all-external
```

If you subsequently change the configuration by installing additional packages via the venv pip, use `pip freeze` to create a new requirements.txt file.

```bash
$ pip freeze > requirements.txt
```

## API

Not defined yet. It should be RESTful and json.


## Heroku getting started README --- python-getting-started

A barebones Python app, which can easily be deployed to Heroku.

This application support the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

### Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started
$ pip install -r requirements.txt
$ python manage.py syncdb
$ foreman start web
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

### Deploying to Heroku

```sh
$ heroku create
$ git push heroku master
$ heroku run python manage.py syncdb
$ heroku open
```

### Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

