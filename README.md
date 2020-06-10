# DataJammingWebApp

A Flask app that uses the AI built and trained in [DataJamming](https://github.com/mhamedouadghiri/DataJamming/) to make text predictions given the encrypted input.


## Running Locally ...
Make sure you have Python 3.7 installed in your machine. Then follow these steps (Windows, cmd).
```
$ git clone https://github.com/mhamedouadghiri/DataJammingWebApp/
$ cd DataJammingWebApp
$ python -m venv venv
$ venv\Scripts\activate
$ python -m pip install --upgrade pip
$ python -m pip install -r requirements.txt
```

The either run the app with Flask.
```
$ set FLASK_APP=app
$ flask run
```

Or install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and run it with heroku.
```
$ heroku local web -f Procfile.windows
```

The app should now be running at [127.0.0.1:5000](http://127.0.0.1:5000/).


## ... deploying to heroku ...
Just follow the steps [here](https://devcenter.heroku.com/articles/getting-started-with-python) to get started.


## ... otherwise
Just visit the already deployed app [here](http://medpfa.herokuapp.com/).
