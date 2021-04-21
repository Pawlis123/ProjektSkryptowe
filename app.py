from flask import Flask
from Model import db
from flask_jwt_extended import JWTManager
from AuthorizationControllers import login_controller, register_controller
import datetime
from UtilityControllers import url_manager, get_articles


mongodb_password = "wknpiwgm"

database_name = "Skryptowe"
DB_URI = "mongodb+srv://mainUser:{}@cluster0.wiakf.mongodb.net/{}?retryWrites=true&w=majority".format(mongodb_password,
                                                                                                      database_name)
app = Flask(__name__)
app.config["MONGODB_HOST"] = DB_URI
app.config["JWT_SECRET_KEY"] = "ultrasecretkey"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(hours=24)
db.init_app(app)
jwt = JWTManager(app)
app.register_blueprint(login_controller.login_controller)
app.register_blueprint(register_controller.register_controller)
app.register_blueprint(url_manager.url_manager)
app.register_blueprint(get_articles.get_articles)

if __name__ == '__main__':
    app.run(debug=True)
