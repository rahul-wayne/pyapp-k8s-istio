from flask import Flask, request, redirect, url_for, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Setup MongoDB connection
client = MongoClient('mongodb://mongodb-service:27017/')
db = client['microserviceDB']
collection = db['data']

#@app.route('/')
#def index():
#    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        data = request.form
        collection.insert_one({'title': data['title'], 'content': data['content']})
        return redirect(url_for('add_data'))
    return render_template('add_data.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)