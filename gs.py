from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days=5)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        # make dictionary key
        session["user"] = user
        flash("login successful")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user")
def user():
    if  "user" in session:
        user = session['user']
        return render_template("user.html", user=user)
    else:
        flash("not logged in")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    # if  "user" in session:
    #     user = session['user']
        flash("you have logged out", "info")
    # else:
        session.pop("user", None)
        return redirect(url_for("login"))

# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}"

# @app.route("/admin")
# def admin():
#     # redirect to name of function, to redirect with parameter
#     # ("user", name="goes_here")
#     return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)