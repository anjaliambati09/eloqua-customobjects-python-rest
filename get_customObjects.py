import sys
import json
sys.path.append('./lib')
from eloqua_request import EloquaRequest

request = EloquaRequest('site', 'user', 'password')
response = request.get('/assets/customObjects', None)
#print(response)
JSON_object = json.loads(response.decode('utf-8'))
print(JSON_object)
