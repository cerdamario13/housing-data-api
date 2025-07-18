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
    
@app.route('/affordability', methods=['GET'])
def affordability():
    """
    Get Metro Area-Typical Home Value and Mortgage Affordability: April 2022
    """
    location = request.args.get('location')
    try:
        data = model.read_home_affordability_2022(location)
        return jsonify(data)
    except Exception as e:
        print(str(e))
        return jsonify({'message': 'Error occurred'}), 500

@app.route('/yty_change', methods=['GET'])
def yty_change():
    """
    Get the Year to Year change for Rent and Home Value
    """
    location = request.args.get('location')
    try:
        data = model.year_to_year_change(location)
        return jsonify(data)
    except Exception as e:
        print(str(e))
        return jsonify({'message': 'Error occurred'})

if __name__ == '__main__':
    app.run(debug=False, port=8000, host='0.0.0.0')