.. _services-webserver-mongoose:

.. _mongoose: http://code.google.com/p/mongoose/

mongoose
========
`mongoose`_ is built on top of libmongoose embedded library. Libmongoose is 
used to serve Web GUI on embedded devices, implement RESTful services, RPC
frameworks (e.g. JSON-RPC), handle telemetry data exchange, and perform many
other tasks in various different industries. 

This example shows the details of the `mongoose`_ web server. ::

    $ bannergrab 10.0.0.65 8889
    HTTP/1.1 200 OK
    Date: Wed, 29 May 2013 15:24:20 GMT
    Last-Modified: Wed, 29 May 2013 14:44:55 GMT
    Etag: "51a61467.3b0"
    Content-Type: text/html
    Content-Length: 944
    Connection: close
    Accept-Ranges: bytes

