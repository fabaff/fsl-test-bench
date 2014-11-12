.. _dropbear: https://matt.ucc.asn.au/dropbear/dropbear.html
.. _nmap: http://nmap.org/

.. _services-misc-dropbear:

dropbear
========
`dropbear`_ which is running on port 222 is a lightweight SSH server.

To retrieve the version with `nmap`_, use the command mentioned below::

    $ nmap -sV -p 222 --script=banner 10.0.0.65
    [...]
    Host is up (0.00045s latency).
    PORT    STATE SERVICE VERSION
    222/tcp open  ssh     Dropbear sshd 2012.55 (protocol 2.0)
    |_banner: SSH-2.0-dropbear_2012.55
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Banner grabbing with ``netcat`` will give you the version back.::

    $ nc -v 10.0.0.65 222
    Ncat: Version 6.25 ( http://nmap.org/ncat )
    Ncat: Connected to 10.0.0.65:222.
    SSH-2.0-dropbear_2012.55
