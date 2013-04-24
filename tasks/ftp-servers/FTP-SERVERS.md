# FTP servers
File Transfer Protocol (FTP) is an importent protocol for transferring files
from host to host. All FTP connections are unencrypted to make it possible to
sniff the control and data connections between the client and the server.
For the Fedora Security Lab Test bench the listed ftp servers are available:

* [vsftpd](http://vsftpd.beasts.org)
* [proftpd](http://www.proftpd.org/) (not ready)
* [pure-ftpd](http://www.pureftpd.org)

# Ports assignment
To run all ftp servers on one machine it's needed that they use different ports.
Below you find a listing with the port and the assigned ftp server.

| Port     | Server                   |
|:--------:|:-------------------------|
| **21**   | vsftpd |
| **2021** | pure-ftpd |
| **2121** | proftpd |

