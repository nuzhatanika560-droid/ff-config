from flask import Flask, request, jsonify
from urllib.parse import unquote
import base64
import sys

app = Flask(__name__)

@app.route('/MajorLogin', methods=['GET', 'POST'])
def major_login():
    raw = request.get_data(as_text=True)
    print("MAJORLOGIN_RAW:", raw, flush=True)
    print("MAJORLOGIN_URL_DECODED:", unquote(raw), flush=True)
    try:
        print("MAJORLOGIN_B64:", base64.b64decode(raw).decode('utf-8', errors='ignore'), flush=True)
    except:
        pass
    return jsonify({"status": 0, "login": "ok"})

@app.route('/Ping', methods=['GET', 'POST'])
def ping():
    return jsonify({"status": 0, "message": "ok"})

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    raw = request.get_data(as_text=True)
    print("PATH:", request.full_path, flush=True)
    print("BODY_RAW:", raw, flush=True)
    print("BODY_URL_DECODED:", unquote(raw), flush=True)
    return jsonify({"status": 0, "login": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)