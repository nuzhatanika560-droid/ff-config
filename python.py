from flask import Flask, request, jsonify

app = Flask(__name__)

WORKING_RESPONSE = {
    "maintenance_msg": "Server is under maintenance. Please try later.",
    "abhotupdate_cdn_url": "https://ffp.springmusk.dev/hotpatchs/",
    "is_server_open": True,
    "patchnote_url": "https://t.me/nepgamer",
    "billboard_cdn_url": "https://ff.springmusk.dev/ffmax/pausedg.jpg;https://ff.springmusk.dev/ffmax/564c3e03-2204-476d-89c7-365b8fbd22f4.png",
    "billboard_bg_url": "",
    "billboard_msg": "",
    "web_url": "https://t.me/nepgamer",
    "test_url": "https://t.me/nepgamer",
    "is_update_btn_show": False,
    "show_high_framerate_UI": True,
    "appstore_url": "https://t.me/nepgamer",
    "backup_appstore_url": "https://t.me/nepgamer"
}

@app.route('/ver.php', methods=['GET', 'POST'])
def ver():
    print("VER PATH:", request.full_path)
    return jsonify(WORKING_RESPONSE)

@app.route('/MajorLogin', methods=['GET', 'POST'])
def major_login():
    print("MAJORLOGIN BODY:", request.get_data(as_text=True))
    print("MAJORLOGIN HEADERS:", dict(request.headers))
    return jsonify(WORKING_RESPONSE)

@app.route('/Ping', methods=['GET', 'POST'])
def ping():
    print("PING BODY:", request.get_data(as_text=True))
    return jsonify({"status": 0, "message": "ok"})

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    print("CATCH PATH:", request.full_path)
    print("CATCH BODY:", request.get_data(as_text=True))
    return jsonify(WORKING_RESPONSE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
