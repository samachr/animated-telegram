import os, json
from flask import Flask, render_template, request
app = Flask(__name__)

ipaddr = os.getenv("IP", "0.0.0.0")
port = int(os.getenv("PORT", 3000))

# server globals
tracking={}

@app.route('/api/input_example', methods = ['POST', 'GET'])
def save_search():
    input_param = request.args.get("search")
    if input_param in tracking:
        tracking[input_param] += 1
    else:
        tracking[input_param] = 1

    return input_param

@app.route('/api/json_example', methods = ['GET'])
def get_json_stuff():
    return json.dumps({"key":"value"})

@app.route('/', methods = ['GET'])
def index():
    global tracking
    return render_template('index.html', tab="", tracking=tracking)

@app.route('/app.js', methods = ['GET'])
def appjs():
    global tracking
    global top100
    return render_template('app.js')

if __name__ == '__main__':
    app.run(host=ipaddr, port=port, debug=False)
