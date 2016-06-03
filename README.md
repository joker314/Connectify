# Connectify
<h5><em>A Python library that delivers HTTP/HTTPS requests in a simple manner.</em></h5>
![Connectify Logo](https://raw.githubusercontent.com/Omegabyte/Connectify/master/connectify/logo.jpeg)

# Install
Install with `pip install connectify`

# Library Usage
There are functions for major request methods:

`connectify.post("mysite.com:80", mypost, myheaders")`

`connectify.get("mysite.com:80", '/getfile.html', myheaders")`

`connectify.head("mysite.com:80", '/')`

You can use the request function for less common methods:

`connectify.request("mysite.com:80", "DELETE", '/deletefile.html', myheaders")`

You can do the same stuff as mentioned with HTTPS:

`connectify.httpspost("mysite.com:80", mypost, myheaders")`

`connectify.httpsget("mysite.com:80", '/getfile.html', myheaders")`

`connectify.httpshead("mysite.com:80", '/')`

`connectify.httpsrequest("mysite.com:80", "DELETE", '/deletefile.html', myheaders")`

Handing responses is just as easy, you get response via response number (Response number starts at 0):

`connectify.httpget("mysite.com:80", '/getfile.html', myheaders")`

`print(connectify.responsestatus(0))`

`print(connectify.responsereason(0))`

`print(connectify.responsedata(0))`

# I want to Help!
Make your fork and start a pull request, I'll check it for errors and then merge it.
If you regularly make commits I'll add you as collaborator.

# Collaborator Rules
* Only push directly to master if there is an urgent bugfix.
* Ask for a second opinion before merging a pull request.
* Don't make issues to propose a new release, ask first in the general discussion.
* Add useful comments to code if confusing or complicated.
* Credit sources eg. `StackOverflow`

# I've got a question!
Please don't open an issue to ask a question, ask in the general discussion.
