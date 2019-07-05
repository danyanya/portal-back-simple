from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def index():
  return 'it works!'

def login(username, code):
    if username == 'bob' and code == 'marley':
        return {"traffic": 12, "minutes":13}, True
    return {}, False

@app.route('/check', methods=['POST'])
def get_user():
  username = request.form['username']
  code = request.form['code']
  response, err = login(username,code)
  response = jsonify(response)
  if not err:
      response.status_code = 403
  return response
