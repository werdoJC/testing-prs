from flask import render_template
from imagebattle import app


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/leading', methods=['GET'])
def leading():
    return render_template('leading.html')
