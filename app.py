import os
import flask
import subprocess
from flask import Flask, render_template
from flask_milligram import Milligram

app = Flask(__name__)
milligram = Milligram(app)

@app.route("/")
def hello_world():
    # return your_module.your_function_in_the_module()
    return render_template('index.html')

if __name__ == '__main__':
    print("before")
    #os.system("python slideshow.py")
    subprocess.Popen(["python","slideshow.py"])
    print("after")
    app.run(debug=True)