from flask import Flask, jsonify

app = Flask(__name__)

students_data = {
    1: {"name": "Anu", "dept": "CSE", "year": 3},
    2: {"name": "Karthi", "dept": "ECE", "year": 2},
    3: {"name": "Priya", "dept": "IT", "year": 4}
}

@app.route('/students', methods=['GET'])
def get_all_students():
    try:
        return jsonify(students_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        print("GET ALL Students called")

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    try:
        if student_id not in students_data:
            return jsonify({"error": "Student not found"}), 404
        return jsonify({
            "student_id": student_id,
            "details": students_data[student_id]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        print("GET Students by ID called")

if __name__ == '__main__':
    app.run(debug=True, port=8003)
