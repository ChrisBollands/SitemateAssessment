from flask import Flask, request, jsonify

app = Flask(__name__)

# write the data to a file and read/write to it

issues = []

# Endpoint create
@app.route('/create', methods=['POST'])
def create():
    new_object = request.get_json()
    issues.append(new_object)
    return jsonify({'message': 'Record created successfully'})

# Endpoint read
@app.route('/read', methods=['GET'])
def read():
    return jsonify(issues)

# Endpoint update
@app.route('/update/<int:index>', methods=['PUT'])
def update(index):
    updated_issue = request.get_json()
    if 0 <= index < len(issues):
        issues[index] = updated_issue
        print(issues)
        return jsonify({'message': 'Object updated successfully'})
    else:
        return jsonify({'error': 'Object not found'})


# # Endpoint delete
# @app.route('/delete/<int:index>', methods=['DELETE'])
# def delete(index):

if __name__ == '__main__':
    app.run(debug=True)