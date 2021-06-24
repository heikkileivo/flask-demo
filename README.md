# flask-demo
Simple, minimal [Flask](https://flask.palletsprojects.com/en/2.0.x/) demo, intended to be run on uWsgi + nginx.

## Installation for development

To run the demo in local environment, follow these steps:

1. Clone the source code

```bash

git clone git@github.com:heikkileivo/flask-demo.git

```

2. Create a [virtual environment](https://docs.python.org/3/library/venv.html) for python

```bash

cd flask-demo
python3 -m venv env

```

3. To install dependecies and run the demo, you first need to activate the virtual environment:

```bash

source env/bin/activate

```

4. Then you can install required dependencies...

```bash

pip install -r requirements.txt

```

5. ..and run the server:

```bash

cd src
python app.py

```
Open your browser and browse to [http://localhost:5000/](http://localhost:5000) to view the demo.

Note that by default the flask runs in debug mode off. To enable debug mode, 
create a file for local settings:

```bash

cd settings
cp default.py local.py

```

Edit the local.py file to enable debug mode:

```python

DEBUG = True
ENV = 'development'

```

Restart the server to see the effects. In debug mode the server is 
restarted automatically, if you eg. modify a file, which is quite convinient.

## Installation to production server

