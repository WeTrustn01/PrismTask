# PrismFP Task
This is a python Flask REST API for managing trades. This application uses postgresql.
The following goal have been met: CRUD API for a Trade Model; API uses PostgreSQL as the database and SQLAlchemy as an ORM layer; Code is accessible on GitHub, Testing has been done; Schema Migrations implemented; Docker image can be created

## Getting Started
The following installation can be done on macOS 10.14.3 or similar UNIX systems

### Prerequisites and Installation
applications works with the following version of python, but older versions might be supported
```
python 3.7.0
```
(OPTIONAL) Create a python virtual environment:
```
python3 -m venv venv
virtualenv venv
source venv/bin/activate
```
All required python packages can be installed using requirements.txt:
```
pip3 install -r requirements.txt
```
To start the application run:
```
python3 -m flask db init
python3 -m flask db init
python3 -m flask db migrate -m "trades table"
python3 -m flask db upgrade
python3 -m flask run
```
NOTE: You will have to change database configuration in /app/__init__.py:
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://USER:PASSWORD@localhost/DATABASE_NAME'
```
Replace capitalised with your own details
pg_start.sh and pg_stop.sh are scripts to start or stop the postgresql server on macOS

### Using Docker
```
docker build -t prism:latest .
docker run --name prism -d -p 8000:5000 --rm microblog:latest
```
You will communicate with the application using port 8000. This can be changed

NOTE: This has not been tested!

##Tests
Application was tested using Postman.
E.g:
```
POST http://localhost:5000/trades
post the following form data: currency - USD; quantity - 1000; direction - SELL

GET http://localhost:5000/trades
get all trades in JSON format

GET http://localhost:5000/trades/1
get trade with id=1 in JSON format

PATCH http://localhost:5000/trades/1
update trade with id=1 in JSON format with the following form data: currency - UPDATE_TEST; quantity - 101; direction - TEST

DELETE http://localhost:5000/trades/1
delete trade with id=1 in JSON format
```
Can also test using:
```
flask shell
```
this will allow interacting with the models without working routes

Currently the application does not handle invalid input: i.e direction and currency can be any strings

## Justification for design
Application code has been modularised to some extent in order to simulate a real project. Migrations used so that changes to databases can be inspected before being pushed to a production server.
