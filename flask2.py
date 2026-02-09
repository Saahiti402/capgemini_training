from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    print(">>> Root endpoint HIT")
    return "Hello!!"

@app.route('/hello')
def hello_world():
    print(">>> /hello endpoint HIT")
    return "Hello World!!"

if __name__ == '__main__':
    app.run(debug=True)
