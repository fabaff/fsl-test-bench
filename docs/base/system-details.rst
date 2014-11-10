.. _Network XML format: http://libvirt.org/formatnetwork.html
.. _Libvirt Project: http://libvirt.org
.. _NAT: http://wiki.libvirt.org/page/VirtualNetworking#Network_Address_Translation_.28NAT.29
.. _local.yml: https://github.com/fabaff/fsl-test-bench/blob/master/variables/local.yml
.. _local-setup.yml: https://github.com/fabaff/fsl-test-bench/blob/master/local-setup.yml
.. _git repository: https://github.com/fabaff/fsl-test-bench
.. _network template: https://github.com/fabaff/fsl-test-bench/blob/master/files/libvirt-network.j2
.. _fsl-virt-inst: https://git.fedorahosted.org/cgit/security-spin.git/tree/test-bench/fsl-virt-inst

.. _base-system-details:

System details
==============
This section provides details about the different kind of Test bench setups
which are possible and their specific default configuration.

Local virtual machine
---------------------
This setup option (`local-setup.yml`_) creates a local virtual machine with 
``virt-install`` on the local host. The variables defined in the `local.yml`_ 
are fed to various files, a kickstart file, the ``virt-install`` script, 
and the network configuration shown later in this section.

The default settings in `local.yml`_ are very generic. ::

    ---
    # User settings
    language: en_US.UTF-8
    keyboard: sg-latin1
    timezone: Europe/Zurich

    # Name of the virtual machine
    virtname: FSL-Test-bench

    # Name of the disk image
    img_name: fsl01

    # Name of the bridge
    bridge: virbr1

    # Memory of the virtual machine
    ram: 1024

The network for the Test bench is separated from the default libvirt network 
to avoid conflicts. It's using `NAT`_ and the interface **virbr1**.

.. nwdiag::

    nwdiag {
      network [shape = cloud];
      network -- host;

      network libvirt {
        address = "10.1.1.0/24";
        host [address = "10.1.1.1"];
        testbench [address = "10.1.1.5"];
        honeypots [address = "10.1.1.x"];
      }
    }

The variables out of the `local.yml`_ file are used to fill the 
libvirt `network template`_. The standard setup for the **testbench**
network looks like the example below. 

.. code-block:: xml

    <network>
      <name>testbench</name>
      <uuid>391123e3-6666-154f-dd58-64b43435274755642</uuid>
      <forward mode='nat'/>
      <bridge name='virbr1' stp='on' delay='0' />
      <mac address='52:52:11:22:33:44'/>
      <ip address='10.1.1.1' netmask='255.255.255.0'>
        <dhcp>
          <range start='10.1.1.5' end='10.1.1.50' />
          <host mac='52:52:00:00:00:01' name='test-bench' ip='10.1.1.5' />
        </dhcp>
      </ip>
    </network>

.. $ sudo virsh net-edit testbench

Additional details about the format and different option, can be found in the 
`Network XML format`_ documentation of the `Libvirt Project`_.

Network host
------------
If you choose this way to go, you need to take care of the network
configuration and the installation of Fedora. In environments where a
automatic provisioning solution for operating system is available this is the
easiest way to start.  

Virtualized host
----------------
The difference between be network host setup and the virtualized host setup is
that multiple Test benches could run on a single host. The setup doesn't work 
with NAT with is the default of libvirt. You need to setup a bridge and your
virtual machine must be able to connect to that bridge. You can use the
`fsl-virt-inst`_ script. This script create a guest with a minimal Fedora
installation which can be used for the Test bench.

This setup is perferred over a network host because it gives more flexibility. 

Environment
-----------

 .. warning::
    sorry, not implemented

The idea is to have an external USB/Firewire harddrive with all needed data on
it. Meaning all packages (mirrored from the Fedora Package collection), all
other components downloaded, and the configuration files ready. You plug that
drive in and this machine act as server. Then DHCP/DNS services are setup
automatically, a PXE configuration is put in place, and Test benches as
virtual machines on the server are created. The clients use the server's
PXE capability to setup themselfs. No access to the internet is needed and
the whole environment can stay isolated. The only prerequirement then is
hardware and a physical network which both are often present in class rooms.

