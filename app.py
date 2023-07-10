import random
import time

from flask import jsonify
from flask_api import FlaskAPI, status
from opentelemetry.instrumentation.flask import FlaskInstrumentor

api = FlaskAPI(__name__)
FlaskInstrumentor().instrument_app(api)

@api.route('/')
def root_path():
    return jsonify({"message": "root path of the app"}), status.HTTP_200_OK

def _sleep():
    time.sleep(1)

def _roll_dice():
    return random.randint(0, 9)

@api.route('/roll')
def roll_path():
    _sleep()
    r = _roll_dice()
    if r in range(1, 6):
        return jsonify({"output": r}), status.HTTP_200_OK
    elif r > 6:
        return jsonify({"error": f"output:{r} beyond range(1-6)"}), status.HTTP_501_NOT_IMPLEMENTED
    else:
        return jsonify({"error": f"output=0"}), status.HTTP_500_INTERNAL_SERVER_ERROR

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=8080, debug=True, use_reloader=False)

