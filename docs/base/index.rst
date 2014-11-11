.. _Fedora: https://fedoraproject.org
.. _Fedora Package Collection: https://admin.fedoraproject.org/pkgdb

.. _base-index:

Base
====
The initial idea behind the Test benches is that they can be built on-site by
the customers. This way we don't need to ship pre-configured virtual machine
images which are like blackboxes. The customers doesn't need to trust us about
what's inside the VM or check everything by themselves. They should be in
control of every setup step. Nothing is hidden and everything is transparent.
No backdoors, no malware, no evil stuff.

The core components are installed out of the `Fedora Package Collection`_, if
they are available. This ensures that the operating system run the latest
packages and behave with integrity.

After the setup of the FSL Test bench is possible to update the system with
the package management tools. ::  

    $ sudo yum -y update

Vulnerable web application, PHP shells, and some helper tools are download 
directly from their upstream locations. It's not possible to update those 
application automatically.

One advantage of the on-site creation process, if creating a network host, is
that the local network setup is detected and is used to configure the Test
benches. The Test bench is ready to use.

A disadvantage is that a connection to the internet is needed during the
setup process and a already working network infrastructure with DHCP/DNS has
to be present. The customer needs minimal technical skill for the setup. It's
not a one-click-thing.

It's also possible to build a Fedora Security Lab Test bench on a local machine
which is very straight-forwards and easy to do. The local setup encapsulates 
the Test bench from the world and is only accessible from the host.

.. toctree::
   :maxdepth: 2

   architecture
   system-details
