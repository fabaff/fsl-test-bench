.. _nginx: http://nginx.org/

.. _services-webserver-nginx:

nginx
=====
`nginx`_ [engine x] is an HTTP and reverse proxy server, as well as a mail
proxy server. Thanks to accelerated reverse proxying with caching, nginx is 
able to provide simple load balancing and fault tolerance. 

`nginx`_ is the only web server with SSL support. ::

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
