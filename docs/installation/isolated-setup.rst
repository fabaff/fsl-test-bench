.. -*- mode: rst -*-

.. _installation-local-setup:

.. _script: https://git.fedorahosted.org/cgit/security-spin.git/plain/test-bench/fsl-tb-inst
.. _git repository: https://github.com/fabaff/fsl-test-bench
.. _Virtual Machine Manager: http://virt-manager.et.redhat.com/

Setup in an isolated environment
================================

 .. warning::
    sorry, not implemented. Development will hopefully happen in the future.

The Fedora Security Lab environment can be used to create a complete
environment consisting of an attack target and attackers in an isolated area
of an existing physical network or a class room.

Requirement
-----------

The requirements for running a Fedora Security Lab Environment are:

* A system which is capable of acting as server, is able to boot from external
  devices (USB), and have a network interface 
* working physical network (all systems are connected to the same network
  segment)
* some systems capable for network booting (PXE boot)

Basically a class room for the computer science education is a good starting
point. ::

         Switch
      +----------------+     +---------+
      |X X X X X X X X |     |Server   |
      +^-^-^---------^-+     |- DHCP   |
       | | |         |       |- PXE    |
       | | |         +-------|- Data   |
       | | |                 +---------+
       | | |
       | | +-----------------+
       | +--------+          |
      ++-------+ ++-------+ ++-------+
      |Client 1| |Client 2| |Client 3|
      +--------+ +--------+ +--------+

Setup Course
------------

* Disconnect the physical network from the outside
* Start the system which will become the server
* When the server is up and running, start your other system after you have
  changed their BIOS boot sequence to `Boot from network` or similar.



