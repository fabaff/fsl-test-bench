.. -*- mode: rst -*-

.. _misc-contribute-documentation:

.. _Sphinx: http://sphinx-doc.org/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Documentation: https://fedora-security-lab-test-bench.readthedocs.org/en/latest/
.. _Read the Docs: https://readthedocs.org/

.. _template: https://github.com/fabaff/fsl-test-bench/blob/master/template.yml
.. _folder: https://github.com/fabaff/fsl-test-bench/tree/master/docs

.. _sphinx-bootstrap-theme: http://loose-bits.com/
.. _blockdiag: http://blockdiag.com
.. _nwdiag: http://blockdiag.com/en/nwdiag/index.html

Documentation
=============

The documention source files are located in the *docs* `folder`_. All files are
written with the `reStructuredText`_ syntax. The structure of the *docs*
`folder`_ devide the content in various sub-folders those folder represent
sections in the documentation ::

    .
    |-- appendix --------- The documentation's appendix
    |-- applications ----- Application section 
    |-- base ------------- Base information about the FSL Test bench
    |-- _build ----------- Sphinx folder (the generated documentation)
    |-- conf.py ---------- Configuration file for Sphinx
    |-- images ----------- Screenshots
    |-- index.rst -------- Default file for the documentation
    |-- installation ----- Installation section
    |-- intro ------------ Introduction section
    |-- Makefile --------- Makefile for building the documentation locally
    |-- misc ------------- This section contains various topics 
    |-- requirements.txt - This file is needed by Read the Docs
    |-- services --------- Section with details about the available services
    |-- _static ---------- Sphinx folder
    `-- _templates ------- Sphinx folder

The documentation uses the `sphinx-bootstrap-theme`_ as theme. This theme is 
not available in the official Sphinx package. Because of this a separate 
installation is needed. ::
 
    $ sudo yum -y install python-pip
    $ sudo pip-python install sphinx_bootstrap_theme
 
For the generation of diagramms on-the-fly, the documentation uses 
`blockdiag`_ and `nwdiag`_ ::

    $ sudo easy_install sphinxcontrib-blockdiag
    $ sudo easy_install sphinxcontrib-nwdiag

For building the documentation locally, you need `Sphinx`_. ::

    $ sudo yum -y install python-sphinx python-docutils

If you want to build the documentation, switch to the *`docs`_* folder and
use `make` to build it. ::

    $ cd docs
    $ make html 

The latest `Documentation`_ is always available at `Read the Docs`_. After 
commit the changes to the git repository, `Read the Docs`_ rebuild the complete
documentation.
