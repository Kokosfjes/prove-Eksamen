from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config["SECRET_KEY"] = "lotus-hemmelig"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"


# Brukermodell. Nye modeller (f.eks. for filer/saker) kan legges til her
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Offentlige sider
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")


# Innlogging
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        brukernavn = request.form["username"]
        passord = request.form["password"]
        bruker = User.query.filter_by(username=brukernavn).first()
        if bruker and bruker.password == passord:
            login_user(bruker)
            return redirect(url_for("demo"))
        flash("Feil brukernavn eller passord")
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


# Beskyttet side med HTML/CSS/JS-demo
@app.route("/demo")
@login_required
def demo():
    return render_template("demo.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
