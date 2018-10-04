from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

bp = Blueprint('colors', __name__,
                        template_folder='templates',
                        url_prefix='/colors')

def show(page):
    try:
    	return render_template('colors/%s' % page)
    except TemplateNotFound:
        abort(404)
        
@bp.route('/')
def index():
	return show('colors.html')