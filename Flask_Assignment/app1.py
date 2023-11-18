## Build a Flask app with static HTML pages and navigate between them

from flask import Flask ,request ,render_template ,jsonify

app =Flask(__name__)

@app.route("/")
def home():
    return render_template("index1.html")



@app.route("/index2.html", methods = ['GET', 'POST'])
def about():
    return render_template("index2.html")


if __name__ == "__main__" :
    app.run(host= "0.0.0.0" ,port=5001)