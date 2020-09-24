#  Employee Management

The purpose of this application is help DeKUT to manage employees' information.

## How it works

It offers an admin WEB interface to manage employees' data and a REST API to list, add and remove employees.

## Getting Started

### Prerequisites
- GIT
- Python 3.6.1
-postgresql

#### Linux:
`sudo apt-get install git python3.6.1 `

### Installation
1. Create a Directory
  mkdir `fema_project`
2. Access project directory
  `cd fema_project`
3. Clone [FEMA project](https://github.com/DeKUT-DSAIL/Backend_Cmapp.git) repository
`git clone https://github.com/DeKUT-DSAIL/Backend_Cmapp.git`
4. Create a Python Virtualenv and activate it
```
python3 -m venv .venv
source .venv/bin/activate
```
4. Install project requirements
`pip install -r requirements.txt`
5. Run Database migration

```
./manage.py makemigrations 
./manage.py migrate 
```
6. Create a Superuser to manage the system

`./manage.py createsuperuser`

## Running the project

`./manage.py runserver`

## Running Tests

`./manage.py test`

## How to use

Access Admin interface URL: `http://127.0.0.1:8000/admin`
