from flask import Flask, render_template

import platform
 
os= platform.uname()
os = list(os)
app = Flask(__name__)

@app.route("/")
def home():
    return  render_template("index.html",os=os[0],name=os[1],release=os[2],version=os[3],machine=os[4])


if __name__ =="__main__":
    app.run(debug=False,port =0.0.0.0)

    