# flask-demo
Simple, minimal [Flask](https://flask.palletsprojects.com/en/2.0.x/) demo, intended to be run on uWsgi + nginx.

The live demo can be viewed in [https://flask-demo.dynalias.net/](https://flask-demo.dynalias.net/).


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

Follow these steps to install the demo in a production environment. 
To run a flask app on a production server it is recommended to use 
[NGINX](https://www.nginx.com/) as web server and [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) to run the python application.
The demo source code contains sample configuration files for both.

1.  [Install NGINX](https://www.nginx.com/resources/wiki/start/topics/tutorials/install/) as web server

```bash

sudo apt-get update
sudo apt-get install nginx

```

2. Clone the source code where-ever you find suitable, create a virtual environment etc.

```bash

git clone git@github.com:heikkileivo/flask-demo.git
cd flask-demo
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
pushd src/settings
copy default.py local.py
popd

```

This demo does not contain any real settings which should be overriden on the server, but
in practice you should edit the DB settings etc. in the local.py file and keep the DEBUG setting as False.

3. Create symbolic link to /srv directory

The configuration files assume that the application is located in /srv directory, so you need to create a symbolic link pointing to where your source code has been cloned. 
This requires adming privileges. The following example assumes that you have installed the source to your home directory.

```bash

cd /srv
sudo ln -s /home/[your-account]/flask-demo .

```

4. Start uWSGI service

To run the python application, you have to run the uWSGI server. The configuration file for uWSGI service is [flask-demo.ini](src/flask-demo.ini); review it for details. 
You can either install it as [systemd service](https://linuxconfig.org/how-to-create-systemd-service-unit-in-linux#h8-creating-and-installing-a-service-unit) or run it using [supervisord](http://supervisord.org/) (or by any other means you find appropriate). 

The systemd service file is [flask-demo.service](src/flask-demo.service). To install uWSGI as systemd service, create a symbolic link to it into /etc/systemd/system directory and start the service:

```bash

sudo ln -s /srv/flask-demo/src/flask-demo.service /etc/systemd/system
sudo systemctl start flask-demo.service

```

If the system started normally, you should see flask-demo.sock file in /tmp directory. 

Alternatively, you can run uWSGI using supervisord. Refer to [supervisord documentation](http://supervisord.org/installing.html) for details in installing. 
To start uWSGI using supervisor, create a symbolic link to supervisord configuration file [flask-demo.supervisor.conf](src/flask-demo.supervisor.conf) 
into supervisord configuration directory /etc/supevisor/conf.d:

```bash

sudo ln -s /srv/flask-demo/src/flask-demo.supervisor.conf /etc/supervisor/conf.d
sudo supervisorctl reload
sudo supervisorctl status

```

You should see uwsgi service running in supervisorctl status, and you should find flask-demo.sock file in /tmp directory.

5. Set up NGINX to serve the application

To set up NGINX, review the nginx configuration file [flask-demo.nginx.conf](src/flask-demo.nginx.conf). Modify the server_name directive according to the 
dns name you are planning to host your service. Then create a symbolic link into /etc/nginx/sites-enabled directory and restart nginx:

```bash

sudo ln -s /srv/flask-demo/src/flask-demo.nginx.conf /etc/nginx/sites-enabled
sudo service nginx configtest
sudo service nginx reload

```

You should now see the flask site up and running on your production server.

6. Serve site with https 

The final step would be to install https certificate to serve the site using https. 
The easiest way is to use [certbot](https://certbot.eff.org/) to create a Let's Encrypt certificate. Refer to [certbot documentation](https://certbot.eff.org/instructions) for installing certbot and run:

```bash

sudo certbot --nginx

```

Follow the instructions to create a certificate to your site, and your site should be now served using https. 
