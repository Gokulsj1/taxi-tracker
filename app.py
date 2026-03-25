from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    from flask import request

    if "db.gokulsj.shop" in request.host:
        return render_template("dashboard.html")

    return render_template("index.html")

@app.route("/history")
def history():
    return render_template("history.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
