from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    print("FULL PATH:", request.full_path)
    print("METHOD:", request.method)
    print("HEADERS:", dict(request.headers))
    print("BODY:", request.get_data(as_text=True))

    return jsonify({
        "status": 0,
        "message": "ANNIE_CONFIG_ACTIVE",
        "login": "ok",
        "config": {
            "aim_assist": 100,
            "aim_assist_range": 999,
            "aim_assist_angle": 180,
            "headshot_rate": 100,
            "aim_target": "head",
            "no_recoil": 1,
            "no_spread": 1,
            "auto_fire": 1,
            "anti_ban": 1,
            "check_version": 0,
            "check_resource": 0,
            "check_hacker": 0
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)