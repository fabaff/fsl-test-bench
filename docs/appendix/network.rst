.. _appendix-network:

Network
=======

 .. warning::
    This information could be obsolete.

The diagram below shows the layout of the network during the creation and the
setup of the Fedora Test bench. The FSL Test bench needs an IP address out of
10.0.0.0/24 because some services have this IP address range in their
configuration files. The hardcoded IP address is 10.0.0.64. This is a drawback
of the distribution as virtual machine.

The IP range needs to be changed in the livirtd configuration when putting
this virtual machine on a live media. ::

    x
    xx    +--------------------+      +---------------------+
     xx   | Router             |      | Host                |
      xxxx| 10.0.0.1           +------+ 10.0.0.10           |
          | 10.0.0.0/24        |      | |                   |
          |                    |      | vnet0 (Bridge)      |
          +--------------------+      |   ^                 |
                                      |   |                 |
                                      | +-+---------------+ |
                                      | | FSL Test bench  | |
                                      | | 10.0.0.64       | |
                                      | +-----------------+ |
                                      +---------------------+
