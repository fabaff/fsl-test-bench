.. -*- mode: rst -*-

.. _services-misc-ntp:

.. _ntp: http://www.ntp.org/
.. _nmap: http://nmap.org/

ntp
===

The Network Time Protocol (`ntp`_) is a networking protocol for the
synchronization of clocks of computer systems over networks. NTP is
providing the information in UTC (Coordinated Universal Time).

Login your FSL Test bench to check if you have connections to ntp servers.::

    # ntpq -p
         remote           refid      st t when poll reach   delay   offset  jitter
    ==============================================================================
    *ds1789963.dedic 192.53.103.103   2 u    1   64    1   16.390    2.484   0.674
     ns1.pmodwrc.ch  189.247.1.117    2 u    2   64    1   19.949    0.255   0.502
     ntppublic.uzh.c 130.60.205.7     3 u    1   64    1   16.315    2.361   0.341
     aerith.projectd 217.147.208.1    3 u    2   64    1   22.728   -0.846   0.022

Sync your clock with the Fedora Security Lab Test Bench::

    $ sudo ntpdate 10.0.0.65
    16 Aug 10:56:08 ntpdate[30588]: adjust time server 10.0.0.65 offset 0.002292 sec

Unless an error message is displayed, the system time of your local system 
should now be set.

.. note:: It was not tested if this works without a connection to the internet.
