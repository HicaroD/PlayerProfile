from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, world</p>"

@app.route("/<nickname>")
def get_player(nickname):
    return f"<p> Hello, {nickname}"

if __name__ == "__main__":
    app.run()
