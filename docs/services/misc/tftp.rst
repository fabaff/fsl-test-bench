.. _tftp: http://sourceforge.net/projects/tftp-server/

.. _services-misc-tftp:

tftp
====
`tftp`_ (xinetd) is a single port Trivial File Transfer Protocol server

The tftp server is serving a simple text file. ::

    $ ls
    $ tftp 10.0.0.64
    tftp> get info.txt
    tftp> quit
    $ ls
    info.txt

