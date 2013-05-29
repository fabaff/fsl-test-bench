.. -*- mode: rst -*-

.. _misc-contribute-web-interface:

.. _Ansible: http://ansible.cc/
.. _Fedora Package Collection: https://apps.fedoraproject.org/packages/

.. _bootstrap: http://twitter.github.io/bootstrap/
.. _playbook: https://github.com/fabaff/fsl-test-bench/blob/master/tasks/website.yml
.. _Jinja2: http://jinja.pocoo.org/docs/
.. _folder: https://github.com/fabaff/fsl-test-bench/tree/master/files/website

Web interface
=============

The web interface is based on Twitter's `bootstrap`_ front-end framework. The 
`website.yml` `playbook`_ is delivering `Jinja2`_ template pages. 

The *file/website* `folder`_ contains the all template files which will be
rendered as html during the setup process. The most importent files are:

- **about.j2** : This file contain further details about the Test bench.
- **contact.j2** : This file provides contact details and links to additional
  resources.
- **index.j2** : The index.html file shows all available application on the
  Test bench and gives the user easy access to those tools.
