.. -*- mode: rst -*-

.. _services-webserver-http-server:

.. _http-server: https://github.com/nodeapps/http-server

http-server (node.js)
=====================

The `http-server`_ functionality is used on top of `node.js`_.

The next example shows a connection the `http-server`_. ::

    $ nc 10.0.0.64 8888
    HEAD / HTTP/1.1
    host: localhost

    HTTP/1.1 200 OK
    server: ecstatic-0.1.7
    etag: "139483-944-Fri Apr 26 2013 19:09:31 GMT+0200 (CEST)"
    last-modified: Fri, 26 Apr 2013 17:09:31 GMT
    cache-control: max-age=3600
    content-type: text/html
    Date: Fri, 26 Apr 2013 21:24:51 GMT
    Connection: keep-alive
