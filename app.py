from flask import Flask, render_template, request, jsonify
from logic.trainer import get_hand_scenario, evaluate_action

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_hand', methods=['GET'])
def new_hand():
    mode = request.args.get('mode', 'response')
    scenario = get_hand_scenario(mode)
    return jsonify(scenario)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    result = evaluate_action(data['position'], data.get('opener'), data['hand'], data['action'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

