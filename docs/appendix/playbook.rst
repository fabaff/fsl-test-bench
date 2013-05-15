.. -*- mode: rst -*-

.. _appendix-playbook:

Playbook
========

The **all-in-one.yml** contains all items which are installed on the FSL Test
bench. This should give the reader a bit of an inside view of the creation
workflow of the Fedora Security Lab Test bench. This playbook calls every 
include playbook which contains the tasks for the service it represents. ::

    # This playbook contains all tasks to perform on a fresh Fedora installation to
    # create a Fedora Security Lab Test bench.
    #
    # Copyright (c) 2013 Fabian Affolter <fabian@affolter-engineering.ch>
    #
    # Licensed under CC BY 3.0. All rights reserved.
    #
    ---
    - hosts: fsl-tb
      user: root
      vars_files:
        - variables/application-versions.yml
        - variables/sensitive-variables.yml

      tasks:
    # Common tasks
        - include: tasks/preparation.yml
        - include: tasks/motd-hhs.yml
        - include: tasks/hosts-hhs.yml
        - include: tasks/users.yml

    # Services
        - include: tasks/web-servers/lighttpd.yml
        - include: tasks/web-servers/nginx.yml
        - include: tasks/web-servers/tomcat.yml
        - include: tasks/web-servers/pywebserve.yml
        - include: tasks/web-servers/nodejs.yml
        - include: tasks/db-servers/mysql.yml
        - include: tasks/ftp-servers/vsftpd.yml
        - include: tasks/dropbear.yml
        - include: tasks/file-servers/tftp.yml
        - include: tasks/telnet.yml
        - include: tasks/cups.yml
        - include: tasks/file-servers/samba.yml
        - include: tasks/file-servers/nfs.yml
        - include: tasks/openvpn-static.yml
        - include: tasks/mail-servers/postfix.yml
        - include: tasks/mail-servers/dovecot.yml

    # HHS Test bench specific stuff
        - include: tasks/website-hhs.yml

    # Helpers
        - include: tasks/helpers/log-system.yml
        - include: tasks/helpers/cgi.yml
        - include: tasks/helpers/phpinfo.yml
        - include: tasks/helpers/php-shell-detector.yml
        - include: tasks/helpers/linfo.yml
        - include: tasks/helpers/phpmyadmin.yml

    # Vulnerable Web Application
        - include: tasks/apps/sqlol.yml
        - include: tasks/apps/sqli.yml
        - include: tasks/apps/bwapp.yml
        - include: tasks/apps/dvwa.yml
        - include: tasks/apps/hackademic.yml
        - include: tasks/apps/xssed.yml

    # Honeypots
        - include: tasks/honeypots/honeyd.yml

    # Shells
        - include: tasks/shells/b374k.yml
        - include: tasks/shells/dnashell.yml
        - include: tasks/shells/phpshell.yml
        - include: tasks/shells/ajaxshell.yml

    # Common tasks
    #    - include: tasks/cleanup.yml

      handlers:
       - include: handlers/system.yml
       - include: handlers/services.yml
