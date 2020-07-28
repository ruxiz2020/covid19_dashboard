# text_toolkit

## website can be viewed here

https://covid19-dashboard-simple.herokuapp.com/


## How to run reporting tool


```bash
virtualenv -p python3 env
source env/bin/activate
```

Install the requirements:

```bash
env/bin/pip install -r requirements.txt

```
Run the app:

```bash
env/bin/python app.py
```
Open a browser at http://127.0.0.1:8050


## deploying it on Heroku

```bash
heroku create covid19-dashboard-simple

git remote add heroku  text-toolkit

git push heroku master
```
