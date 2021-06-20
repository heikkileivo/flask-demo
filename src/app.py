import logging
import sys
from flask import Flask
from flask import render_template as render
from threading import Thread

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)
app.config.from_object('settings')


@app.route('/')
def index():
    return render('index.html')

@app.route('/sample/')
def view():
    return render('sample.html')

@app.route('/about/')
def about():
    return render('about.html')

if __name__ == '__main__':
    # If the application was started using python app.py,
    # run the debug server
    app.run()
