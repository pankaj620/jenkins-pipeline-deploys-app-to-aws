from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Python deployed via Jenkins!"

@app.route('/health')
def healthCheck():
    return "website is running healthy"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
