.. -*- mode: rst -*-

.. _appendix-host-system:

Host system
===========

The host system was a machine running Fedora 19. CPU is an Intel(R) Core(TM)2
Quad CPU Q6600 @ 2.40 GHz with 8 GB of memory. The hypervisor was KVM and
libvirt 1.0.5.6. ::

    $ cat /etc/fedora-release
    Fedora release 19 (Schrödinger’s Cat)

With one of the latest kernel. ::

    $ uname -a
    Linux host01.home.network 3.6.11-5.fc17.x86_64
    #1 SMP Tue Jan 8 21:40:51 UTC 2013 x86_64 x86_64 x86_64 GNU/Linux

The network configuration looked like this: ::

    $ ip addr
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 16436 qdisc noqueue state UNKNOWN 
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
        inet6 ::1/128 scope host 
           valid_lft forever preferred_lft forever
    2: em1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast 
    state UP qlen 1000
        link/ether 90:e6:ba:69:f2:76 brd ff:ff:ff:ff:ff:ff
        inet 10.0.0.10/24 brd 10.0.0.255 scope global em1
        inet6 fe80::92e6:baff:fe69:f276/64 scope link 
           valid_lft forever preferred_lft forever
    3: p37p1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast 
    master vnet0 state UP qlen 1000
        link/ether 90:e6:ba:69:d6:ae brd ff:ff:ff:ff:ff:ff
        inet6 fe80::92e6:baff:fe69:d6ae/64 scope link 
           valid_lft forever preferred_lft forever
    4: p3p1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast 
    state DOWN qlen 1000
        link/ether 00:30:4f:53:fa:b7 brd ff:ff:ff:ff:ff:ff
    5: vnet0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue 
    state UP 
        link/ether 90:e6:ba:69:d6:ae brd ff:ff:ff:ff:ff:ff
        inet 10.0.0.104/24 brd 10.0.0.255 scope global vnet0
        inet6 fe80::92e6:baff:fe69:d6ae/64 scope link 
           valid_lft forever preferred_lft forever
    6: virbr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue 
    state DOWN 
        link/ether 52:54:00:31:fe:4d brd ff:ff:ff:ff:ff:ff
        inet 192.168.122.1/24 brd 192.168.122.255 scope global virbr0
    [snip]
    14: vnet5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master 
    vnet0 state UNKNOWN qlen 500
        link/ether fe:52:00:00:00:01 brd ff:ff:ff:ff:ff:ff
        inet6 fe80::fc52:ff:fe00:1/64 scope link 
           valid_lft forever preferred_lft forever
