
Simple Flask python API server for test portal use

Usage:

```bash

<install python, python-pip>

pip install Flask

cd <dir>

export FLASK_ENV=development
export FLASK_APP=app.py

flask run

<server will be on 127.0.0.1:5000>
 

```

cURL example:


```bash

# request
curl -X POST -F "username=bob" -F "code=marley" localhost:5000/check

# response

{"minutes":13,"traffic":12}


```
