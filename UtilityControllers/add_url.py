from Model.User import User
from flask import make_response, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

add_url = Blueprint("add_url", __name__)


@add_url.route('/api/add-url', methods=['POST'])
@jwt_required()
def add_url_endpoint():
    username = get_jwt_identity()
    user_object = User.objects(username=username).first()
    content = request.json
    url_list = content['new_urls']
    current_url_list = user_object.rss_url_list
    for url in url_list:
        if url not in current_url_list:
            current_url_list.append(url)
    user_object.update(rss_url_list=current_url_list)
    return make_response("OK", 200)
