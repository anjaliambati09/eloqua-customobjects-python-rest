import sys
sys.path.append('./lib')
from eloqua_request import EloquaRequest

request = EloquaRequest('site', 'user', 'password')
response = request.get('/data/customObject/{id}', None)
