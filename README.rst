Flask example project
=====================

This contains the code I use to help answer flask questions. It shows several
useful-but-not-obvious patterns and tricks, like:

* organizing app code with blueprints
* the extension pattern
* generic/reusable blueprints
* reusable modules with flask-sqlalchemy models
* using flask-sqlalchemy models without flask (without app context)
* adding cli commands


You're most likely here because I linked you to some example in the code;
otherwise, if you'd like to read and explore how is this example app structured,
the best place to start reading it is `flaskexample/__init__.py`.
Follow the imports into the flaskexample "app" package, and into the generic
packages outside it. (that are generic in the sense they're not part of the app,
so they could've come from PyPI)


Running this code
-----------------

To create the database, create a config file, or edit `config.py`, and do:
`python manage.py --config config.py createdb`

To run the devserver, do:
`python manage.py --config config.py run`

To run the tests:
`py.test`


TODO
----

* add the 'using vanilla sqla models with flask-sqla' example
* add the 'using the same models with multiple binds' example
