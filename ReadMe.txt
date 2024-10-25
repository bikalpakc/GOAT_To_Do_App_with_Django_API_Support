This is the completely functional To Do App with login, registration, authentication, Third-party login(Google), profile, profile picture, CRUD(Create, Read, Update, Delete) features along with APIs, that allow this application to be integrated to any front end framework or technology.

This app is built upon Python Django and Python Django Rest Framework.

To start the app/Django server, write the following in the terminal: python manage.py runserver

In order to login through the API, provide the username and password to the following Endpoint:
http://127.0.0.1:8000/api/auth/login   (Browsable API activated)

In order to logout:
http://127.0.0.1:8000/api/auth/logout

After logging in, To view or add tasks of that logged in user:
http://127.0.0.1:8000/api/tasks/ 

To update, delete or view details of the single task:
http://127.0.0.1:8000/api/tasks/<task_name>

Screenshots of this project are also included in the repository.