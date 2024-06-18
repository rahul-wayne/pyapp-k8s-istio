from flask import Flask, render_template, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# Setup MongoDB connection
client = MongoClient('mongodb://mongodb-service:27017/')
db = client['microserviceDB']
collection = db['data']

@app.route('/view')
def view_data():
    data = list(collection.find())
    for item in data:
        item['_id'] = str(item['_id'])
    return render_template('view_data.html', data=data)

@app.route('/delete/<id>', methods=['GET'])
def delete_data(id):
    collection.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('view_data'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)