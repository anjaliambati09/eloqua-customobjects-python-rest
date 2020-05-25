import base64
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse

class EloquaRequest(urllib.request.Request):
    headers = ''
    base_url = 'https://secure.p01.eloqua.com/api/REST/2.0/'

    def __init__(self, site, user, password):
        authKey = base64.b64encode(bytes(site + "\\" + user + ":" + password, 'utf-8')).decode('ascii')
        self.headers = {"Content-Type":"application/json", "Authorization":"Basic " + authKey}

    def get(self, url, data):
        return self.request('GET', url, data)

    def post(self, url, data):
        return self.request('POST', url, data)

    def put(self, url, data):
        return self.request('PUT', url, data)

    def delete(self, url, data):
        return self.request('DELETE', url, data)

    def request(self, method, url, data):
        request_object = urllib.request.Request(self.base_url + url)
        request_object.get_method = lambda: method

        for key,value in list(self.headers.items()):
          request_object.add_header(key,value)

        if data != None:
          data = urllib.parse.urlencode(data)

        response = urllib.request.urlopen(request_object, data)
        return response.read()
