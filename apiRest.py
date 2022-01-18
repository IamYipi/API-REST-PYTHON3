from flask import Flask, jsonify

# Initialize Flask

app = Flask(__name__)

# Jsonify variable

examples = [{'name': "Example 0",
             'example_id': "0",
             'Description': "This is the example 0 for the API restful using flask",
             'price': "pay me with BTC"},
            {'name': "Example 1",
             'example_id': "1",
             'Description': "This is the example 1 for the API restful using flask",
             'price': "pay me with ETH"}]


# For lunch the API in a virtual machine local web server http://127.0.0.1:5000/ or http://localhost:5000/

@app.route('/')
def index():
    return "Welcome Yipi's API REST"

  
# For run introduce the next url:
# http://127.0.0.1:5000/examples

@app.route("/examples", methods=['GET'])
def get():
    return jsonify({'Examples': examples})


# For run introduce the next url:
# http://127.0.0.1:5000/examples/id
# id is the number of the example you want to see

@app.route("/examples/<int:example_id>", methods=['GET'])
def get_example(example_id):
    return jsonify({'example': examples[example_id]})


# For run introduce in a second terminal:
# curl -i -H "Content-Type: Application/json" -X POST http://localhost:5000/examples

@app.route("/examples", methods=['POST'])
def create():
    example = {'name': "Example 2",
               'example_id': "2",
               'Description': "This is the example 2 for the API restful using flask",
               'price': "pay me with SOL"}
    examples.append(example)
    return jsonify({'Created': example})


# For run introduce in a second terminal:
# curl -i -H "Content-Type: Application/json" -X PUT http://localhost:5000/examples/id
# -- id is the number you want to put

@app.route("/examples/<int:example_id>", methods=['PUT'])
def example_update(example_id):
    examples[example_id]['Description'] = "Description has been changed :D"
    return jsonify({'example': examples[example_id]})


# For run introduce in a second terminal:
# curl -i -H "Content-Type: Application/json" -X DELETE http://localhost:5000/examples/id
# -- id is the number you want to delete

@app.route("/examples/<example_id>", methods=['DELETE'])
def delete(example_id):
    examples.remove(examples[example_id])
    return jsonify({'result': True})


# For run Main

if __name__ == '__main__':
    app.run(debug=True)
