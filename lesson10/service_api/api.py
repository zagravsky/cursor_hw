from flask import Blueprint, request
from flask.views import MethodView

from model import *

user_api = Blueprint('user_api', __name__, static_folder='../../static', template_folder='../../templates')


class UserView(MethodView):
    """
    CRUD User View
    """

    def get(self):
        user = User.query.order_by(User.id).all()
        return users_schema.jsonify(user)

    def post(self):
        data = request.get_json()
        new_user = User(**data)

        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user)

    def put(self, id):
        data = request.get_json()
        username = data.get("username")

        row = User.query.filter_by(id=id).first()
        row.username = username

        db.session.commit()
        return user_schema.jsonify(row)

    def delete(self, id):
        row = User.query.filter_by(id=id).first()

        db.session.delete(row)
        db.session.commit()
        return user_schema.jsonify(row)


user_api.add_url_rule('/user', view_func=UserView.as_view('user_api'))
user_api.add_url_rule('/user/<id>', view_func=UserView.as_view('user_change'))
