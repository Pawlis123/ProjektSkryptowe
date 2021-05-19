from Model.User import User
from flask import Blueprint, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
import Utils.ArticlesFetching as af

get_articles = Blueprint("get_articles", __name__)


@get_articles.route("/api/articles", methods=['GET'])
@jwt_required()
def get_all_articles():
    username = get_jwt_identity()
    user_object = User.objects(username=username).first()
    user_current_dict = user_object.rss_url_dict
    if len(user_current_dict) == 0:
        return make_response(jsonify(msg="NO RSS ADDRESSES"), 400)
    dict_to_serialize = af.fetch_articles(user_current_dict)
    return make_response(jsonify(dict_to_serialize), 200)
