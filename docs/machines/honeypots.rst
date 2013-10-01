.. -*- mode: rst -*-

.. _applications-honeypots:

.. _Fedora: https://fedoraproject.org
.. _honeyd: http://www.honeyd.org
.. _template: https://github.com/fabaff/fsl-test-bench/blob/master/files/honeyd.j2

Honeypots
=========

Currently the low-interaction honeypots make use of `honeyd`_. Those
honeypots are only intended to be targets for port scans. For details about
the honeypot configuration, please check the configuration `template`_.

* Microsoft Windows XP
* Microsoft Windows 2003 Server
* Linux 2.4.20

The honeypots are requesting IP addresses by DHCP. ::

    Apr 24 10:09:35 test-bench honeyd[1077]: [eth0] got DHCP offer: 10.0.0.133
    Apr 24 10:09:35 test-bench honeyd[1077]: [eth0] got DHCP offer: 10.0.0.134
    Apr 24 10:09:35 test-bench honeyd[1077]: [eth0] got DHCP offer: 10.0.0.135


A fast ``nmap`` scan shows the details about the honeypots: ::

    $ sudo nmap -sVT 10.0.0.133 10.0.0.134 10.0.0.135

    Starting Nmap 6.25 ( http://nmap.org ) at 2013-04-24 23:26 CEST
    Nmap scan report for 10.0.0.133
    Host is up (0.022s latency).
    Not shown: 997 closed ports
    PORT    STATE SERVICE       VERSION
    135/tcp open  msrpc?
    139/tcp open  netbios-ssn?
    445/tcp open  microsoft-ds?

    Nmap scan report for 10.0.0.134
    Host is up (0.016s latency).
    Not shown: 996 closed ports
    PORT    STATE SERVICE       VERSION
    80/tcp  open  http?
    135/tcp open  msrpc?
    139/tcp open  netbios-ssn?
    445/tcp open  microsoft-ds?

    Nmap scan report for 10.0.0.135
    Host is up (0.015s latency).
    Not shown: 994 closed ports
    PORT    STATE SERVICE    VERSION
    21/tcp  open  tcpwrapped
    22/tcp  open  tcpwrapped
    23/tcp  open  tcpwrapped
    25/tcp  open  smtp       Sendmail 8.12.2/8.12.2/SuSE
    110/tcp open  tcpwrapped
    143/tcp open  tcpwrapped
    Service Info: Host: test-bench.; OS: Unix

    Nmap done: 3 IP addresses (3 hosts up) scanned in 163.53 seconds


