.. _Ansible: http://ansible.cc/
.. _git repository: https://github.com/fabaff/fsl-test-bench
.. _script: https://git.fedorahosted.org/cgit/security-spin.git/tree/test-bench/fsl-virt-inst

.. _installation-network-setup:

Setup on a host
===============
To setup a Test bench as a separate machine you need at least two pysical
systems. A management system and the system for the Test bench. We recommand
to use the Test bench as virtual machine on a host. This has some benefits over
the setup on a physical system. You can run multiple instances and creating
new Test benches is fast and automated.The requirement are a host with a
bridged network connection and a working network, incl. DHCP/DNS.

For the setup process a connection to the internet is mandatory because some
files need to be downloaded. This guide will use the definitions
from below for the two system to make it clear which one is involved: 

* **System 1**: Is the managing system. Can be the same system from which you
  want to perform all testing task in the future.
* **System 2**: Will become the Test bench.

The first step is to create a running Fedora installation (a minimal
installation is just fine) for the Test bench on System 2. The ``fsl-virt-inst`` 
`script`_ can help to get you in this matter. Make sure that SSH
is working.

System 1 can run a Linux distribution of your choice. We assume that is a
Fedora installation too. The setup process for System 2 will be done with
`Ansible`_. It enables us to manage systems over SSH in a simple, secure,
and fast way. Install Ansible on System 1. ::

    $ sudo yum -y install ansible

Now we need to clone the Fedora Security Lab test bench `git repository`_
which contains the playbooks on System 1. Playbooks are recipes to perform
task on a remote system. ::

    $ git clone git@github.com:fabaff/fsl-test-bench.git

System 2 needs Python. Make sure that it is available. If not install it.

Then we must copy the SSH key of System 1 to the ``authorized_keys`` file of
System 2. Lauch the command from below on System 1. ::

    $ sudo ssh-copy-id -i /root/.ssh/id_rsa.pub root@[IP address of System 2]

On System 1 edit the ``/etc/ansible/hosts`` file and add the IP address of
System 2. ::

    [fsl-tb]
    IP address of System 1

    [fsl-tb-vpn]

The file ``variables/sensitive.yml`` contains all passwords.
If you don't want to run with default password, edit this file according your
needs.

Now let Ansible do the work. Below the command is shown to setup the Fedora
Security Lab Test bench on a single machine. ::

    $ sudo ansible-playbook fsl-test-bench/all-in-one.yml

When all tasks are finished, the Test bench is ready. The overview page
should be accessible: ``http://[IP address of System 2]``.
