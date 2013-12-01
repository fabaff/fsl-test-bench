.. -*- mode: rst -*-

.. _services-misc-snmp:

.. _net-snmp: http://www.net-snmp.org/

snmp
====

The Simple Network Management Protocol (SNMP) protocol was designed for
monitoring the health and welfare of computer and network equipment.

Get the data pn your Fedora Security Lab Test Bench::

    $ snmpwalk -v2c -c public localhost system

Or check it from a system in the same network::

    $ snmpwalk -v2c -c public 10.0.0.64 system
