from flask import Flask, jsonify

 
app = Flask(__name__)


@app.route('/')
def home():
    return jsonif(message="Hello my name is Tidding Ramsey B")
    


if __name__ == '__main__':
    app.run(debug=True)
    