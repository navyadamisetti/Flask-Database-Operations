# CRUD operations using Flask and Database in Ubuntu
   This is to create a list about trip using flask functions where the user can implement CRUD operations using web pages.
   
## Requirements>>>

- python: Json, Flask, pymysql, Requests, Collections, render_template, request, jsonify, redirect, url_for
- MySQL Database
- Html


## setting up :+1:
- Firstly installed pip, flask, virtualenv, pymysql.
```
$sudo apt-get install pthon-pip
$sudo apt-get install python-flask
$sudo apt-get install python-virtualenv
$sudo apt-get install python-pymysql
```
- entered MySQL and created a database "navya" 
- created a table "location" with columns ID(Primary Key), Name, Latitude and Longitude.


## Python-Flask>>>

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

### Main Menu:

- From Line 19 to Line 25: [final_asg.py](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/final_asg.py)
- HTML code for Index : [click here](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/templates/index.html)
- It only displays a page used to select the operations that we want to perform.
- OUTPUT: Webpage
![alt tag](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/Outputss/index.png)

### List in Tabular Format:

- From Line 29 to Line 36: [final_asg.py](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/final_asg.py)
- HTML code for Trip List: [click here](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/templates/list.html)
- By using for loop it displays whole data.
- It also had link to Main Menu.
- OUTPUT: Webpage
![alt tag](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/Outputss/triplist.png)

### List in Json Format:

- From Line 40 to Line 54: [final_asg.py](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/final_asg.py)
- Serialization can be done to the data in "navya" to convert it to Json Data.
- HTML code for Trip List in Json Format: [click here](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/templates/jsonlist.html)
- OUTPUT: Webpage
![alt tag](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/Outputss/json.png)

### Insertion:

- From Line 58 to Line 73: [final_asg.py](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/final_asg.py)
- We have to insert Name, Latitude and Longitude.
- As ID is a primary key it is in incremental model.
- HTML code for Insertion: [click here](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/templates/insert.html)
- OUTPUT: Webpage1
![alt tag](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/Outputss/insert1.png)

- This leads to the Trip list in Tabular Format after the Insertion.

- OUTPUT: Webpage2
![alt tag](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/Outputss/insert2.png)

### Updation:

- From Line 77 to Line 108: [final_asg.py](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/final_asg.py)
- We need to enter the key for which we want to update data.
- HTML code for it is: [click here](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/templates/update.html)

- OUTPUT: Webpage1
![alt tag](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/Outputss/update1.png)

- This leads to another webpage where we actually update the data.
- HTML code for it: [click here](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/templates/update1.html)

- OUTPUT: Webpage2
![alt tag](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/Outputss/update2.png)

- This leads to the Trip list in Tabular Format after the Updation.

- OUTPUT: Webpage3
![alt tag](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/Outputss/update3.png)

### Deletion

- From Line 112 to Line 125: [final_asg.py](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/final_asg.py)
- We need to enter the key for which the data wanted to be deleted.
- HTML code for it: [click here](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/templates/delete.html)

- OUTPUT: Webpage1
![alt tag](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/Outputss/delete1.png)

- This leads to the Trip list in Tabular Format after the Deletion.

- OUTPUT: Webpage2
![alt tag](https://github.com/navyadamisetti/Flask-Database-Operations/blob/master/Outputss/delete2.png)
## Thank you
