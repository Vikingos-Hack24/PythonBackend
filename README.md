To run it :
uvicorn app.main:app --reload



# PythonBackend
Backend para python:


Posible stack de python y workflow

FastAPI Para la generacion de las APIs>

Conectando a base de datos posiblemente hosteado en GoogleCloud




app/: Main application package.
main.py: Entry point for the FastAPI app.
core/: Core settings and configurations.
config.py: Configuration variables and settings.
api/: API routers and endpoints.
endpoints/: Individual endpoint definitions.
services/: Integrations with external services (e.g., Google Cloud).
models/: Pydantic models and data schemas.
utils/: Utility functions and helper methods.
tests/: Test cases for your application.



SETUP
git pull
activate virtual env
pip install 


# Endpoints:

All will be using the endpoint /api/


FEDERICO

POST
user/register/

POST
user/login/ --Utilizing Firebase AUTH

GET
user/{id}/path/

GET
user/{id}/{auth}/info/ -- All importan information to make sure to build unique dashboard for person. {{DISCUSSION NEEDED}}


Edson

POST
user/{id}/createPath ->> Path
information : 'String... All of the things that were mentioned in the initial survey to make sure its unique path'

{
[{level : numberOfLevel, moduleName : "nameOfModule", moduleInfo:".... Info info about module", next: [NextModules, can be one or two at maximum like a binary tree]}...
Maximum of 7 modules
]
}

Emi

POST
user/{id}/{moduleName}/createSurvey
GET
user/{id}/{moduleName}/getSurvey


Baca

POST 
user/{id}/finPal ---- Info retrieved in the POST, answers to that specific question. (Baca sabra que mas se necesita)






