# Reddit Bot

This is a basic bot for reddit.

---------------------------------------

## Run the VENV

From within the project directory

1. Activate the venv

    $ source tutorial-env/bin/activate

2. Run the application

    $ python3 app/main.py

3. You need to do some setup on the reddit account you wish to use. Create a Reddit App from https://www.reddit.com/prefs/apps/ . Choose to make a script. This is a bot so it does not require a redirect URI but you have to enter one anyhow so enter "http://127.0.0.1" into the field.

Collect the webapp name and also the secret key from the form.

---------------------------------------

## Shut down the app

1. control + c to kill the application

2. Deactivate the venv (Obvious?)

    $ deactivate
