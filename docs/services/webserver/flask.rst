.. _services-webserver-flask:

.. _flask: http://flask.pocoo.org

flask
=====
`flask`_ is a lightweight Python web application framework. It's and based on
the Werkzeug WSGI toolkit and the Jinja2 template engine. This framework keeps
the core simple but additional feature can be added through extensions.

This example shows the details a HTTP GET request ::

    $ bannergrab 10.0.0.65 8886
    HTTP/1.0 200 OK
    Content-Type: text/html; charset=utf-8
    Content-Length: 43
    Server: Werkzeug/0.14.1 Python/3.7.7
    Date: Mon, 25 May 2020 11:19:56 GMT
