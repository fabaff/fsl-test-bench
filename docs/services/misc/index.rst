.. _Fedora: https://fedoraproject.org/

.. _services-others:

Other servers/services
======================
The Fedora Security Lab Test bench is hosting some services which are usualy
not found on public accessible systems. ``telnet`` was replaced with more secure
systems. Nowadays ``tftp`` is mainly used for provisioning VoIP installations.
Print servers like ``cups`` are used in office environments.

To give the students the possibility to work with VPN, an OpenVPN setup with
a static key is included.   

.. toctree::
   :maxdepth: 2

   tftp
   telnet
   openvpn
   openssh
   dropbear
   cups
   ngircd
   xrdp
   ntp
   mosquitto
   prosody
   snmp
