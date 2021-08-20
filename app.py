!flask/bin/python
from flask import Flask, jsonify, request

app = Flask(__name__)

temperature = [
   {
        'id': 1,
        'current-temp': "68",
        'set-temp': "72"
   }
]

@app.route('/ThermsAreUs/api/v1.0/current-temp', methods=['GET'])
def get_current():
    return jsonify({'current-temp': temperature[0]["current-temp"]})

@app.route('/ThermsAreUs/api/v1.0/current-setpoint', methods=['GET'])
def get_desired():
    return jsonify({'current-setpoint': temperature[0]["set-temp"]})

@app.route('/ThermsAreUs/api/v1.0/current-setpoint', methods=['PUT'])
def update_temp():
    temperature[0]['set-temp'] = request.json.get('set-temp', temperature[0]['set-temp'])
    return jsonify({'current-setpoint': temperature[0]["set-temp"]})
if __name__ == '__main__':
    app.run(debug = True,host="0.0.0.0")