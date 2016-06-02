# Postman
<h5><em>A Python library that delivers HTTP/HTTPS requests in a simple manner.</em></h5>
![alt tag](https://raw.githubusercontent.com/Omegabyte/Postman/master/Postman.jpeg)
# Library Usage
There are functions for major request methods:

`postman.post("mysite.com:80", mypost, myheaders")`

`postman.get("mysite.com:80", '/getfile.html', myheaders")`

`postman.head("mysite.com:80", '/')`

You can use the request function for less common methods:

`postman.request("mysite.com:80", "DELETE", '/deletefile.html', myheaders")`

You can do the same stuff as mentioned with HTTPS:

`postman.httpspost("mysite.com:80", mypost, myheaders")`

`postman.httpsget("mysite.com:80", '/getfile.html', myheaders")`

`postman.httpshead("mysite.com:80", '/')`

`postman.httpsrequest("mysite.com:80", "DELETE", '/deletefile.html', myheaders")`
