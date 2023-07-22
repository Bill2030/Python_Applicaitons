from flask import Flask, render_template, url_for, redirect, request



app = Flask(__name__)

@app.route('/success')
def success():
   return render_template("success.html")


@app.route('/', methods= ["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"],
        password = request.form["password"]
        return redirect(url_for("success"))
    return render_template("login.html")

if __name__ =="__main__":
    app.run(debug=True, host="127.0.0.1", port=5002)



