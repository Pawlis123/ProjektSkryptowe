from Model.User import User
from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

url_manager = Blueprint("url_manager", __name__)


@url_manager.route('/api/add-urls', methods=['POST'])
@jwt_required()
def add_url_endpoint():
    username = get_jwt_identity()
    user_object = User.objects(username=username).first()
    user_current_dict = user_object.rss_url_dict
    request_dict = request.json
    counter = 0

    for key in request_dict:
        if user_current_dict.get(key) is None:
            user_current_dict.update({key: request_dict.get(key)})
            counter += 1
    user_object.update(rss_url_dict=user_current_dict)

    if counter:
        return jsonify({"msg": "Successfully added new urls to a dict"}), 200
    else:
        return jsonify({"msg": "There was no unique urls"}), 200


@url_manager.route('/api/edit-urls', methods=['POST'])
@jwt_required()
def edit_urls():
    username = get_jwt_identity()
    user_object = User.objects(username=username).first()
    user_current_dict = user_object.rss_url_dict
    request_dict = request.json
    counter = 0

    for key in request_dict:
        if user_current_dict.get(key):
            user_current_dict.update({key: request_dict.get(key)})
            counter += 1
    user_object.update(rss_url_dict=user_current_dict)

    if counter:
        return jsonify({"msg": "Successfully edited urls to a dict"}), 200
    else:
        return jsonify({"msg": "There was no urls to edit"}), 200


@url_manager.route('/api/delete-url/<dict_key>', methods=['POST'])
@jwt_required()
def delete_url(dict_key: str):
    username = get_jwt_identity()
    user_object = User.objects(username=username).first()
    user_current_dict = user_object.rss_url_dict
    if user_current_dict.pop(dict_key):
        user_object.update(rss_url_dict=user_current_dict)
        return jsonify({"msg": "Successfully deleted url"}), 200
    else:
        return jsonify({"msg": "There was none url with such key"}), 200

