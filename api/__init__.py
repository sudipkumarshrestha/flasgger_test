from flask import Flask
from api.signup.route import signup
from flasgger import Swagger

# from flasgger import LazyString, LazyJSONEncoder


app = Flask(__name__)


app.config['SWAGGER'] = {
    'title': 'My API',
    'uiversion': 3,
    'openapi': '3.0.2',
    'specs_route': '/swagger/',
    'specs_url': '/swagger/apispec_1.json',
}
swagger = Swagger(app)
def create_app():
    app.register_blueprint(signup)

    return app

