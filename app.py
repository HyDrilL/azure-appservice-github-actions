from flask import Flask

app = Flask(__name__)


@app.route("/")
def home() -> str:
    return "Azure App Service CI/CD demo by Mustapha"


@app.route("/health")
def health() -> str:
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)