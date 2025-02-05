from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def intro():
    return render_template("intro.html")

@app.route("/main")
def main_prompt():
    return render_template("main.html")

@app.route("/yes")
def yes():
    return render_template("yes.html")

@app.route("/no")
def no():
    return render_template("no.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

