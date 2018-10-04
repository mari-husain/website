from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

bp = Blueprint('main', __name__,
                        template_folder='templates')

def show(page):
    try:
    	return render_template('main/%s' % page)
    except TemplateNotFound:
        abort(404)
        
@bp.route('/')
def index():
	return show('index.html')
	
@bp.route('/resume')
def resume():
	return show('resume.html')