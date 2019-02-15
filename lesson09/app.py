from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, make_response, url_for
from datetime import timedelta
import os

from werkzeug.utils import secure_filename

from api import api

app = Flask(__name__)

app.register_blueprint(api)


dict_info_about = {"Nick": "Age: 31, Favourite drink: kola",
                   "Jack": "Age 22, Favourite drink: coffee"}


dict_cars = {
    "Tiguan": {"Year": 2012, "Miles": 87000, "Price": 10200},
    "Accord": {"Year": 2010, "Miles": 126000, "Price": 8000},
    "CC": {"Year": 2010, "Miles": 109000, "Price": 8600}
}

data = {
    "news": {
        "New elections coming",
        "Used car gets cheaper"
    }
}

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)


@app.route("/")
@app.route("/home")
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template("home.html", data=data, dict_cars=dict_cars)


@app.route('/login', methods=['POST'])
def login():
    if request.form['password'] == 'admin' and request.form['username'] == 'admin':
        session['logged_in'] = True
        session['username'] = request.form['username']
    else:
        flash('wrong password!')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


@app.route("/about")
def about():
    return "<h1>About Page</h1>"


@app.route("/cars/")
def get_all():
    result = ""
    for key, value in dict_cars.items():
        result = result + key + " " + str(value) + "\n"

    return result


@app.route("/cars/<path:name>/")
def get_item(name):
    if name in dict_cars.keys():
        return dict_cars.get(name).value
    return name


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return 'Subpath %s' % subpath


@app.route("/products")
def products():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template("products.html", data=data, dict_cars=dict_cars)


@app.route("/month/<int:number>")
def return_month_name(number):
    month = name_of_the_month(number)
    return render_template("month.html", month=month)


def name_of_the_month(number):
    """
    Returns the month according to the number
    :param number: int
    :return:
    """
    months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December")
    return months[number - 1]


test_methods_dict = ["Value 1", "Value 2"]


@app.route('/test_methods')
@app.route('/test_methods/<string:value>', methods=['GET', 'POST', 'DELETE'])
def test_methods(value=None):
    if request.method == 'POST':
        do_post(value)
        return "Successfully added a new value"
    if request.method == 'DELETE':
        do_delete(value)
        return "Successfully deleted the value"
    else:
        return do_get()


def do_post(value):
    """
    This method will add value to the test_methods_dict
    :return:
    """
    return test_methods_dict.append(value)


def do_get():
    """
    Returns template with all test_methods_dict values
    :return:
    """
    return render_template('test_methods.html', values=test_methods_dict, name="a")


def do_delete(value):
    """
    Delete values from test_methods_dict
    :param value:
    :return:
    """
    for i, elem in enumerate(test_methods_dict):
        if elem == value:
            test_methods_dict.pop(i)


from flask.views import MethodView

request_object_data = {"Key 1": "Value 1",
                       "Key 2": "Value 2"}


# http://werkzeug.pocoo.org/docs/0.14/wrappers/


class RequestObject(MethodView):
    def get(self):
        client_name = request.headers.get("client_name")
        args = request.args
        base_url = request.base_url

        response = dict()
        response["client_name"] = client_name
        response["args"] = args
        response["base_url"] = base_url

        return jsonify(response)

    def post(self):
        data = request.data
        return data


app.add_url_rule('/request_object', view_func=RequestObject.as_view('request_object'))


class FileUpload(MethodView):
    def post(self):
        f = request.files['file']
        f.save(f"{secure_filename(f.filename)}")
        return "success"


app.add_url_rule('/file_upload', view_func=FileUpload.as_view('file_upload'))

from functools import wraps
from flask import g, request, redirect, url_for


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)

    return decorated_function


from datetime import timedelta
from flask import session


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)


db = {
    "news": ["elem", "elem_2", "elem_3"]
}


@app.route('/homework_home')
def home_page():
    return render_template('home.html', data=db)


@app.route('/get_cookie')
def get_cookie():
    return jsonify(request.cookies)


@app.route('/set_cookie')
def set_cookie():
    response = make_response()
    response.set_cookie("email", "...@gmail.com")  # not more then one value
    return response


@app.route("/test_abort")
def test_redirect():
    abort(501, "Value error")
    return redirect(url_for("home"))


@app.errorhandler(501)
def error_501_handler(error):
    return render_template("error_501.html")

@app.errorhandler(404)
def error_404_handler(error):
    return render_template("error_404.html")

app.secret_key = b'"\xaa;\x0b\x12\x8a\xa1V+\x16\xc5\x91\xfb,\xcb#'


@app.route("/test_session")
def test_session():
    app.logger.warning("this is warning")
    app.logger.error("This is error")
    session["key"] = "value"
    return "hello"


if __name__ == '__main__':
    app.run(debug=True)
