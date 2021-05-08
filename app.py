from flaskext.mysql import MySQL
from flask import Flask

app = Flask(__name__)

# MySql setup
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "ROOT"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "ion_image"

mysql = MySQL(app)

@app.route('/')
def index():
    return "Ion Image Server"

if __name__ == '__main__':
    app.run(debug = True)