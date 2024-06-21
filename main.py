from flask import Flask, request, jsonify, Response
import requests

app = Flask(__name__)

@app.route('/get-google-doc', methods=['GET'])
def get_google_doc():
    try:
        page = request.args.get('page', default=1, type=int)
        page_size = request.args.get('page_size', default=100, type=int)
        url = f"https://hook.us1.make.com/dhdnk5s11kugf2jj8hwjta68uph0ssc7?page={page}&pageSize={page_size}"
        headers = {
            "Accept": "text/plain"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        # Return the response text
        return Response(response.text, mimetype='text/plain')

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Request to external API failed", "message": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
