from flask.json import jsonify
from flask import jsonify
from app import app

@app.route('/connection-test/')
def connection_test():
    return jsonify({"data": [], "message": "Connection established successfully!"})

if __name__ == '__main__':
    app.run(debug=True)