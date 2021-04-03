from flask import Flask
from Model import db
# from flask_jwt_extended import create_access_token
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from AuthorizationContollers import login_controller, register_controller

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

# class Book(db.Document):
#     book_id = db.IntField()
#     title = db.StringField()
#     author = db.StringField()
#
#     def to_json(self):
#         return {
#             "book_id": self.book_id,
#             "title": self.title,
#             "author": self.author
#         }
#
#
# @app.route('/api/db_populate', methods=['POST'])
# def db_populate():
#     book1 = Book(book_id=1, title="Game of Thrones", author="Martin")
#     book2 = Book(book_id=2, title="testXD", author="MartinXD")
#     book1.save()
#     book2.save()
#     return make_response("", 200)
#
#
# @app.route('/api/books', methods=['GET', 'POST'])
# def api_books():
#     if request.method == "GET":
#         books = []
#         for book in Book.objects:
#             books.append(book)
#         return make_response(jsonify(books), 200)
#
#     elif request.method == "POST":
#         content = request.json
#         book = Book(book_id=content['book_id'], title=content['title'], author=content['author'])
#         book.save()
#         return make_response("", 201)
#
#
# @app.route('/api/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
# def api_each_book(book_id):
#     if request.method == "GET":
#         pass
#     elif request.method == "POST":
#         pass
