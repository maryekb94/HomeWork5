from pyramid.response import Response

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError



@view_config(route_name='index', renderer='templates/index.jinja2')
def index(request):
    return {'link': u'<a href="about/aboutme.html">About me</a>'}


@view_config(route_name='about', renderer='templates/about/aboutme.jinja2')
def about(request):
    return {'link': u'<a href="/">Index</a>'}

