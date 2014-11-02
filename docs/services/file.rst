.. _Fedora: https://fedoraproject.org/
.. _samba: http://www.samba.org/
.. _nfs: http://nfs.sourceforge.net/

.. _services-file:

File servers
============
Serving file is often an essential feature of a server. In the Linux world
two popular systems are used, samba and nfs. It depends on the use case which
system is more common. In a Linux-only environment nfs is a good choice. If
you want to serve files for Microsoft Windows systems samba is an easy way to
go. 

* `samba`_
* `nfs`_

There is a samba share available. ::

    $ nmbscan -h 10.0.0.64
    nmbscan version 1.2.6 - laptop011 - Thu Apr 25 09:53:17 CEST 2013
    domain MYGROUP
      server TEST-BENCH
        ip-address 10.0.0.64
          ip-name fedora-test.home.network
        server-software Samba 4.0.5
        operating-system Unix
        share samba
          share-type Disk
        share IPC$
          share-type IPC
          share-comment IPC Service (Samba Server Version 4.0.5)
