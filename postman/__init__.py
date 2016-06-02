'''
Hello Github coders!
There's lots of cool things here you can tinker with, if you find a bug submit an issue.
If you manage to tinker something Awesome go to:
https://github.com/Omegabyte/Postman/
Then make your fork and start a pull request.
'''

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

