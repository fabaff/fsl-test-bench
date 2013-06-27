.. -*- mode: rst -*-

.. _appendix-nmap:

nmap
====
The nmap output below shows the view of the Test bench from the network side. ::

    $ sudo nmap -sVT 10.0.0.64

    Starting Nmap 6.25 ( http://nmap.org ) at 2013-04-26 19:49 CEST
    Nmap scan report for fedora-test.home.network (10.0.0.64)
    Host is up (0.84s latency).
    Not shown: 982 filtered ports
    PORT     STATE  SERVICE         VERSION
    21/tcp   open   ftp             vsftpd 3.0.2
    22/tcp   open   ssh             OpenSSH 6.1 (protocol 2.0)
    23/tcp   open   telnet          Linux telnetd
    25/tcp   closed smtp
    80/tcp   open   http            lighttpd 1.4.31
    110/tcp  open   pop3            Dovecot pop3d
    139/tcp  open   netbios-ssn     Samba smbd 3.X (workgroup: TEST-BENCH)
    143/tcp  open   imap            Dovecot imapd
    222/tcp  open   ssh             Dropbear sshd 2012.55 (protocol 2.0)
    443/tcp  open   http            nginx 1.2.8
    445/tcp  open   netbios-ssn     Samba smbd 3.X (workgroup: TEST-BENCH)
    631/tcp  open   ipp             CUPS 1.5
    993/tcp  open   ssl/imap        Dovecot imapd
    995/tcp  open   ssl/pop3        Dovecot pop3d
    2049/tcp open   nfs             2-4 (RPC #100003)
    8080/tcp open   http            Apache Tomcat/Coyote JSP engine 1.1
    8088/tcp open   http            nginx 1.2.8
    8888/tcp open   sun-answerbook?

    Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

    Service detection performed.
    Nmap done: 1 IP address (1 host up) scanned in 85.61 seconds

