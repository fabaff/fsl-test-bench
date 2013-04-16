# Setup the FSL Test bench =
To setup a Test bench you need at least two systems either a physical machine
with a virtual machine and a bridged network connection or two physical
systems (one as system to perform the the actions and one which will serve
as Test bench). In the latter case a working network is needed too, incl.
DHCP/DNS. For the setup process a connection to the internet is mandatory
because some files need to be downloaded. This guide will use the definitions
from below for the two system to make it clear which one is involved: 

 * System 1: Is the managing system. Can be the same system from which you
want to perform all testing task in the future.
 * System 2: Will become the Test bench.

The first step is to create a running Fedora installation (a minimal
installation is just fine) for the Test bench on System 2. Make sure that SSH
is working.

System 1 can run a Linux distribution of your choice. We assume that is a
Fedora installation too. The setup process for System 2 will be done with
[http://ansible.cc/ Ansible]. It enables us to manage systems over SSH in a
simple, secure, and fast way. Install Ansible on System 1:

``bash
sudo yum -y install ansible
```

Now we need to clone the [https://github.com/fabaff/fsl-test-bench git repository]
which contains the playbooks on System 1. Playbooks are recipes to perform
task on a remote system. 

``bash
git clone git@github.com:fabaff/fsl-test-bench.git
```

Login to System 2 from System 1 as root. Check if Python is available on
System 2. If not install it. Then we must copy the SSH key to the
*authorized_keys* file.

```bash
ssh root@[IP address of System 1] 'cat ~/.ssh/id_rsa.pub' | cat - >> ~/.ssh/authorized_keys
```

On System 1 edit the */etc/ansible/hosts* file and add the IP address of
System 2. The file *variables/sensitive-variables.yml* contains all passwords.
If you don't want to run with default password, edit this file according your
needs.

Now let Ansible do the work.

```bash
sudo ansible-playbook fedora-ansible/setup.yml
```

When all tasks are finished, the Test bench is ready. The overview page
should be accessible: http://[IP address of System 2].
