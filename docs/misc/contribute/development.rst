.. -*- mode: rst -*-

.. _misc-contribute-development:

.. _Ansible: http://ansible.cc/
.. _modules: http://ansible.cc/docs/modules.html
.. _playbooks: http://ansible.cc/docs/playbooks.html
.. _documentation: http://ansible.cc/docs/

.. _Fedora Package Collection: https://apps.fedoraproject.org/packages/
.. _Fedora Security Lab: https://fedorahosted.org/security-spin/

.. _git repository: https://github.com/fabaff/fsl-test-bench
.. _git: http://git-scm.com/
.. _Fork A Repo: https://help.github.com/articles/fork-a-repo
.. _Github: https://github.com/

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Jinja2: http://fedoraproject.org/
.. _YAML: http://www.yaml.org/

.. _template: https://github.com/fabaff/fsl-test-bench/blob/master/template.yml
.. _file: https://github.com/fabaff/fsl-test-bench/blob/master/files/motd.j2

Development
===========
Most parts of the Fedora Security Lab Test bench are `Ansible`_ playbooks.
There are some helper script in Bash and Python. The web interface is made with
simple HTML files.

Git setup
---------
First install `git`_ on your system. ::

    $ yum -y install git

After installing git, identify yourself to git with your name and your
email address. ::

    $ git config --global user.name "Your name"
    $ git config --global user.email "your.name@example.com"

`Github`_ provides tools for collaboration including a way to easy fork
existing repositories. Go to the Fedora Security Lab Test Bench 
`git repository`_ and fork it. For more detail please refer to the
`Fork A Repo`_ page of Github. Clone your fork: ::

    $ git clone git@github.com:your_github_username/fsl-test-bench.git

At the moment there is no connection to the upstream repository. You need to
add another remote named "upstream" which points to the upstream repository. ::

    $ cd fsl-test-bench
    $ git remote add upstream git@github.com:fabaff/fsl-test-bench.git

Make changes, add new features, write documentation, or fix typos. Then commit
all changes. ::

    $ git add new_file
    $ git commit new_file -m "This is a new file"
    $ git push origin master

If you are done, send a **pull request**.

Don't forget to pull-in changes from the upstream repository from time to time
as described in the `Fork A Repo`_ document. ::

    $ git pull --rebase upstream master

Layout git repository
---------------------
The all source files are located in the *`docs`_* folder. All file are written with
the `reStructuredText`_ syntax. The structure of the *`docs`_* folder devide
the content in various sub-folders those folder represent sections in the
documentation ::

        .
        ├── docs ----------------- Documentation
        ├── files ---------------- Template files
        │   └── kickstart -------- Kickstart files for the installation
        ├── handlers ------------- Handlers for services
        ├── tasks ---------------- A collection of tasks
        │   ├── apps ------------- Vulnerable web applications
        │   ├── helpers ---------- Helper tools
        │   ├── honeypots -------- Low-interaction honeypots
        │   └── shells ----------- PHP shells
        └── variables ------------ Storage files for variables


**Template files**

All templates are located in *files* and are using the `Jinja2`_ engine. This 
means that you can placed The example below shows a section of the `motd`
`file`_. ::

          Hostname    : {{ ansible_hostname }}
          System type : {{ ansible_system }}
          Kernel      : {{ ansible_kernel }}

A nice way to check what variables are available is::

    $ sudo ansible -m setup [IP of a managed host]

**Handlers**

The so-called handlers can be used as shortcut for managing services, like
stop, start, and restart. If a new service is included, the handlers should be
present. At the moment the playbook doesn't make heavy use of handlers.

**Tasks**

This folder contains all playbooks. If the playbook fits into an existing 
category it's placed in the corresponding sub-folder.

**Variables**

The files in *variables* contains values which can be accessed from other
playbooks. This make it possible to reuse certain values over different 
plays. 

Writing playbooks
-----------------
Playbooks are written in `YAML`_ which makes the playbook very easy to read and
to write. `Ansible`_ provides a bunch of `modules`_ for various operation. Those
modules are used in the `playbooks`_. Please read the `playbooks`_ section in
the Ansible `documentation`_ to familar with the concept of the playbooks.

There is a `template`_ playbook online which acts as a starting point.

To have a basic level of modularization, one playbook should only include tasks
for one application or tool and then included in another playbook::

      tasks:
        - include: tasks/libvirt.yml
        - include: tasks/virt-install.yml

Please make sure that you use the full path when invoking commands 
``command: /usr/bin/mv`` instead just ``command: mv``.

