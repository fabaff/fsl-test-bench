.. -*- mode: rst -*-

.. _services-others:

.. _Fedora: https://fedoraproject.org/
.. _OpenVPN: http://openvpn.net
.. _cups: http://www.cups.org
.. _ngircd: http://ngircd.barton.de/
.. _dropbear: https://matt.ucc.asn.au/dropbear/dropbear.html
.. _openssh: http://www.openssh.org/
.. _tftp: http://sourceforge.net/projects/tftp-server/
.. _xrdp: http://www.xrdp.org/
.. _ntp: http://www.ntp.org/
.. _MQTT: http://mqtt.org/
.. _mosquitto: http://mosquitto.org/

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
* `tftp`_ (xinetd) is a single port Trivial File Transfer Protocol server
* `OpenVPN`_ server with a static key
* `cups`_ is a standards-based printing system
* `ngircd`_ is a lightweight Internet Relay Chat server
* `xrdp`_ is an remote desktop protocol (RDP) server
* `ntp`_ is Network Time Protocol server
* `mosquitto`_ is a `MQTT`_ message broker

telnet
------

The tftp server is serving a simple text file. ::

    $ ls
    $ tftp 10.0.0.64
    tftp> get info.txt
    tftp> quit
    $ ls
    info.txt

User should be able to connect to a telnet server. ::

    $ telnet 10.0.0.65
    Trying 10.0.0.65...
    Connected to 10.0.0.65.
    Escape character is '^]'.
    Fedora release 18 (Spherical Cow)
    Kernel 3.9.4-200.fc18.x86_64 on an x86_64 (1)
    test-bench login:

mosquitto
---------

Subscribing to the topic **fsl/testbench** of the `MQTT`_ broker from your local machine::

    $ $ mosquitto_sub -h 10.0.0.65 -d -t fsl/testbench
    Client mosqsub/24366-laptop011 sending CONNECT
    Client mosqsub/24366-laptop011 received CONNACK
    Client mosqsub/24366-laptop011 sending SUBSCRIBE (Mid: 1, Topic: fsl/testbench, QoS: 0)
    Client mosqsub/24366-laptop011 received SUBACK
    Subscribed (mid: 1): 0

Publishing messages on your FSL Test bench::

    $ mosquitto_pub -d -t fsl/testbench -m "This is a message from your FSL Test bench"
    Client mosqpub/20531-test-benc sending CONNECT
    Client mosqpub/20531-test-benc received CONNACK
    Client mosqpub/20531-test-benc sending PUBLISH (d0, q0, r0, m1, 'fsl/testbench', ... (42 bytes))
    Client mosqpub/20531-test-benc sending DISCONNECT

You should now get the message from the FSL Test Bench. ::

    Client mosqsub/24366-laptop011 received PUBLISH (d0, q0, r0, m0, 'fsl/testbench', ... (42 bytes))
    This is a message from your FSL Test bench

