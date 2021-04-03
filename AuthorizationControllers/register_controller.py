from Model.User import User
from flask import make_response, request, Blueprint
import bcrypt

register_controller = Blueprint("register_controller", __name__)


@register_controller.route('/register', methods=['POST'])
def register_endpoint():
    content = request.json
    if content:
        username = content['username']
        password = content['password']
        if not username:
            return make_response("MISSING USERNAME", 401)
        if not password:
            return make_response("MISSING PASSWORD", 401)

        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = User(username=username, password=password)
        try:
            user.save()
        except:
            return make_response("NON UNIQUE USERNAME VALUE", 403)
        return make_response("", 201)
    else:
        return make_response("Missing informations", 401)
