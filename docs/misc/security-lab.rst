.. -*- mode: rst -*-

.. _misc-security-lab:

.. _playbook: https://github.com/fabaff/fsl-test-bench/blob/master/fsl.yml
.. _Fedora Security Lab: https://fedorahosted.org/security-spin/
.. _Fedora 29 x86_64: http://mirror.karneval.cz/pub/linux/fedora-alt/releases/20/Spins/x86_64/Fedora-Live-Security-x86_64-20-1.iso
.. _Fedora 20 i686: http://mirror.karneval.cz/pub/linux/fedora-alt/releases/20/Spins/i386/Fedora-Live-Security-i686-20-1.iso
.. _Making Media: http://docs.fedoraproject.org/en-US/Fedora/18/html/Installation_Guide/sn-making-media.html
.. _Installation Guide: http://docs.fedoraproject.org/en-US/Fedora/18/html/Installation_Guide/index.html

Setup the Fedora Security Lab
=============================

The setup of the `Fedora Security Lab`_ can be done by several ways. 

Live media
-----------

There are two different Live images available of the Fedora Security Lab. Those
images can be used to create physical CDs or Live USB key.

* Download the 64-bit PC Edition: `Fedora 20 x86_64`_ Live Security
* Download the 32-bit PC Edition: `Fedora 20 i686`_ Live Security

For further information please check the `Making Media`_ section in the 
Fedora `Installation Guide`_.

comps Package group
-------------------

 .. warning::
    This work only on Fedora 19 and beyond.

You have a default Fedora installation and want all Fedora Security Lab
packages installed, you can use the groupinstall feature of yum. ::

    $ sudo yum groupinstall security-lab

Ansible playbook
----------------

The `fsl.yml` `playbook`_ contains all packages which are included in the 
Fedora Security Lab. 

Add all your hosts to ``/etc/ansible/hosts`` to the **[fsl_hosts]** group. 
Then run the playbook. ::

    $ sudo ansible-playbook fsl.yml -f 10


