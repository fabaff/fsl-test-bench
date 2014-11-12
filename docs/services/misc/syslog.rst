.. _syslog-ng: http://www.balabit.com/network-security/syslog-ng
.. _RFC3164: http://tools.ietf.org/html/rfc3164
.. _RFC5424: http://tools.ietf.org/html/rfc5424

.. _services-misc-syslog:

syslog-ng
=========
`syslog-ng`_ is an implementation of the Syslog protocol. It uses the standard
BSD syslog protocol, specified in `RFC3164`_ and the proposed `RFC5424`_.

Using the server
----------------

    mausezahn -t syslog sev=3 -P "Message from FSL." -A 10.1.1.109 -B 192.168.7.7
