.. -*- mode: rst -*-

.. _faq-index:

.. _Ansible: http://ansible.cc/
.. _Fedora Package Collection: https://apps.fedoraproject.org/packages/
.. _setup page: https://fedorahosted.org/security-spin/wiki/Test%20bench%20setup
.. _fsl-packages.yml: https://git.fedorahosted.org/cgit/security-spin.git/log/ansible-playbooks/fsl-packages.yml
.. _Fedora Security Lab: https://fedorahosted.org/security-spin/
.. _Fedorahosted.org: https://fedorahosted.org
.. _Forbidden items: http://fedoraproject.org/wiki/Forbidden_items

FAQ
===

Is the Fedora Security Lab Test bench a Live CD?
------------------------------------------------
No, it's a default Fedora installation which is configured with the help of
`Ansible`_. For setup a system like the Fedora Security Lab Test bench some
file modifications are needed. Live CDs don't allow to ship modified content
or files.

Why not make RPMS of all parts?
---------------------------------
Because the Package Review process in Fedora is slow (even for simple packages
it takes months and I wanted to have the FSL Test bench now). Most software
core parts are coming out of the Fedora Package Collection. The surrounding 
items and the configuration are installed by Ansible out of their upstream 
sources.

Will the Fedora Security Lab Test bench become a Live CD one day?
-----------------------------------------------------------------
I don't think so, but never say never. We are customizing configuration files.
Those configuration files are modified during the setup process to match the
provided environment. The web interface is dynamically generated according
your choises on the fly. This is not possible with a Spin.

Do you provide a VM or something similar?
-----------------------------------------
No, because one big issue is trust. Providing a VM is like shipping a
blackbox. You have to trust us about what's inside the VM. By using Ansible's
playbooks you can see what steps are taken to setup the FSL Test bench. You
are in control of every setup step, nothing is hidden and everything is
transparent. The core components are installed out of the
`Fedora Package Collection`_ on top of a minimal Fedora installation. This
ensure that the operating system runs the latest packages and behave with
integrity.

How should the network around the FSL Test bench looks like?
------------------------------------------------------------
As mentioned on the `setup page`_ a DNS/DHCP server is a requirement. For
security purposes we suggest that you use a dedicated network for setup your
FSL Test bench.

Is internet access needed for the Fedora Security Lab Test bench?
-----------------------------------------------------------------
For the setup access to the internet of the system which will host the FSL
Test bench is needed. When the setup is finished, you can shutdown
the internet access.
DO NOT expose the FSL Test bench to the internet. Bad things could
happen. You have been warned.

Can I use the FSL Test bench repository to setup a Fedora Security Lab?
-----------------------------------------------------------------------
Yes, you can. Periodically the `fsl-packages.yml`_ playbook get synced. This
ways you don't need to clone the `Fedora Security Lab`_ git repository
to install Fedora Security Lab host.

Why are you still using yum and not dnf?
----------------------------------------
First DNF was used, then we switched back to yum. Soon we will switch to DNF
again because DNF will become the next default Package manager for
Fedora. And as always we wanted to be ahead of the rest of the world.

Do you have some reference installations?
-----------------------------------------
No. This is project is a proof of concept only at the moment.

How long does it take from Zero to go?
--------------------------------------
Creating a libvirt-based virtual machine and using Ansible to configure it, 
takes something between 25 and 30 minutes. It heavily depends on your hardware
and the speed of your internet connection.

Is The Fedora Security Lab Test Bench vulnerable for Heartbleed?
----------------------------------------------------------------
It depends on the point in time when you created your Test bench. Check if
you are running at least with ``openssl-1.0.1e-37.fc20``.

Is this something similar to Fedora Formulas?
---------------------------------------------
Yes, it is. Basically we skipped the discussions and just made an implementation
which we think is feasible for our needs.

Why is this project not hosted on Fedorahosted.org?
---------------------------------------------------
Because github offers easy access to the git repositories for everyone not only
Fedora contributors. To get as many contributions as possible we need to be as
open as possible.
The `Fedora Security Lab`_ is hosted on `Fedorahosted.org`_ and we don't plan
to change that.

Can I contribute?
-----------------
Sure, contributions are appriciated. Please for the Fedora Security Lab Test
bench repository and when you are done, open a **Pull request**.

Can I include item X?
---------------------
Please follow the Fedora Project guidelines in this matter. The 
`Forbidden items`_ page in the Fedora Wiki is a good starting place. The item
to include must be under an open source license, not proprietary, and not
violate laws.
