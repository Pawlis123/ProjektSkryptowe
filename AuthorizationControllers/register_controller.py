from Model.User import User
from flask import make_response, request, Blueprint, jsonify
import bcrypt


register_controller = Blueprint("register_controller", __name__)


@register_controller.route('/api/register', methods=['POST'])
def register_endpoint():
    content = request.json
    if content:
        username = content['username']
        password = content['password']
        if not username:
            return make_response(jsonify(msg="MISSING USERNAME"), 400)
        if not password:
            return make_response(jsonify(msg="MISSING PASSWORD"), 400)
        if len(password) < 6:
            return make_response(jsonify(msg="Password should be at leas 6 character long"), 400)

        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = User(username=username, password=password, rss_url_dict={})
        try:
            user.save()
        except:
            return make_response(jsonify(msg="User with that username already exists"), 403)
        return make_response(jsonify(msg="Account has been created"), 201)
    else:
        return make_response(jsonify(msg="MISSING REQUEST BODY"), 401)
