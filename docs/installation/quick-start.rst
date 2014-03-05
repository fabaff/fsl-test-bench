.. -*- mode: rst -*-

.. _installation-quick-start:

.. _Ansible: http://ansible.cc/
.. _Ansible documentation: http://ansible.cc/docs/patterns.html
.. _Ansible Getting Started: http://ansible.cc/docs/gettingstarted.html
.. _Python: http://www.python.org/
.. _git repository: https://github.com/fabaff/fsl-test-bench
.. _file: https://github.com/fabaff/fsl-test-bench/blob/master/variables/sensitive-variables.yml

Quick-start setup
=================
This section describes the needed steps to setup a Test bench from a common
point of view in quick and fast way. In the further sections covers special
use cases which are described in detail then.

The setup of `Ansible`_ is explained on the `Ansible Getting Started`_ page.
Here is only the setup of the managed nodes and special details for the
management system covered. For every system you want to manage, you need to
have the client's SSH key in the *authorized_keys* file of the managed system
and Python.

Prerequisites
-------------
On the managing system you need the `Ansible`_ package. ::

    # yum -y install ansible

Make sure that `Python`_ is installed on the managed node(s). If not, install
the Python package. If you have performed a minimal Fedora installation Python
is available. Otherwise: ::

    # yum -y install python

.. The playbooks will using DNF as package management software instead of yum soon.

Fedora Security Lab test bench git repository
---------------------------------------------
You need to clone the Fedora Security Lab test bench `git repository`_
which contains all the playbooks. Playbooks are recipes to perform
task on a remote system. ::

    $ git clone git@github.com:fabaff/fsl-test-bench.git

If you want to contribute back to this Project, please fork it first.

SSH key
-------
Then you must copy the SSH key of the managing system to the ``authorized_keys``
file of . Lauch the command from below on the managing system. ::

    $ sudo ssh-copy-id -i /root/.ssh/id_rsa.pub root@[IP address of the node]

/etc/ansible/hosts
------------------
The file */etc/ansible/hosts* shall contain all managed hosts to be setup up.
The available groups are: 

- **fsl-tb**: Default group name for machine which uses the all-in-one playbook
- **fsl-tb-vpn**: Group name for machine which acts as VPN servers
- **fsl-tb-master**: Hosts for FSL Test bench guests when using virtualization
- **fsl_hosts**: Hosts to install the Fedora Security Lab package set

Those groups are refected in the playbook to setup only the named hosts.

More information about this topic are available are in the 
`Ansible documentation`_.

Variables
---------
After cloning the `git repository`_, edit the `variables/sensitive-variables.yml`
`file`_ if you don't want to use *password* as default password for the 
application and *testbench* for the system.

The file ``variables/sensitive.yml`` contains all passwords for root and the 
users and details for the certificate. Please edit this file according to your
needs.

Run it
------
Now let Ansible do the work. Below the command is shown to setup the Fedora
Security Lab Test bench with the `all-in-one.yml` playbook. ::

    $ sudo ansible-playbook fsl-test-bench/all-in-one.yml

All hosts which belongs to the **fsl-tb** group will be converted into Fedora
Security Lab Test benches.
