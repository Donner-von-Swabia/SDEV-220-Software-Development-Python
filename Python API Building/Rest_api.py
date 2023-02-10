from flask import Flask
from flask_restful import Api, Resource, reqparse,abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class BooksModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)


#db.create_all()


books_put_arges = reqparse.RequestParser()
books_put_arges.add_argument('book_name', type=str, help="Name of the book", required=True)
books_put_arges.add_argument("author", type=str,help="Author of book", required=True)
books_put_arges.add_argument("publisher",type=str,help="Publisher of book", required=True)

book_update_arges = reqparse.RequestParser()
book_update_arges.add_argument('book_name', type=str, help="Name of the book")
book_update_arges.add_argument("author", type=str,help="Author of book")
book_update_arges.add_argument("publisher",type=str,help="Publisher of book")


resource_fields = {
    'id' : fields.Integer,
    'book_name' : fields.String,
    'author' : fields.String,
    'publisher': fields.String
}


class books(Resource):
    @marshal_with(resource_fields)
    def get(self, id):
        result = BooksModel.query.filter_by(id=id).first()
        if not result:
            abort(404, message='No video with id')
        return result
        
    @marshal_with(resource_fields)
    def put(self,id):
        args = books_put_arges.parse_args()
        result = BooksModel.query.filter_by(id=id).first()
        if result:
            abort(409, message="Video ID Taken")
        book = BooksModel(id=id,book_name=args['book_name'],author=args['author'],publisher=args['publisher'])
        db.session.add(book)
        db.session.commit()
        return book, 201
    @marshal_with(resource_fields)
    def patch(self,id):
        args = book_update_arges.parse_args()
        result = BooksModel.query.filter_by(id=id).first()
        if not result:
            abort(404, message='No video with id')
        
        if args['book_name']:
            result.book_name = args['book_name']
        if args['author']:
            result.book_name = args['author']
        if args['publisher']:
            result.book_name = args['publisher']
        db.session.commit()
        return result



    def delete(self,id):
        result = BooksModel.query.filter_by(id=id).first()
        if not result:
            abort(404, message='No video with id')
        db.session.delete(result)
        db.session.commit()
        return 202

api.add_resource(books, '/<int:id>')

if __name__ == "__main__":
    app.run(debug=True)