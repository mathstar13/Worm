from flask import *
app = Flask(__name__)
@app.route('/package/<n>')
def gpkg(n):
	