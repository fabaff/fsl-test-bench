# Fedora Security Lab Test bench - FAQ

**Is the Fedora Security Lab Test bench a Live CD?**
No, it's a default Fedora installation which is configured with the help of
[Ansible][http://ansible.cc/]. For setup a system like the Fedora Security Lab
Test bench some file modifications are needed. Live CDs don't allow to ship
modified content or files.

**Why not make RPMS of all parts?**
Because the Package Review process in Fedora is slow (even for simple packages
it takes months and I wanted to have the FSL Test bench now). Most software
core parts are coming out of the Fedora Package Collection. The surrounding 
items and the configuration are installed by Ansible out of their upstream 
sources.

**Will the Fedora Security Lab Test bench become a Live CD one day?**
I don't think so, but never say never.

**Can I use the FSL Test bench repository to setup a Fedora Security Lab?**
Yes, you can. Periodically the [fsl-packages.yml](https://git.fedorahosted.org/cgit/security-spin.git/log/ansible-playbooks/fsl-packages.yml) playbook get synced. This ways you don't need to clone the 
[Fedora Security Lab](https://fedorahosted.org/security-spin/) git repository
to install Fedora Security Lab host.

**Why are you using dnf and not yum?**
The reason is simple DNF will become the next default Package manager for
Fedora. And as always we wanted to be ahead of the rest of the world.

**Do you have some reference installations?**
No. This is project is a proof of concept only at the moment.

**How long does it take for Zero to go?**
Creating a libvirt-based virtual machine and using Ansible to configure it, 
takes something between 15 and 20 minutes. It heavily depends on your hardware
and the speed of your internet connection.

**Is this something similar to Fedora Formulas?**
Yes, it is. Basically we skipped the discussions and just made an implementation
which we think is feasible for our needs.

**Why is this project not hosted on Fedorahosted.org?**
Because github offers easy access to the git repositories for everyone not only
Fedora contributors. To get as many contributions as possible we need to be as
open as possible.
The [Fedora Security Lab](https://fedorahosted.org/security-spin/) is hosted
on [Fedorahosted.org](https://fedorahosted.org) and we don't plan to change
that.

**Can I contribute?**
Sure, contributions are appriciated. Please for the Fedora Security Lab Test
bench repository and when you are done, open a **Pull request**.

**Can I include item X?**
Please follow the Fedora Project guidelines in this matter. The
[Forbidden items](http://fedoraproject.org/wiki/Forbidden_items) page in 
the Fedora Wiki is a good starting place. The item to include must be under an
open source license, not proprietary, and not violate laws.
