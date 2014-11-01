.. _services-webserver-lighttpd:

.. _lighttpd: http://www.lighttpd.net

lighttpd
========
This is the server which is providing the web interface. `lighttpd`_ is
optimized for speed while still standards-compliant, secure and flexible.

This example shows the details of the `lighttpd`_ web server. ::

    $ bannergrab 10.0.0.64 80
    HTTP/1.0 200 OK
    Allow: OPTIONS, GET, HEAD, POST
    Content-Length: 0
    Connection: close
    Date: Sat, 01 Nov 2014 13:18:35 GMT
    Server: lighttpd/1.4.35
