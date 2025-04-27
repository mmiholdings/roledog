from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/sentiment', methods=['POST'])
def sentiment():
    text = request.json.get('text', '')
    score = round(random.uniform(-1, 1), 3)  # Fake sentiment score
    result = {
        'text': text,
        'sentiment_score': score,
        'confidence': round(random.uniform(0.7, 0.99), 2)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
