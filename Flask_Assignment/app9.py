from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


@app.route("/")
def Hello():

    return "Welcome to webPage"

@app.errorhandler(404)
def Invalid_route(e):
    return "Invalid route"

@app.errorhandler(500)
def internalerror(e):
    return "500 Error"



if __name__ == '__main__':
    app.run(host ="0.0.0.0",port =5001, debug=True)