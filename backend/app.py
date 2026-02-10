from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Backend!"

@app.route("/api")
def api():
    return "Backend API working"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
