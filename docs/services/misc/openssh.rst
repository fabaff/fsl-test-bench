.. -*- mode: rst -*-

.. _services-misc-openssh:

.. _openssh: http://www.openssh.org/
.. _nmap: http://nmap.org/

openssh
=======

`openssh`_ (Port 22) encrypts communication sessions over a computer network
using the SSH protocol. 

Banner grabbing with ``netcat`` will give you the version back::

    $ nc -v 10.0.0.65 22
    Ncat: Version 6.25 ( http://nmap.org/ncat )
    Ncat: Connected to 10.0.0.65:22.
    SSH-2.0-OpenSSH_6.1

There are two other ways to retrieve the version with `nmap`_. The first is ::

    $ nmap -sV -p 22 10.0.0.65
    [...]
    Host is up (0.00053s latency).
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 6.1 (protocol 2.0)

The second is ::

    $ nmap -sV -p 22 --script=banner 10.0.0.65
    [...]
    Host is up (0.00061s latency).
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 6.1 (protocol 2.0)
    |_banner: SSH-2.0-OpenSSH_6.1
