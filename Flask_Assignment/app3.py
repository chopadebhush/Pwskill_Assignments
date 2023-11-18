##4. Create a Flask app with a form that accepts user input and displays it.


from flask import Flask ,render_template ,request,redirect ,url_for

app =Flask(__name__)

@app.route('/')
def index():
    return render_template("index3.html")

@app.route("/submit",methods =["POST" ,"GET"])
def index2():
    user_input =request.form["user_input"]
    return render_template("index4.html",user =user_input)






if __name__ =="__main__" :
    app.run(host= "0.0.0.0" ,port=5003,debug=True)