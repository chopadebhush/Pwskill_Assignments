## 3. Develop a Flask app that uses URL parameters to display dynamic content.

from flask import Flask ,request ,render_template ,jsonify

app  =Flask(__name__)


@app.route("/")
def dynamic_content():
    return "welcome to the dynamic content app"


@app.route("/greet")
def greet():
    data =request.args.get("name")
    
    if data :
        return f"Hello {data}"
    else:
        return f"Hello anaymous"


        

if __name__ =="__main__" :
    app.run(host= "0.0.0.0" ,port=5002)