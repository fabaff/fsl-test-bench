.. _appendix-nmap:

nmap
====
The ``nmap`` output below shows the view of the Test bench from the network
side. ::

    $ sudo nmap -sV --reason 10.0.0.64

    Starting Nmap 6.45 ( http://nmap.org ) at 2014-10-28 09:44 CET
    Nmap scan report for 10.0.0.64
    Host is up, received arp-response (0.00060s latency).
    Not shown: 983 filtered ports
    Reason: 962 no-responses and 21 host-prohibiteds
    PORT     STATE  SERVICE         REASON  VERSION
    21/tcp   open   ftp             syn-ack vsftpd 3.0.2
    22/tcp   open   ssh             syn-ack OpenSSH 6.4 (protocol 2.0)
    23/tcp   open   telnet          syn-ack Linux telnetd
    25/tcp   open   smtp            syn-ack Postfix smtpd
    80/tcp   open   http            syn-ack lighttpd 1.4.35
    110/tcp  open   pop3            syn-ack Dovecot pop3d
    143/tcp  open   imap            syn-ack Dovecot imapd
    222/tcp  open   ssh             syn-ack Dropbear sshd 2014.64 (protocol 2.0)
    443/tcp  closed https           reset
    631/tcp  closed ipp             reset
    993/tcp  open   ssl/imap        syn-ack Dovecot imapd
    995/tcp  open   ssl/pop3        syn-ack Dovecot pop3d
    3389/tcp open   ms-wbt-server   syn-ack xrdp
    8000/tcp open   http            syn-ack BaseHTTPServer 0.3 (Python 2.7.5)
    8080/tcp open   http            syn-ack Apache Tomcat/Coyote JSP engine 1.1
    8088/tcp closed radan-http      reset
    8888/tcp open   sun-answerbook? syn-ack
    1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at http://www.insecure.org/cgi-bin/servicefp-submit.cgi :
    SF-Port8888-TCP:V=6.45%I=7%D=10/28%Time=544F577A%P=x86_64-redhat-linux-gnu
    SF:%r(GetRequest,4EB,"HTTP/1\.1\x20200\x20OK\r\nserver:\x20ecstatic-0\.4\.
    SF:13\r\netag:\x20\"11166-963-Sun\x20Jun\x2015\x202014\x2021:59:16\x20GMT\
    SF:+0200\x20\(CEST\)\"\r\nlast-modified:\x20Sun,\x2015\x20Jun\x202014\x201
    SF:9:59:16\x20GMT\r\ncache-control:\x20max-age=3600\r\ncontent-length:\x20
    SF:963\r\ncontent-type:\x20text/html;\x20charset=UTF-8\r\nDate:\x20Tue,\x2
    SF:028\x20Oct\x202014\x2008:44:42\x20GMT\r\nConnection:\x20close\r\n\r\n<!
    SF:DOCTYPE\x20HTML\x20PUBLIC\x20\"-//W3C//DTD\x20HTML\x204\.01//EN\">\n<!-
    SF:-\nThis\x20file\x20is\x20part\x20of\x20the\x20Fedora\x20Security\x20Lab
    SF:\x20Test\x20bench\x20and\x20distributed\x20with\nAnsible\.\n\nCopyright
    SF:\x20\(c\)\x202013-2014\x20Fabian\x20Affolter\x20<fab@fedoraproject\.org
    SF:>\n\nThe\x20FSL\x20Test\x20bench\x20is\x20licensed\x20under\x20GPLv2\.\
    SF:n-->\n<html\x20lang=\"en\">\n<head>\n\x20\x20\x20\x20<meta\x20charset=\
    SF:"utf-8\">\n\x20\x20\x20\x20<title>Fedora\x20Security\x20Lab\x20Test\x20
    SF:bench\x20\|\x20Webserver\x20is\x20up\x20and\x20running\.\.\.</title>\n\
    SF:x20\x20\x20\x20<meta\x20name=\"viewport\"\x20content=\"width=device-wid
    SF:th,\x20initial-scale=1\.0\">\n\x20\x20\x20\x20<meta\x20name=\"descripti
    SF:on\"\x20content=\"Penetration\x20testing\x20system\">\n\x20\x20\x20\x20
    SF:<meta\x20name=\"author\"\x20content=\"Joerg\x20Simon,\x20Fabian\x20Affo
    SF:lter\">\n</head>\n")%r(HTTPOptions,8F,"HTTP/1\.1\x20404\x20Not\x20Found
    SF:\r\nserver:\x20ecstatic-0\.4\.13\r\nContent-Type:\x20text/plain\r\nDate
    SF::\x20Tue,\x2028\x20Oct\x202014\x2008:44:42\x20GMT\r\nConnection:\x20clo
    SF:se\r\n\r\nNot\x20found\n")%r(FourOhFourRequest,8F,"HTTP/1\.1\x20404\x20
    SF:Not\x20Found\r\nserver:\x20ecstatic-0\.4\.13\r\nContent-Type:\x20text/p
    SF:lain\r\nDate:\x20Tue,\x2028\x20Oct\x202014\x2008:44:42\x20GMT\r\nConnec
    SF:tion:\x20close\r\n\r\nNot\x20found\n");
    MAC Address: 52:52:00:00:00:01 (Unknown)
    Service Info: Host:  testbench01.localdomain; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

    Service detection performed. Please report any incorrect results at http://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 53.28 seconds

