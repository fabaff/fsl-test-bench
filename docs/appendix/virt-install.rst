.. -*- mode: rst -*-

.. _appendix-virt-install:

.. _template: https://github.com/fabaff/fsl-test-bench/blob/master/files/fsl-virt-install.j2
.. _git repository: https://github.com/fabaff/fsl-test-bench

virt-install
============

``virt-install`` creates a virtual machine with the a minimal kickstart file 
shown in :ref:`appendix-kickstart`. ::

    virt-install \
        --name FSL-Test-bench \
        --os-variant fedora18 \
        --ram 1024 \
        --disk /var/lib/libvirt/images/fsl-tb-f18.img,size=6 \
        --location http://mirror.switch.ch/ftp/mirror/fedora/linux/releases/18/Fedora/x86_64/os/ \
        --initrd-inject fsl-testbench.ks \
        --extra-args "ks=file:fsl-testbench.ks" \
        --noautoconsole \
        --vnc \
        --network=network:testbench \
        --mac=52:52:00:00:00:01

The `template`_ can be found in the FSL Test bench `git repository`_.
