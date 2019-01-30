from flask import Blueprint
from flask.views import MethodView

from flask import current_app


class FabrikApiView(MethodView):
    def get(self):
        return current_app.config.get("TEST_VARIABLE")


factory_api = Blueprint('factory_api', __name__, static_folder='./static', template_folder='./template')

factory_api.add_url_rule('/factory', view_func=FabrikApiView.as_view('factory_api'))
