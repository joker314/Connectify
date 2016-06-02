import httplib, urllib, ssl

# From http://stackoverflow.com/questions/14102416/python-requests-requests-exceptions-sslerror-errno-8-ssl-c504-eof-occurred
from functools import wraps
def sslwrap(func):
    @wraps(func)
    def bar(*args, **kw):
        kw['ssl_version'] = ssl.PROTOCOL_TLSv1
        return func(*args, **kw)
    return bar
ssl.wrap_socket = sslwrap(ssl.wrap_socket)

defaultall = {"Content-type": "*/*",
           "Accept": "*/*"}

def request(url, method, getfile=None, headers=None, params=None):
    ''' Send a HTTP request. '''
    conn = httplib.HTTPConnection(url)
    conn.request(method, getfile, params, headers)
    global response 
    response = list()
    response.append(conn.getresponse())
    conn.close()

def httpsrequest(url, method, getfile=None, headers=None, params=None):
    ''' Send a HTTPS request. '''
    conn = httplib.HTTPSConnection(url)
    conn.request(method, getfile, params, headers)
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
    httpsrequest(url, 'POST', headers, params)

def httpsget(url, headers, params):
    httpsrequest(url, 'GET', headers, params)

def httpshead(url, headers, params):
    httpsrequest(url, 'HEAD')

def responsestatus(num):
    return response[num].status

def responsereason(num):
    return response[num].reason

def responsedata(num):
    return response[num].read()

