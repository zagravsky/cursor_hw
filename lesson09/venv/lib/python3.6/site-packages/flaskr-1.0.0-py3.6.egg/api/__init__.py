from flask import Blueprint, render_template
from flask.views import MethodView


class ApiView(MethodView):
    def get(self):
        return render_template("login.html")


api = Blueprint('api', __name__, static_folder='./static', template_folder='./template')

api.add_url_rule('/api', view_func=ApiView.as_view('api'))


