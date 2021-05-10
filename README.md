# ImageServer
A prototype Restful server and client that allow a user to search and retrieve medical images from a central storage location.

## Setup
### Client

In the Client/client directory, run the following shell instructions.
```
npm install
```
Compiles and hot-reloads for development
```
npm run serve
```

### Server

In the Server folder, run the following shell instructions.
```
python3 app.py
```

Open http://localhost:8080/ on browser to access the Client page.

You should see something like this:

<img src="client_demo.png" width="700" height="400">


## System Components

1. Client (Vue.js)
2. Server (Flask)
3. Database (MySql on AWS RDS)
4. Data Storage (AWS S3)

## Components design and characteristics

### Process
1. The Vue client sends REST Get request with the data containing patient's first name and last name by Axios. 
2. The Flask server receives the request.
3. The Flask server fetch the data from the MySql database on AWS RDS with sql query.
4. The Flask server sends back response to Vue client.
5. Vue client displays client's images.

### Client

The client is implemented with VueJs on NodeJs JavaScript runtime environment. I chose Vue for framework because of my prior project experience and its fast learning curve.

### Server

The server is implemented by Python Flask to satisfy the requirement language. I chose Flask becasue it is fast and lightweight, with the ability of easy and fast deployment. The server can be easily duplicated for system scalability improvement. I also has prior Flask project experience.

### Database and Storage

I chose a Mysql database because the data related to system is highly relational and structured. The database is deployed on AWS RDS for several reasons: avaliability, security and scalability. 

1. Ideally the hospital system would require a high avaliability concern so the docter should always be able to get patient's image during surgery or visiting hours. The AWS RDS helps us handle the avaliability issue as their cloud service has solutions to ensure avaliability.
2. The Database would need security mechanism to protect patients' data. AWS's cloud service ensure database's security, and our system could use secure communication to protect the data transmission.
3. Scalability. AWS's service provide easy scale-up and scale-down.

I chose AWS RDS for storage for the same concerns as database: avaliability, security and scalability.

Currenlty both database and storage are set as public accessable. We can change the set up to be protected mechanism in future.

The database has 2 tables.

| Patient     |             |           |        |
| ----------  | ------------|-----------|--------|
| patient_id  | first_name  | last_name | birthday|

| Image     |             |            |           |    
| ----------| ------------|------------|-----------|
| image_id  | patient_id  | date_taken | image_url |

## System Design Characteristic

1. High Avaliability: Use AWS to ensure avlaiblity features
2. Security - ideally. sensitive data. maybe use JWT as authentication to access the platform, use Https for security, end to end encrpted, in future

### Future Thoughts
1. Automation implementation: Docker, Kubernete, Jenkins
2. Code improvement: Sanitization of inputs.
3. Unit Testing


