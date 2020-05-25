.. _services-webserver-darkhttpd:

.. _darkhttpd: http://unix4lyfe.org/darkhttpd/

darkhttpd
=========
`darkhttpd`_ is a simple, fast HTTP 1.1 web server for static content. It
does not support PHP or CGI but is designed to serve static content.

This example shows the details of the `darkhttpd`_ web server. ::

    $ bannergrab 10.0.0.65 8887
    HTTP/1.1 200 OK
    Date: Mon, 25 May 2020 10:35:42 GMT
    Server: darkhttpd/1.12
    Accept-Ranges: bytes
    Connection: close
    Content-Length: 1352
    Content-Type: text/html; charset=UTF-8
