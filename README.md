Flask app using Docker and NGINX

For local development the sqlite database is used. In order to run the application run the flask app while inside the flask directory.
An example usage of the api can be found in the tests.

The docker container is setup to use PostgresSQL as database, but there are some issues with the connectivity I am yet to fix.

Further improvements:
- make PostgresSQL work inside the docker
- write more unit tests
- add logging to the application for better monitoring.
