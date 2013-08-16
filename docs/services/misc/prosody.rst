.. -*- mode: rst -*-

.. _services-misc-prosody:

.. _prosody: http://prosody.im
.. _XMPP: http://xmpp.org/
.. _Jabber: http://www.jabber.org/
.. _mcabber: http://www.lilotux.net/~mikael/mcabber/
.. _console: http://prosody.im/doc/console

prosody
=======

`prosody`_ is a communications server for `Jabber`_/`XMPP`_.

Using the server
----------------

To connect the Jabber server with `mcabber`_ create the configuration file
``.mcabberrc`` in the home directory with the following content for the
**admin**::

    set jid = admin@10.0.0.65
    set password = admin
    set server   = 10.0.0.65
    set resource = console
    set priority = 1
    set ssl_ignore_checks = 1

Or if you want to connect as user **bob**. Open an additional terminal and
switch to user **bob**::

    # su - bob

Create the ``.mcabberrc`` configuration file for **bob**:

    set jid = bob@10.0.0.65
    set password = bob
    set server   = 10.0.0.65
    set resource = console
    set priority = 1
    set ssl_ignore_checks = 1

Start ``mcabber``

    $ mcabber

Add all users you like to your roster and vice versa. Replace the usernames
with the user you would like to add.::

    /add bob@10.0.0.65
    /authorization allow admin@10.0.0.65

.. _mcabber-fig:
.. figure:: ../../images/macabber.png
    :width: 600px
    :align: center
    
    Mcabber  

When done, quit::

    /quit

Telnet console
--------------

On the Fedora Security Lab Test bench the prosody server provides a telnet
`console`_ to interact with. ::

    $ telnet localhost 5582
    Trying ::1...
    telnet: connect to address ::1: Connection refused
    Trying 127.0.0.1...
    Connected to localhost.
    Escape character is '^]'.
    |                    ____                \   /     _       
                        |  _ \ _ __ ___  ___  _-_   __| |_   _ 
                        | |_) | '__/ _ \/ __|/ _ \ / _` | | | |
                        |  __/| | | (_) \__ \ |_| | (_| | |_| |
                        |_|   |_|  \___/|___/\___/ \__,_|\__, |
                        A study in simplicity            |___/ 


    | Welcome to the Prosody administration console. For a list of commands, type: help
    | You may find more help on using this console in our online documentation at 
    | http://prosody.im/doc/console

Let's get the uptime from the server as example. ::

    server:uptime()
    | OK: This server has been running for 0 days, 0 hours and 7 minutes (since Fri Aug 16 17:03:24 2013)
