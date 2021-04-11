from flask_login import LoginManager

app = Flask (__name__)
login = LoginManager(app = app)
app.secret_key = "14#11125!"