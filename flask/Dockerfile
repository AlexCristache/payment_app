# Use the Python3.8 image
FROM python:3.8.1-buster
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD . /app

# Install the dependencies
RUN pip install -r requirements.txt

ENV DATABASE_URL="postgresql://localhost:5432"

#RUN flask db downgrade

#RUN flask db init

#RUN flask db upgrade

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
