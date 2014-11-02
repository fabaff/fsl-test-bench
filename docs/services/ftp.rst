.. _Fedora: https://fedoraproject.org/
.. _vsftpd: http://vsftpd.beasts.org
.. _proftpd: http://www.proftpd.org/
.. _pure-ftpd: http://www.pureftpd.org

.. _services-ftp:

FTP servers
===========
File Transfer Protocol (FTP) is an importent protocol for transferring files
from host to host. All FTP connections are unencrypted to make it possible to
sniff the control and data connections between the client and the server. The
listed ftp servers are ready to include:

* `vsftpd`_
* `proftpd`_
* `pure-ftpd`_

To run all ftp servers on one machine it's needed that they use different
ports. Table below shows the ports and the assigned ftp server.

+------------+-----------+
| Port       | Server    |
+============+===========+
| 21         | vsftpd    |
+------------+-----------+
| 2021       | pure-ftpd |
+------------+-----------+
| 2221       | proftpd   |
+------------+-----------+

For vsftpd TLS support is coming soon and the configuration is not really
working. ::

    $ ftp 10.0.0.64
    Connected to 10.0.0.64 (10.0.0.64).
    220 (vsFTPd 3.0.2)
    Name (10.0.0.64:fab): bob
    331 Please specify the password.
    Password:
    230 Login successful.
    Remote system type is UNIX.
    Using binary mode to transfer files.
    ftp> ls
    500 OOPS: priv_sock_get_int
    Passive mode refused.
