from flask import Flask, request
from pymongo import MongoClient
from flask_cors import CORS # pip install Flask-Cors

app = Flask(__name__)
CORS(app)
client = MongoClient("mongo", 27017) # Nombre del servicio MongoDB en docker-compose.yml
db = client.sampledb  # Nombre de la base de datos
collection = db.datacollection  # Nombre de la colección

@app.route('/store', methods=['POST'])
def store_data():
    data = request.json['data']
    collection.insert_one({"data": data})
    return 'Data stored in MongoDB', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
