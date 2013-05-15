.. -*- mode: rst -*-

.. _appendix-kickstart:

.. _template: https://github.com/fabaff/fsl-test-bench/blob/master/files/kickstart/fedora-mini.j2
.. _git repository: https://github.com/fabaff/fsl-test-bench

Kickstart file
==============

The ``fsl-testbench.ks`` kickstart file is used to setup a minimal installation
of Fedora as libvirt-based virtual machine. ::

    # Minimal Kickstart file for the Fedora Security Lab test bench
    # Installation, not an upgrade
    install

    # No graphical things needed
    skipx
    text

    # Language
    lang en_US.UTF-8

    # Kexboard setup
    keyboard sg-latin1 
    #keyboard us

    # Networking
    network --onboot yes --device eth0 --bootproto dhcp --ipv6 auto --hostname test-bench

    # Authentication
    auth --enableshadow --passalgo=sha512
    #rootpw {{ server_root_password }}
    rootpw testbench

    # Services, SELinux and firewall
    firewall --enabled --ssh
    services --enabled network,sshd
    selinux --enforcing
    #firstboot --disable
    logging --level=info

    # Time zone
    timezone Europe/Zurich

    # Disk setup
    zerombr
    bootloader --location=mbr --append="rd_NO_PLYMOUTH"
    ignoredisk --only-use=vda
    clearpart --none --initlabel --drives=vda
    autopart

    poweroff

    %packages
    @core
    chrony
    #dnf
    bash-completion
    %end

The `template`_ can be found in the FSL Test bench `git repository`_.
