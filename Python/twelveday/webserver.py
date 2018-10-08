#Web Server Gateway interface
#localhost:8000/Francis     localhost:8000/Calvin
from wsgiref.simple_server import make_server

from webclient import application

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')

httpd.serve_forever()
