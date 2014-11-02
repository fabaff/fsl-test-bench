.. _MariaDB: https://mariadb.org/
.. _MySQL: http://www.mysql.com/
.. _mongoDB: http://www.mongodb.org/
.. _Sqlite: http://www.sqlite.org/

.. _services-db:

Database server
===============
The `MariaDB`_ database engine is used for the web applications but it is still
possible to misuse it for your own requirements. All current available DBMS are
accessible by remote systems with client tools. For management or administration
tasks web interfaces are provided, please check the ``Misc`` section on the
default start page of your FSL Test bench.

* `MariaDB`_
* `MySQL`_ (replaced by MariaDB)
* `mongoDB`_
* `Sqlite`_

If you want to interact with the `mongoDB`_ instance, make your that you have
the client tools installed on your system. ::

    $ mongo testbench --host 10.0.0.64
