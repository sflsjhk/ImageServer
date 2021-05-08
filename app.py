from flaskext.mysql import MySQL
from flask import Flask, render_template, jsonify,request

app = Flask(__name__)

# MySql setup
app.config['MYSQL_DATABASE_HOST'] = "localhost"
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = "abc26604331"
app.config['MYSQL_DATABASE_DB'] = "ion_image"

mysql = MySQL()
mysql.init_app(app)	
conn = mysql.connect()

# Get Patient's image from first_name, last_name
@app.route('/', methods = ['GET'])
def index():
    # Get Patient's first/last name from Restful API Json Request
    patient_json = request.get_json()
    if not patient_json:
        # no input
        return jsonify({'error':'input missing'})
    else:
        first_name = patient_json['first_name']
        last_name = patient_json['last_name']
        
        # Mysql Cursor for getting Data in DB
        cursor = conn.cursor()
        # Query to get images by first/last name
        cursor.execute("SELECT * FROM Patients WHERE (first_name = %s AND last_name = %s)",(first_name,last_name))
        # get patient detail as tuple
        patient = cursor.fetchone()
        
        # If fetch result is empty
        if not patient:
            return jsonify({'error':'Patient does not exist in database'})
        
        # Query to get images by patient id
        patient_id = patient[0]
        images = cursor.execute("SELECT * FROM Images WHERE patient_id = %s", patient_id)
        if images >= 1:
            patientImages = cursor.fetchall()
            cursor.close()
            img_set = []
            for image in patientImages:
                img_set.append(image[3])
            return jsonify({'patient_name':patient_json, 'imageURLs':img_set})
        else:
            cursor.close()
            return jsonify({'error':'Patient does not have image in database'})

# Get Patient's images by patient_id
@app.route('/patient/<int:patient_id>', methods = ['GET'])
def getImageById(patient_id):
    cursor = conn.cursor()
    # Query to get images by patient id
    images = cursor.execute("SELECT * FROM Images WHERE patient_id = %s", patient_id)
    if images >= 1:
        patientImages = cursor.fetchall()
        img_set = []
        for image in patientImages:
            img_set.append(image[3])
        return jsonify({'patient_id':patient_id, 'imageURLs':img_set})
    else:
        return jsonify({'error':'Patient does not have image in database'})

if __name__ == '__main__':
    app.run(debug = True)