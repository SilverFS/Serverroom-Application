##Imports all necessary products
import flask
from flask import Flask, render_template, request, session, redirect
import mysql.connector
import datetime
import os

id = 0





##MySQL/USBWebserver connection to the database "applicatie"
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="usbw",
    database="serverruimte"
)
##Cursor is intended to collect data and move it to the database.
mycursor = mydb.cursor()



##Refers to all HTML pages and static's in the folder "static." This folder contains 2 stylesheets (styles.css & w3.css).
app = Flask(__name__, static_url_path='/static')

##app route loginpage (I do not use this one (I intended, but didn't had the time left))
@app.route('/login')
def login():
    return render_template('index.html', **templateData, data=data)


##Index (Homepage)
@app.route('/')
def index():
    return render_template('index.html')



##Info page
@app.route('/Info')
def Info():
    return render_template('Info.html')


##approute edit_now
@app.route('/edit_now', methods=['POST'])
def edit_now():
    if request.method == 'POST':
        ##Variables
        reserveringsdatum = '"' + request.form['Reserveringsdatum'] + '"'
        einddatum = '"' + request.form['Einddatum'] + '"'
        psnummer = '"' + request.form['PSnummer'] + '"'
   
        ##Update info of the content in the form and sql.
        sql = "UPDATE " + tablenow + " SET Begindatum = " + reserveringsdatum + " WHERE id = " + idnow
        mycursor.execute(sql)
        sql = "UPDATE " + tablenow + " SET Einddatum = " + einddatum + " WHERE id = " + idnow
        mycursor.execute(sql)
        sql = "UPDATE " + tablenow + " SET Leerlingnummer = " + psnummer + " WHERE id = " + idnow
        mycursor.execute(sql)

        mydb.commit()

        ##Return to the last session.
        return redirect(session['url'])



##Render rack
@app.route('/edit_data/<string:serverrack>/<string:id>/', methods=['GET', 'POST'])
def edit_data(id, serverrack):
    global idnow
    global tablenow
    idnow = id
    ##Selecting the right Server rack from the dropdown menu. It's linked to the buttons in the dropdown menu with "idnow."
    tablenow = "racku20" + serverrack
    ##Idnow is the id of every rack in the list.
    sql = "SELECT * FROM " + tablenow + " WHERE id = " + idnow
    mycursor.execute(sql)
    data = mycursor.fetchall()

    templateData = {
        'title' : 'Edit'
    }

    return render_template('edit.html', **templateData, data=data)







##Render rack >> delete info
@app.route('/delete_data/<string:serverrack>/<string:id>/', methods=['GET', 'POST'])
def delete_data(id, serverrack):
    global idnow
    global tablenow
    idnow = id
    tablenow = "racku20" + serverrack
    sql = "SELECT * FROM " + tablenow + " WHERE id = " + idnow
    mycursor.execute(sql)
    data = mycursor.fetchall()

    templateData = {
        'title' : 'Delete'
    }
    ##It's somewhat the same as "UPDATE" but content removed, like this: ""
    sql = "UPDATE " + tablenow + " SET Begindatum = %s WHERE id = %s"
    val = ("", idnow)
    mycursor.execute(sql, val)
    sql = "UPDATE " + tablenow + " SET Einddatum = %s WHERE id = %s"
    val = ("", idnow)
    mycursor.execute(sql, val)
    sql = "UPDATE " + tablenow + " SET Leerlingnummer = %s WHERE id = %s"
    val = ("", idnow)
    mycursor.execute(sql, val)

    mydb.commit()


    return redirect(session['url'])
    






##Contact form page
@app.route('/Contact')
def Contact():
    return render_template('Contact.html')

##RackU201 page
@app.route('/racku201')
def RackU201():
    session['url'] = flask.request.url
    global tablenow
    tablenow = flask.request.url
    ##Getting everything from racku201
    mycursor.execute("SELECT * FROM racku201")
    data = mycursor.fetchall()

    templatedata = {
        'title' : 'racku201'
        }
    
    return render_template ('Lijstvanservers.html', **templatedata, data=data)


##RackU202 page
@app.route('/racku202')
def RackU202():
    session['url'] = flask.request.url
    global tablenow
    tablenow = flask.request.url
    mycursor.execute("SELECT * FROM racku202")
    data = mycursor.fetchall()

    templatedata = {
        'title' : 'racku202'
        }

    return render_template ('Lijstvanservers.html', **templatedata, data=data)



##RackU203 page
@app.route('/racku203')
def RackU203():
    session['url'] = flask.request.url
    global tablenow
    tablenow = flask.request.url
    mycursor.execute("SELECT * FROM racku203")
    data = mycursor.fetchall()

    templatedata = {
        'title' : 'racku203'
        }


    return render_template ('Lijstvanservers.html', **templatedata, data=data)



##RackU205 page
@app.route('/racku205')
def RackU205():
    session['url'] = flask.request.url
    global tablenow
    tablenow = flask.request.url
    mycursor.execute("SELECT * FROM racku205")
    data = mycursor.fetchall()

    templatedata = {
        'title' : 'racku205'
        }


    return render_template ('Lijstvanservers.html', **templatedata, data=data)



##RackU206 page
@app.route('/racku206')
def RackU206():
    session['url'] = flask.request.url
    global tablenow
    tablenow = flask.request.url
    mycursor.execute("SELECT * FROM racku206")
    data = mycursor.fetchall()

    templatedata = {
        'title' : 'racku206'
        }


    return render_template ('Lijstvanservers.html', **templatedata, data=data)


##RackU207 page
@app.route('/racku207')
def RackU207():
    session['url'] = flask.request.url
    global tablenow
    tablenow = flask.request.url
    mycursor.execute("SELECT * FROM racku207")
    data = mycursor.fetchall()

    templatedata = {
        'title' : 'racku207'
        }


    return render_template ('Lijstvanservers.html', **templatedata, data=data)

##Return page (to the last session)
@app.route('/return')
def return0():
    return redirect(session['url'])

##Site connection / port: define / debugging
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(port=80, debug=True)
