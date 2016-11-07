# CRUD operations using Flask and Database in Ubuntu
   This is to create a list about trip using flask functions where the user can implement CRUD operations using web pages.
   
## Requirements

- python: Json, Flask, pymysql, Requests, Collections, render_template, request, jsonify, redirect, url_for
- MySQL Database
- Html


## setting up:
- Firstly installed pip, flask, virtualenv, pymysql.
```
$sudo apt-get install pthon-pip
$sudo apt-get install python-flask
$sudo apt-get install python-virtualenv
$sudo apt-get install python-pymysql
```
- entered MySQL and created a database "navya" 
- created a table "location" with columns ID(Primary Key), Name, Latitude and Longitude.


## Python-Flask

My [Python-Flask code](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/final_asg.py) has different functions to insert, update, delete data and also convert this native data into Json format.
- Connection with "navya" database in MySQL.
- Route for Main Menu.
- Route for list in Tabular Format.
- Route for list in Json Format.
- Route for insertion of details.
- Route for Updation of data.
- Route for Deletion of data.
This is saved in a folder with the name of this file "final_asg".
A new file named ["templates"](https://github.com/navyadamisetti/Flask-Database-Operations/tree/master/templates) will be created in "final_asg" folder.

### Main Menu
