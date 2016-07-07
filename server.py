import os, json
from flask import Flask, render_template, request
app = Flask(__name__)

ipaddr = os.getenv("IP", "0.0.0.0")
port = int(os.getenv("PORT", 3000))

from pymongo import MongoClient
MONGODB_URI = 'mongodb://pythontest:pythonpass@ds015915.mlab.com:15915/heroku_l6st7jg1'
client = MongoClient(MONGODB_URI)
db = client.get_default_database()
testdb = db['test']

@app.route('/api/input_example', methods = ['POST', 'GET'])
def save_search():
    global testdb
    input_param = request.args.get("search")
    result = testdb.find_one({"search_text":input_param})
    if result:
        testdb.update({"search_text":input_param}, {"$set": {"frequency": result["frequency"] + 1}})
    else:
        testdb.insert({"search_text":input_param, "frequency":1})

    return input_param

@app.route('/api/json_example', methods = ['GET'])
def get_json_stuff():
    return json.dumps({"key":"value"})

@app.route('/', methods = ['GET'])
def index():
    global testdb
    docs = [doc for doc in testdb.find()]
    return render_template('index.html', tab="", tracking=docs)

@app.route('/app.js', methods = ['GET'])
def appjs():
    global tracking
    global top100
    return render_template('app.js')

if __name__ == '__main__':
    app.run(host=ipaddr, port=port, debug=False)
