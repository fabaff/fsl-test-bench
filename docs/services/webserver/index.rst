.. -*- mode: rst -*-

.. _services-webserver:

.. _Fedora: https://fedoraproject.org

Web servers
===========

Every type of web server has its purpose and its unique fingerprint. To give
the students the feeling of the real world, various web servers are running.
They don’t serve content, they are just lurking around for fingerprinting and
bannergrabbing. The following web server are available.

.. toctree::
   :maxdepth: 2

   *

To run all web servers on one machine it's needed that they use different
ports. Table below shows the ports and the assigned web server.

+------------+----------------+
| Port       | Server         |
+============+================+
| 80         | lighttpd       |
+------------+----------------+
| 8000       | droopy         |
+------------+----------------+
| 8008       | cherokee       |
+------------+----------------+
| 8080       | tomcat         |
+------------+----------------+
| 8800       | apache         |
+------------+----------------+
| 8808       | nginx          |
+------------+----------------+
| 8880       | pywebserve     |
+------------+----------------+
| 8888       | http-server    |
+------------+----------------+
| 8889       | mongoose       |
+------------+----------------+
| 8887       | darkhttpd      |
+------------+----------------+
| 8886       | flask          |
+------------+----------------+

At the moment most web servers doesn't support https. This is a task for
the future. The only web server with SSL support is `nginx`_.
