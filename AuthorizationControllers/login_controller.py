from Model.User import User
from flask import make_response, request, jsonify, Blueprint
from flask_jwt_extended import create_access_token
import bcrypt

login_controller = Blueprint("login_controller", __name__)


@login_controller.route("/login", methods=["POST"])
def login():
    content = request.json
    if content:
        username = content['username']
        password = content['password']
        if not username:
            return make_response("MISSING USERNAME", 401)
        if not password:
            return make_response("MISSING PASSWORD", 401)
        user_object = User.objects(username=username).first()
        if not user_object:
            return make_response("USER NOT FOUND", 404)
        if bcrypt.checkpw(password.encode('utf-8'), user_object.password.encode('utf-8')):
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)
        else:
            return make_response("BAD CREDENTIALS", 401)

