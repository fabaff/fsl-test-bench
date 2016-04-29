.. _Fedora: https://fedoraproject.org
.. _Ansible: http://ansible.cc
.. _Jinja2: http://fedoraproject.org/
.. _Lighttpd: https://fedoraproject.org
.. _MySQL: https://fedoraproject.org

.. _base-architecture:

Architecture
============
The whole configuration of the Fedora Security Test bench is always made on
top of a minimal `Fedora`_ installation or a default installation. It doesn't
matter if the target system is a physical one or a virtual machine. After the
installation of Fedora (or one of Fedora's downstream distribution like RHEL,
Scientific Linux, etc. if wished [#f1]_) is done and the setup the SSH
connection is finished, `Ansible`_ is used to distribute the configurations of
all included items.

.. blockdiag::

    blockdiag admin {
      "Fedora Installation" -> Ansible -> "Fedora Security Lab Test bench";

    "Fedora Security Lab Test bench" [color = "greenyellow"];
    }

It's possible to setup multiple Test benches at the same time with different
features. Thanks to Ansible it's very easy to integrate new features or omit
things. The so-called playbooks are easy to read and to write. ::

    ---
    - hosts: all
      user: root 
      tasks:
      - name: install default motd file
        template: src=fedora-motd.j2
                  dest=/etc/motd
                  owner=root
                  mode=0755

Built-in modules facilitate the configuration tasks and templates supports
the `Jinja2`_ engine. ::

    <Location />
      Order deny,allow
      Deny from all
      Allow from 127.0.0.1
      Allow from {{ ansible_eth0.ipv4.network }}/24
    </Location>

Ansible is based on Python and doesn't need a client on the managed system.

For a permanent lab setup and for performance reasons separating and/or
multiplying the Test benches would be a good choice.

All application and services included by the Fedora Security Lab Test bench
are running on a current minimal `Fedora`_ installation. The `Lighttpd`_ 
server acts as primary web server and is serving the web interface of the Test
bench. A `MySQL`_ server is available for database interactions and is hosting
the databases for the vulnerable web applications.

.. rubric:: Footnotes

.. [#f1] For EPEL aren't the same packages available as for Fedora. Please keep
         this in mind when trying to run the Test bench on a non Fedora machine.
