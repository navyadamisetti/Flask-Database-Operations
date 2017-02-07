import json
import requests
import pymysql
import collections
from pprint import pprint
from flask import Flask,render_template,request,jsonify,redirect,url_for
app = Flask(__name__)

conn=pymysql.connect(host="localhost",user="root",password="N@vya14chinnu",db="navya")  
# Connecting to the DataBase.

obj = conn.cursor() 
''' creating an object for cursor class:
 Allows Python code to execute Queries.
'''



@app.route('/') #Route for Index
def Main_Menu():
    '''This Function is used to display index which 
    leads to all the other web pages that contains 
    operations on trip list'''   

    return render_template('index.html')



@app.route("/list") #Route for list displaying
def list():
    """ This will execute query that is used to get 
    all the rows of table Location"""
    obj.execute("SELECT * FROM location")
    data = obj.fetchall()
    
    return render_template('list.html', data = data)



@app.route("/list.json") #Route for Json list
def json_list():
    obj.execute("""SELECT ID,Name,Latitude,Longitude FROM location""")    # executing Query
    rows= obj.fetchall()     #fetching all the rows
    objs= []
    for row in rows:
        b = collections.OrderedDict()
        b['ID'] = row[0]
        b['Name'] = row[1]
        b['Latitude'] = row[2]
        b['Longitude'] = row[3]
        objs.append(b)
    a = json.dumps(objs)    #serialization
    
    return render_template("jsonlist.html",b=a)     



@app.route('/create/') #Route for Insertion 
def create_demo():
    return render_template('insert.html')



@app.route('/create1',methods=['POST','GET']) #Route to execute insert Query
def create_1():
    """ Here the values taken in create route will
    be inserted by executing query"""
    if request.method=='POST':
        z = request.form['name'] # taking the values from the form
	obj.execute("""INSERT into location(Name,Latitude,Longitude) VALUES (%s,%s,%s)""",(z,request.form['latitude'],request.form['longitude']))
        conn.commit()
	
	return redirect(url_for('list'))



@app.route('/update') #Route for Updation
def update_demo():
    return render_template('update.html')



@app.route('/update1',methods=['POST','GET'])#Linked up with /update/ to update new details by giving ID
def update_new_details():
    if request.method=='POST':
        update=request.form['Name']
        query="SELECT ID,Name,Latitude,Longitude from location WHERE ID=%s"
        x=update
        obj.execute(query,x)
        datax=obj.fetchall()	
        
	return render_template('update1.html',datax=datax)



@app.route('/update2', methods=['POST','GET'])#update values based on ID using forms
def details_update():
	"""It will update the values Based on the ID given by the user"""
	if request.method=='POST':
		id=request.form['id']
		name=request.form['name']
		latitude=request.form['latitude']
		longitude=request.form['longitude']
        query="UPDATE location set Name=%s,Latitude=%s,Longitude=%s where ID=%s"
        y=(name,latitude,longitude,id)
        obj.execute(query,y)

        return redirect(url_for('list'))



@app.route("/delete/") #Route for Deletion
def delete():
    return render_template("delete.html")



@app.route('/delete1',methods=['POST','GET'])#This is connect with /delete
def delete1():
    if request.method=='POST':
        delete1=request.form['id']
        e="DELETE from location where ID=%s"
    obj.execute(e,delete1)
    conn.commit()
    return redirect(url_for('list'))



app.run()
