from flask import Flask, request, jsonify
import model
from flask_cors import CORS

# Init app
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def heartbeat():
    return jsonify({'message': 'Connected to the server'})


@app.route('/pi_ratio', methods=['GET'])
def pi_ratio():
    """
    Get the house-price-to-income ratio is a measure used to evaluate housing affordability
    """

    location = request.args.get('location')

    try:
        data = model.read_house_pi_xl(location)
        return jsonify(data)
    except Exception as e:
        print(str(e))
        return jsonify({'message': 'Error occurred'}), 500


if __name__ == '__main__':
    app.run(debug=False, port=8000, host='0.0.0.0')