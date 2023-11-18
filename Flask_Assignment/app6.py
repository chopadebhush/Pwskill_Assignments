## 7. Integrate a SQLite database with Flask to perform CRUD operations on a list of items

from flask import Flask,request,render_template ,redirect,url_for
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("SQ_index.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/submit",methods =["POST","GET"])
def save_detail():
    if request.method == "POST" :
        try :
            Id =request.form["Id"]
            name =request.form["name"]
            address =request.form["address"]

            with sqlite3.connect("sql.db") as con :
                cursor =con.cursor()
                cursor.execute("INSERT INTO student(id ,name,address)values(?,?,?)",(Id,name,address))
                con.commit()
                msg ="record added in  database"
        except :
            
            con.rollback()
            msg ="Error in insert"
        
        finally:
            con.close()
            return render_template("success.html",msg=msg)

@app.route("/view")
def view():
    con =sqlite3.connect("sql.db")
    con.row_factory = sqlite3.Row  
    cursor = con.cursor()  
    cursor.execute("SELECT * FROM student")  
    rows = cursor.fetchall()  
    return render_template("view.html",rows = rows) 

@app.route("/delete" )
def delete():
    return render_template("delete.html")


@app.route("/deleterecord",methods= ["POST"])
def delete_record():
    Id =request.form["Id"]
    with sqlite3.connect("sql.db") as con:
        try :
            cursor =con.cursor()
            cursor.execute("delete from student where id =?",Id)
            msg ="record sucessfully deleted"
        except :
            msg ="cant be deleted"

        finally :
            return render_template("delete_record.html",msg =msg)

if __name__ == "__main__" :
    app.run(host="0.0.0.0",debug =True)