# Setup the FSL Test bench
To setup a Test bench you need at least two systems either a physical machine
with a virtual machine and a bridged network connection or two physical
systems (one as system to perform the actions and one which will serve as
Test bench). In the latter case a working network is needed too, incl.
DHCP/DNS. For the setup process a connection to the internet is mandatory
because some files need to be downloaded. This guide will use the definitions
from below for the two systems to make it clear which one is involved: 

 * System 1: Is the managing system. Can be the same system from which you
want to perform all testing task in the future.
 * System 2: Will become the Test bench.

The first step is to create a running Fedora installation (a minimal
installation is just fine) for the Test bench on System 2. Make sure that SSH
is working.

System 1 can run a Linux distribution of your choice. We assume that is a
Fedora installation too. The setup process for System 2 will be done with
[Ansible](http://ansible.cc/). It enables us to manage systems over
SSH in a simple, secure, and fast way. Install Ansible on System 1:

```bash
$ sudo dnf -y install ansible
```

Now we need to clone the Fedora Security Lab test bench 
[git repository](https://github.com/fabaff/fsl-test-bench)
which contains the playbooks on System 1. Playbooks are recipes to perform
task on a remote system. 

```bash
$ git clone https://github.com/fabaff/fsl-test-bench.git
```

System 2 needs Python. Make sure that it is available. If not install it.

Then we must copy the SSH key of System 1 to the *authorized_keys* file of
System 2. Lauch the command from below on System 1.

```bash
$ sudo ssh-copy-id -i /root/.ssh/id_rsa.pub root@[IP address of System 2]
```

On System 1 edit the */etc/ansible/hosts* file and add the IP address of
System 2. 

```bash
[fsl-tb]
IP address of System 1

[fsl-tb-vpn]

```

The file *variables/sensitive.yml* contains all passwords. If you don't want
to run with default password, edit this file according your needs.

Now let Ansible do the work. Below the command is shown to setup the Fedora
Security Lab Test bench on a single machine.

```bash
$ sudo ansible-playbook fsl-test-bench/all-in-one.yml
```

When all tasks are finished, the Test bench is ready. The overview page
should be accessible: http://[IP address of System 2].
