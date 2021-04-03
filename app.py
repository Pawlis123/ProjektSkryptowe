from flask import Flask
from Model import db
# from flask_jwt_extended import create_access_token
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from AuthorizationControllers import login_controller, register_controller

mongodb_password = "wknpiwgm"

database_name = "Skryptowe"
DB_URI = "mongodb+srv://mainUser:{}@cluster0.wiakf.mongodb.net/{}?retryWrites=true&w=majority".format(mongodb_password, database_name)
app = Flask(__name__)
app.config["MONGODB_HOST"] = DB_URI
app.config["JWT_SECRET_KEY"] = "ultrasecretkey"
db.init_app(app)
jwt = JWTManager(app)
app.register_blueprint(login_controller.login_controller)
app.register_blueprint(register_controller.register_controller)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)


