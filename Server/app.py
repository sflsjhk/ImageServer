from flaskext.mysql import MySQL
from flask import Flask, render_template, jsonify,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MySql setup
app.config['MYSQL_DATABASE_HOST'] = "image-sql.cz2espbhrwak.us-east-1.rds.amazonaws.com"
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = "admin"
app.config['MYSQL_DATABASE_PASSWORD'] = "intuitive"
app.config['MYSQL_DATABASE_DB'] = "image_sql"
mysql = MySQL()
mysql.init_app(app)	
conn = mysql.connect()

# Get Patient's image from first_name, last_name
@app.route('/', methods = ['GET'])
def index():
    # Get Patient's first/last name from Restful API Json Request
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    print(first_name)
    if not first_name or not last_name:
        # no input
        return jsonify({'error':'input missing'})
    else:
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
            img_list = []
            for image in patientImages:
                image_details = {
                  'image_url': image[3],
                  'date_taken': image[2]
                }
                img_list.append(image_details)
            return jsonify({'patient_name':first_name + ' ' + last_name, 'images':img_list})
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
        patient_images = cursor.fetchall()
        cursor.close()
        img_list = []
        for image in patient_images:
            image_details = {
                  'image_url': image[3],
                  'date_taken': image[2]
                }
            img_list.append(image_details)
        return jsonify({'patient_id':patient_id, 'images':img_list})
    else:
        cursor.close()
        return jsonify({'error':'Patient does not have image in database'})

if __name__ == '__main__':
    app.run(debug = True)