.. -*- mode: rst -*-

.. _services-others:

.. _Fedora: https://fedoraproject.org/
.. _OpenVPN: http://openvpn.net
.. _cups: http://www.cups.org
.. _ngircd: http://ngircd.barton.de/
.. _dropbear: https://matt.ucc.asn.au/dropbear/dropbear.html
.. _openssh: http://www.openssh.org/
.. _xrdp: http://www.xrdp.org/
.. _ntp: http://www.ntp.org/

Other servers/services
======================

The Fedora Security Lab Test bench is hosting some services which are usualy
not found on public accessible systems. ``telnet`` was replaced with more secure
systems. Nowadays ``tftp`` is mainly used for provisioning VoIP installations.
Print servers like cups are used in office environments.

To give the students the possibility to work with VPN, an OpenVPN setup with
a static key is included.   

* `openssh`_ (Port 22) encrypts communication sessions over a computer network
  using the SSH protocol
* `dropbear`_ (Port 222) is a lightweight SSH server
* `OpenVPN`_ server with a static key
* `cups`_ is a standards-based printing system
* `ngircd`_ is a lightweight Internet Relay Chat server
* `xrdp`_ is an remote desktop protocol (RDP) server
* `ntp`_ is Network Time Protocol server

.. toctree::
   :maxdepth: 2

   tftp
   telnet
   mosquitto
