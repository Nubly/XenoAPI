from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mariadb+mariadbconnector://root:UruguayFreakingSucksLol420@127.0.0.1:3306/hydro"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
