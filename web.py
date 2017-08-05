from flask import Flask, render_template, request
import os
from data import Data
app = Flask(__name__)

@app.route('/')
def index():
    #name = request.values.get('name')
    a = Data()
    return render_template('index.html',a=a)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    """
    app.run()
    """

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
