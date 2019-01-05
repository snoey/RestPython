from flask import Blueprint
from flask import render_template
from flask_restful import Api
from resources.RegistrationDriver import RegistrationDriverResource
from resources.DailyOrderDriver import DailyOrderDriverResource

api_bp = Blueprint( '',__name__, template_folder="templates")
api = Api(api_bp)

# Route
@api_bp.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

api.add_resource(RegistrationDriverResource, 'RegistrationDriver')
api.add_resource(DailyOrderDriverResource, 'DailyOrderDriver')