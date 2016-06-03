'''
Hello Github coders!
There's lots of cool things here you can tinker with, if you find a bug submit an issue.
If you manage to tinker something Awesome go to:
https://github.com/Omegabyte/Postman/
Then make your fork and start a pull request.
'''

try:
    import httplib, urllib, ssl
except ImportError:
    print('Using python 3, expect bugs!')
    import http.client, urllib.parse, ssl
    global py3
    py3 = True

# From http://stackoverflow.com/questions/14102416/python-requests-requests-exceptions-sslerror-errno-8-ssl-c504-eof-occurred
from functools import wraps
def sslwrap(func):
    @wraps(func)
    def bar(*args, **kw):
        kw['ssl_version'] = ssl.PROTOCOL_TLSv1
        return func(*args, **kw)
    return bar
ssl.wrap_socket = sslwrap(ssl.wrap_socket)

''' Demo Headers. '''
defaultall = {"Content-type": "*/*",
           "Accept": "*/*"}

if not py3:
    def request(url, method, getfile=None, headers=None, params=None):
    ''' Send a HTTP request. '''
    conn = httplib.HTTPConnection(url)
    conn.request(method, getfile, urllib.urlencode(params), headers)
    global response 
    response = list()
    response.append(conn.getresponse())
    conn.close()
else:
    def request(url, method, getfile=None, headers=None, params=None):
    ''' Send a HTTP request. '''
    conn = http.client.HTTPConnection(url)
    conn.request(method, getfile, urllib.parse.urlencode(params), headers)
    global response 
    response = list()
    response.append(conn.getresponse())
    conn.close()

if not py3:
    def httpsrequest(url, method, getfile=None, headers=None, params=None):
        ''' Send a HTTPS request. '''
    conn = httplib.HTTPSConnection(url)
    conn.request(method, getfile, urllib.urlencode(params), headers)
    global response 
    response = list()
    response.append(conn.getresponse())
    conn.close()
else:
    def httpsrequest(url, method, getfile=None, headers=None, params=None):
        ''' Send a HTTPS request. '''
    conn = http.client.HTTPSConnection(url)
    conn.request(method, getfile, urllib.parse.urlencode(params), headers)
    global response 
    response = list()
    response.append(conn.getresponse())
    conn.close()

def post(url, headers, params):
    ''' Send a HTTP POST request. '''
    request(url, 'POST', headers, params)

def get(url, headers, params):
    ''' Send a HTTP GET request. '''
    request(url, 'GET', headers, params)

def head(url, headers, params):
    ''' Send a HTTP HEAD request. '''
    request(url, 'HEAD')

def httpspost(url, headers, params):
    ''' Send a HTTPS POST request. '''
    httpsrequest(url, 'POST', headers, params)

def httpsget(url, headers, params):
    ''' Send a HTTPS GET request. '''
    httpsrequest(url, 'GET', headers, params)

def httpshead(url, headers, params):
    ''' Send a HTTPS HEAD request. '''
    httpsrequest(url, 'HEAD')

def responsestatus(num):
    ''' Return the response status of num, num being the request number. '''
    return response[num].status

def responsereason(num):
    ''' Return the response reason of num, num being the request number. '''
    return response[num].reason

def responsedata(num):
    ''' Return the response data of num, num being the request number. '''
    return response[num].read()

