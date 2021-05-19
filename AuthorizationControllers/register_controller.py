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
            return make_response(jsonify(msg="MISSING USERNAME"), 401)
        if not password:
            return make_response(jsonify(msg="MISSING PASSWORD"), 401)

        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = User(username=username, password=password, rss_url_dict={})
        try:
            user.save()
        except:
            return make_response(jsonify(msg="USER WITH THAT USERNAME ALREADY EXISTS"), 403)
        return make_response(jsonify(msg="USER CREATED"), 201)
    else:
        return make_response(jsonify(msg="MISSING REQUEST BODY"), 401)
