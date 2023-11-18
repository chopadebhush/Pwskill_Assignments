from flask import Flask ,request ,render_template ,redirect ,url_for,session

app =Flask(__name__)

app.config['SECRET_KEY'] ="Bhushan8912"
app.config['SESSION_TYPE'] = 'filesystem'

# @app.route("/")
# def Welcome():
#     return render_template("index5.html")

# @app.route("/submit",methods =["POST" ,"GET"])
# def login():
#     user_name =request.form["user_input"]
#     password =request.form["password"]

#     if (user_name == "bhushan" and password == "Bhushan8912"):

#         return "Welcome to Login page. You Have succesfully login"
        
#     else:
        
#         return "You have Wrong details"


@app.route("/")
def index():
    return "Welcome to the Flask User Session Example"


@app.route("/Login",methods =["POST" ,"GET"])
def login() :
    if request.method == "POST" :
        user_name =request.form["username"] 
        session["user_name"] =user_name
        return redirect(url_for("profile"))
    else:
        return render_template("Login.html")

@app.route("/profile")
def profile():
    user_name =session.get("user_name")
    if user_name  :
        return f"Hello {user_name} Thise is your profile"
    else :
        return "Please log in to access your profile."




if __name__ =="__main__" :
    app.run(debug=True ,host ="0.0.0.0",port = 5004)