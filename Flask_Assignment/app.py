## Question 1 : Create a Flask app that displays "Hello, World!" on the homepage.



from flask import Flask ,request ,render_template ,jsonify

app =Flask(__name__)

@app.route("/homepage")
def Homepage():
    return render_template("index.html")


if __name__ =="__main__" :
    app.run(host= "0.0.0.0" ,port=5000)
