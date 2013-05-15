.. -*- mode: rst -*-

.. _services-other:

.. _Fedora: https://fedoraproject.org/
.. _OpenVPN: http://openvpn.net
.. _cups: http://www.cups.org
.. _ngircd: http://ngircd.barton.de/
.. _dropbear: https://matt.ucc.asn.au/dropbear/dropbear.html
.. _openssh: http://www.openssh.org/
.. _tftp: http://sourceforge.net/projects/tftp-server/

Other servers
=============

The Fedora Security Lab Test bench is hosting some services which are usualy
not found on public accessible systems. ``telnet`` was replaced with more secure
systems. Nowadays ``tftp`` is mainly used for provisioning VoIP installations.
Print servers like cups are used in office environments.

To give the students the possibility to work with VPN, an OpenVPN setup with
a static key is included.   

* `openssh`_ (Port 22) encrypts communication sessions over a computer network
  using the SSH protocol
* `dropbear`_ (Port 222) is a lightweight SSH server
* telnet (xinetd) supports  bidirectional interactive text-oriented communication 
* `tftp`_ (xinetd) is a single port TFTP Server based on Trivial File
Transfer Protocol
* `OpenVPN`_ server with a static key
* `cups`_ is a standards-based printing system
* `ngircd`_ is a lightweight Internet Relay Chat server

The tftp server is serving a simple text file. ::

    [fab@laptop011 hhs-tb]$ ls
    [fab@laptop011 hhs-tb]$ tftp 10.0.0.64
    tftp> get info.txt
    tftp> quit
    [fab@laptop011 hhs-tb]$ ls
    info.txt


