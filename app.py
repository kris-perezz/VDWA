from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/final")
def final():
    return render_template("final.html")

@app.route("/yes")
def yes():
    return render_template("yes.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
