.. -*- mode: rst -*-

.. _services-ftp:

.. _Fedora: https://fedoraproject.org
.. _lighttpd: http://www.lighttpd.net
.. _apache: http://httpd.apache.org
.. _cherokee: http://cherokee-project.com
.. _nginx: http://nginx.org/
.. _tomcat: http://tomcat.apache.org/index.html
.. _droopy: http://gitorious.org/droopy
.. _pywebserve: http://gitorious.org/pywebserve
.. _http-server: https://github.com/nodeapps/http-server
.. _mongoose: http://code.google.com/p/mongoose/

Web servers
===========

Every type of web server has its purpose and its unique fingerprint. To give
the students the feeling of the real world, various web servers are running.
They don’t serve content, they are just lurking around for fingerprinting and
bannergrabbing. The following web server are available.

* `lighttpd`_
* `apache`_ (not ready)
* `cherokee`_ (not ready)
* `nginx`_
* `tomcat`_
* `droopy`_
* `pywebserve`_
* `http-server`_ node.js
* `mongoose`_

To run all web servers on one machine it's needed that they use different
ports. Table below shows the ports and the assigned web server.

+------------+----------------+
| Port       | Server         |
+============+================+
| 80         | lighttpd       |
+------------+----------------+
| 8000       | droopy         |
+------------+----------------+
| 8008       | cherokee       |
+------------+----------------+
| 8080       | tomcat         |
+------------+----------------+
| 8800       | apache         |
+------------+----------------+
| 8808       | nginx          |
+------------+----------------+
| 8880       | pywebserve     |
+------------+----------------+
| 8888       | http-server    |
+------------+----------------+
| 8889       | mongoose       |
+------------+----------------+

At the moment the most web servers doesn't support https. This is a task for
the future. The only web server with SSL support is `nginx`_. ::

    $ nc 10.0.0.64 8080
    HEAD / HTTP/1.1
    host: localhost

    HTTP/1.1 200 OK
    Server: Apache-Coyote/1.1
    Accept-Ranges: bytes
    ETag: W/"7777-1342949470000"
    Last-Modified: Sun, 22 Jul 2012 09:31:10 GMT
    Content-Type: text/html
    Content-Length: 7777
    Date: Fri, 26 Apr 2013 21:20:57 GMT

A connection to `nginx`_ over SSL. ::

    $ openssl s_client -crlf -connect 10.0.0.64:443
    CONNECTED(00000003)
    depth=0 C = CH, ST = BE, L = Berne, O = Test bench, CN = test-bench.localdomain
    verify error:num=18:self signed certificate
    verify return:1
    depth=0 C = CH, ST = BE, L = Berne, O = Test bench, CN = test-bench.localdomain
    verify return:1
    ---
    Certificate chain
     0 s:/C=CH/ST=BE/L=Berne/O=Test bench/CN=test-bench.localdomain
       i:/C=CH/ST=BE/L=Berne/O=Test bench/CN=test-bench.localdomain
    ---
    Server certificate
    -----BEGIN CERTIFICATE-----
    [snip]
    -----END CERTIFICATE-----
    subject=/C=CH/ST=BE/L=Berne/O=Test bench/CN=test-bench.localdomain
    issuer=/C=CH/ST=BE/L=Berne/O=Test bench/CN=test-bench.localdomain
    ---
    No client certificate CA names sent
    ---
    SSL handshake has read 1770 bytes and written 369 bytes
    ---
    New, TLSv1/SSLv3, Cipher is DHE-RSA-AES256-SHA
    Server public key is 2048 bit
    Secure Renegotiation IS supported
    Compression: NONE
    Expansion: NONE
    SSL-Session:
        Protocol  : TLSv1
        Cipher    : DHE-RSA-AES256-SHA
        Session-ID: 33515B817[snip]427BB415
        Session-ID-ctx: 
        Master-Key: 0956B7B[snip]F729586
        Key-Arg   : None
        Krb5 Principal: None
        PSK identity: None
        PSK identity hint: None
        TLS session ticket lifetime hint: 300 (seconds)
        TLS session ticket:
        [snip]
        Start Time: 1367011380
        Timeout   : 300 (sec)
        Verify return code: 18 (self signed certificate)
    ---
    HEAD / HTTP/1.1
    host: localhost

    HTTP/1.1 200 OK
    Server: nginx/1.2.8
    Date: Fri, 26 Apr 2013 21:23:16 GMT
    Content-Type: text/html
    Content-Length: 944
    Last-Modified: Fri, 26 Apr 2013 17:01:48 GMT
    Connection: keep-alive
    Accept-Ranges: bytes

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

