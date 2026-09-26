import os

from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import URL

app = Flask(__name__)

app.secret_key = os.getenv(
    "SECRET_KEY",
    "report-analytics-dev-secret"
)

connection_url = URL.create(
    "mysql+pymysql",
    username=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    database=os.getenv("MYSQL_DB")
)

app.config["SQLALCHEMY_DATABASE_URI"] = connection_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)



class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Report(db.Model):
    __tablename__ = "reports"

    id = db.Column(db.Integer, primary_key=True)
    report_name = db.Column(db.String(150), nullable=False)
    report_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
@app.route("/")
def home():
    return "Report Generation & Analytics Project"


@app.route("/test-db")
def test_db():
    try:
        db.session.execute(db.text("SELECT 1"))
        return "MySQL Database Connected Successfully!"
    except Exception as e:
        return f"Database Error: {e}"
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        new_user = User(
            username=username,
            email=email,
            password=password
        )

        db.session.add(new_user)
        db.session.commit()

        return "Registration Successful!"

    return render_template("register.html")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(
            email=email,
            password=password
        ).first()

        if user:
            session["user_id"] = user.id
            session["username"] = user.username

            return redirect(url_for("dashboard"))

        return "Invalid email or password!"

    return render_template("login.html")
@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    total_reports = Report.query.count()

    sales_reports = Report.query.filter_by(
        report_type="Sales Report"
    ).count()

    employee_reports = Report.query.filter_by(
        report_type="Employee Report"
    ).count()

    analytics_reports = Report.query.filter_by(
        report_type="Analytics Report"
    ).count()

    return render_template(
        "dashboard.html",
        username=session["username"],
        total_reports=total_reports,
        sales_reports=sales_reports,
        employee_reports=employee_reports,
        analytics_reports=analytics_reports
    )
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))
@app.route("/report", methods=["GET", "POST"])
def report():
    if request.method == "POST":

        report_name = request.form["report_name"]
        report_type = request.form["report_type"]
        description = request.form["description"]

        new_report = Report(
            report_name=report_name,
            report_type=report_type,
            description=description
        )

        db.session.add(new_report)
        db.session.commit()

        return render_template(
            "report_success.html",
             report_name=report_name,
             report_type=report_type,
             description=description
        )

       

    return render_template("report.html")
@app.route("/analytics")
def analytics():

    sales_count = Report.query.filter_by(
        report_type="Sales Report"
    ).count()

    employee_count = Report.query.filter_by(
        report_type="Employee Report"
    ).count()

    analytics_count = Report.query.filter_by(
        report_type="Analytics Report"
    ).count()

    finance_count = Report.query.filter_by(
        report_type="Finance Report"
    ).count()

    return render_template(
        "analytics.html",
        sales_count=sales_count,
        employee_count=employee_count,
        analytics_count=analytics_count,
        finance_count=finance_count
    )

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)