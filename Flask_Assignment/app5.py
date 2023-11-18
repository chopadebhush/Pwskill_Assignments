from flask import Flask ,render_template,request ,redirect ,url_for,jsonify
from flask import *

app =Flask(__name__)

@app.route("/")
def uploadPage():
    return render_template("UP_index.html")

@app.route("/success",methods=["POST","GET"])
def success():
    if request.method =="POST" :
        f =request.files["file"]
        f.save(f.filename)
        return render_template("UP_Ack.html",name =f.filename)


if __name__ == "__main__" :
    app.run(host="0.0.0.0",port=5005 ,debug= True)