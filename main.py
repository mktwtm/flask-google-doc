from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/get-google-doc', methods=['GET'])
def get_google_doc():
    page = request.args.get('page', default=1, type=int)
    page_size = request.args.get('page_size', default=100, type=int)
    url = f"https://hook.us1.make.com/dhdnk5s11kugf2jj8hwjta68uph0ssc7?page={page}&pageSize={page_size}"
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": response.status_code, "message": response.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
