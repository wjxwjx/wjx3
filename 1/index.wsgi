import sae
from classroom import wsgi
application = sae.create_wsgi_app(wsgi.application)