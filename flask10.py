from flask import Flask, request, jsonify

app = Flask(__name__)

users_data = {
    "anu": {"password": "anu123", "role": "admin", "account_no": 1234, "balance": 50000, "adhar": 1234567, "pan": "QC45", "phone": 896567},
    "karthi": {"password": "karthi88", "role": "student", "account_no": 2345, "balance": 30000, "adhar": 2234567, "pan": "AB12", "phone": 996567},
    "priya": {"password": "priya99", "role": "teacher", "account_no": 3456, "balance": 70000, "adhar": 3234567, "pan": "RT78", "phone": 786567},
    "ram": {"password": "ram123", "role": "student", "account_no": 4567, "balance": 20000, "adhar": 4234567, "pan": "YU90", "phone": 696567},
    "sita": {"password": "sita456", "role": "admin", "account_no": 5678, "balance": 90000, "adhar": 5234567, "pan": "LO34", "phone": 596567}
}

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form.get("username")
        password = request.form.get("password")

        if username not in users_data:
            return jsonify({"error": "User not found"}), 404

        if users_data[username]["password"] != password:
            return jsonify({"error": "Incorrect password"}), 401

        return jsonify({
            "message": "Login successful",
            "username": username,
            "role": users_data[username]["role"]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        print("LOGIN endpoint called")


@app.route('/users', methods=['GET'])
def users():
    try:
        return jsonify(users_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        print("GET ALL Users called")


@app.route('/users/<string:username>', methods=['GET'])
def get_user_by_username(username):
    try:
        if username not in users_data:
            return jsonify({"error": "User not found"}), 404
        
        return jsonify({
            "username": username,
            "details": users_data[username]
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        print("GET Users by username called")


@app.route('/users/<string:username>/balance', methods=['GET', 'PUT'])
def user_balance(username):
    try:
        if username not in users_data:
            return jsonify({"error": "User not found"}), 404

        if request.method == 'GET':
            return jsonify({
                "username": username,
                "balance": users_data[username]["balance"]
            })

        if request.method == 'PUT':
            data = request.form or request.json

            if "balance" not in data:
                return jsonify({"error": "balance is required"}), 400

            users_data[username]["balance"] = data["balance"]

            return jsonify({
                "message": "Balance updated successfully",
                "username": username,
                "new_balance": users_data[username]["balance"]
            })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/users/<string:username>/adhar',methods=['GET'])
def adhar(username):
    try:
        if username not in users_data:
            return jsonify({"error": "User not found"}), 404
        return jsonify({
            "Username": username,
            "Adhar card number": users_data[username]["adhar"]
            })
    except Exception as e:
        return jsonify({"error":str(e)}), 500
    
@app.route('/users/<string:username>/pan',methods=['GET'])
def pan(username):
    try:
        if username not in users_data:
            return jsonify({"error": "User not found"}), 404
        return jsonify({
            "Username": username,
            "Pan card number": users_data[username]["pan"]
            })
    except Exception as e:
        return jsonify({"error":str(e)}), 500
    
@app.route('/users/<string:username>/phone',methods=['GET'])
def phone(username):
    try:
        if username not in users_data:
            return jsonify({"error": "User not found"}), 404
        return jsonify({
            "Username": username,
            "Phone number": users_data[username]["phone"]
            })
    except Exception as e:
        return jsonify({"error":str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=8007)
