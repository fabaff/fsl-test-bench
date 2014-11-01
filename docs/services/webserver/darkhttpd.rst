.. _services-webserver-darkhttpd:

.. _darkhttpd: http://unix4lyfe.org/darkhttpd/

darkhttpd
=========
`darkhttpd`_ is a simple, fast HTTP 1.1 web server for static content. It
does not support PHP or CGI etc but is designed to serve static content.

This example shows the details of the `darkhttpd`_ web server. ::

    $ bannergrab 10.0.0.65 8887
    HTTP/1.1 200 OK
    Date: Wed, 29 May 2013 15:24:20 GMT
    Last-Modified: Wed, 29 May 2013 14:44:55 GMT
    Etag: "51a61467.3b0"
    Content-Type: text/html
    Content-Length: 944
    Connection: close
    Accept-Ranges: bytes

