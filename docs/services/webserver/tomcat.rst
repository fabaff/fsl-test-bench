.. _services-webserver-tomcat:

.. _Tomcat: http://tomcat.apache.org/index.html

tomcat
======
Apache `Tomcat`_ is an open source software implementation of the Java Servlet
and JavaServer Pages technologies. This server is listening on port 8080. At 
the moment there are no pages served from this server.

.. _tomcat-fig:
.. figure:: ../../images/tomcat.png
    :align: center
    
    Tomcat admin web interface

This example shows the details of the `Tomcat`_ web server. ::

    $ bannergrab 10.0.0.64 8080
    HTTP/1.1 200 OK
    Server: Apache-Coyote/1.1
    Content-Type: text/html;charset=ISO-8859-1
    Date: Sat, 01 Nov 2014 13:17:27 GMT
    Connection: close

