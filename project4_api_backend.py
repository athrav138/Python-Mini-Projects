from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculate", methods=["POST"])
def calculate():

    data = request.get_json()

    x = data.get("x")
    y = data.get("y")
    operation = data.get("operation")

    if None in (x, y, operation):
        return jsonify({
            "error": "Missing input"
        }), 400

    try:
        x = float(x)
        y = float(y)

    except ValueError:
        return jsonify({
            "error": "Invalid numbers"
        }), 400

    if operation == "add":
        result = x + y

    elif operation == "subtract":
        result = x - y

    elif operation == "multiply":
        result = x * y

    elif operation == "divide":

        if y == 0:
            return jsonify({
                "error": "Division by zero"
            }), 400

        result = x / y

    else:
        return jsonify({
            "error": "Invalid operation"
        }), 400

    return jsonify({
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)