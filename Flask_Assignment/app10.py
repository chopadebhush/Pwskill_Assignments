##11. Create a real-time chat application using Flask-SocketIO

from flask import Flask,render_template ,redirect ,url_for

from flask_socketio import SocketIO,send
app =Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")



@socketio.on("messege")
def handdle_mseesege(messege):
    send(messege ,broadcast =True)



@app.route("/")
def socket_index():
    return render_template("socket_IO.html")

if __name__ =="__main__":
    app.run(host="0.0.0.0",port =5001,debug= True)