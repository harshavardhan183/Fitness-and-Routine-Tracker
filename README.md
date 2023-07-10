# QuantifiedSelf
Quantified-Self is a self-tracking application used to track habits, activities and other life parameters like weight, temperature, mood etc.

**Technologies used**

• Flask: Application Code

• Flask-Sqlalchemy: Flask extension for Sqlalchemy to create database models

• Matplotlib: Python library to add graphs in the application

• Bootstrap: For CSS and HTML generation

![image](https://user-images.githubusercontent.com/107307277/173203100-31bbf861-2d8a-4fe3-9f08-e66e853aba7e.png)

**About Schema**

Two tables are created as shown in the above schema.
Tracker table stores tracker name, its type, description and the time when it is modified.
Log table stores the logs of each tracker type. It stores the logs, tracker_id, time when
the log is modified.

**Architecture and Feature**

app.py is the main file containing all the flask code & database models & routes etc.
All html files are present in templates folder and all images are in static folder.
CRUD is implemented for both tracks and logs. User can create, update and delete their
account. Dashboard is created to see the list of trackers with buttons to help in CRUD
operations. Each tracker has its own page to see the logs.

**Working Video Link Of Application**:
https://drive.google.com/file/d/17YQCnruEyMBdX0A0QJ1ioeTzWXrUETEn/view?usp=sharing
