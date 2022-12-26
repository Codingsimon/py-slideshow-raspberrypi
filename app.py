import os
import flask
#import slideshow
from flask import Flask, render_template
from flask_milligram import Milligram

app = Flask(__name__)
milligram = Milligram(app)

@app.route("/")
def hello_world():
    # return your_module.your_function_in_the_module()
    return render_template('index.html')

if __name__ == '__main__':
    os.system("python slideshow.py")
    app.run(debug=True)