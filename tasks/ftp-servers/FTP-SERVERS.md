# FTP servers
Nowadays there are a couple of webservers around for Linux. 'apache', 'nginx',
and 'lighttpd' just to name the most popular. Every type of webserver has its
purpose and its unique fingerprint. The following webserver are available for 
a Fedora Security Test bench setup:

* [vsftpd](http://vsftpd.beasts.org)
* [proftpd](http://www.proftpd.org/)
* [pure-ftpd](http://www.pureftpd.org)

# Ports assignment
To run all ftp servers on one machine it's needed that they use different ports.
Below you find a listing with the port and the assigned ftp server.

| Port     | Server                   |
|:--------:|:-------------------------|
| **21**   | vsftpd |
| **2021** | pure-ftpd |
| **2121** | proftpd |

