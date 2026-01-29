from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    return jsonify({"response": "AI processing: " + data.get('message', '')})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
