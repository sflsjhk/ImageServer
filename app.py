from flaskext.mysql import MySQL
from flask import Flask, render_template, jsonify,request

app = Flask(__name__)

# MySql setup
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "ROOT"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "ion_image"

mysql = MySQL(app)

# Get Patient's image from first_name, last_name
@app.route('/', methods = ['GET'])
def index():
    # Get Patient's first/last name from Restful API Json Request
    patient_json = request.get_json()
    first_name = patient_json['first_name']
    last_name = patient_json['last_name']
    return jsonify({'patient_name':patient_json})

# Get Patient's images by patient_id
@app.route('/patient/<int:patient_id>', methods = ['GET'])
def getImageById(patient_id):
    return jsonify({'result':patient_id})


if __name__ == '__main__':
    app.run(debug = True)