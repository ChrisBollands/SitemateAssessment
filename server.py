from flask import Flask, request, jsonify

app = Flask(__name__)

# write the data to a file and read/write to it

issues = []

# Endpoint to create a new JSON object
@app.route('/create', methods=['POST'])
def create():
    new_object = request.get_json()
    issues.append(new_object)

# Endpoint to read all JSON objects
@app.route('/read', methods=['GET'])
def read():
    return jsonify(issues)

# Endpoint to update a JSON object by its index
@app.route('/update/<int:index>', methods=['PUT'])
def update(index):
    if index < len(issues):
        updated_object = request.get_json()
        issues[index] = updated_object
        return jsonify({'message': 'Object updated successfully'})
    else:
        return jsonify({'error': 'Invalid index'})

# Endpoint to delete a JSON object by its index
@app.route('/delete/<int:index>', methods=['DELETE'])
def delete(index):
    if index < len(issues):
        del issues[index]

if __name__ == '__main__':
    app.run(debug=True)