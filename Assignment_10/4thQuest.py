from flask import Flask, jsonify
import json
import os

#Some of the imports are not from my understanding, because I asked a friend of mine on discord to help this out

app = Flask(__name__)

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, 'airports.json') # like this one

with open(json_path, 'r') as f:
    airports = json.load(f) # this one

@app.route('/airport/<string:icao>')

def get_airport(icao):
    airport = next((airport for airport in airports if airport['icao'].upper() == icao.upper()), None) # and this one for the formatting thingy
     
    if airport:
        return jsonify(airport)
    else:
        response = {
            "error": "Airport not found"
        }
        return jsonify(response), 404

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
