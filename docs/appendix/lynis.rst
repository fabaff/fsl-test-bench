.. -*- mode: rst -*-

.. _appendix-lynis:

lynis
=====

The lynis output is from a virtual instance of a FSL Test bench.  ::

    [root@test-bench ~]# lynis --auditor "FSL Test bench" --check-all

    [ Lynis 1.5.0 ]

    ################################################################################
     Lynis comes with ABSOLUTELY NO WARRANTY. This is free software, and you are
     welcome to redistribute it under the terms of the GNU General Public License.
     See the LICENSE file for details about using this software.

     Copyright 2007-2014 - Michael Boelen, http://cisofy.com
     Enterprise support and plugins available via CISOfy - http://cisofy.com
    ################################################################################

    [+] Initializing program
    ------------------------------------
      - Detecting OS...                                           [ DONE ]
      - Clearing log file (/var/log/lynis.log)...                 [ DONE ]

      ---------------------------------------------------
      Program version:           1.5.0
      Operating system:          Linux
      Operating system name:     Fedora
      Operating system version:  Fedora release 20 (Heisenbug)
      Kernel version:            3.13.9-200.fc20.x86_64
      Hardware platform:         x86_64
      Hostname:                  test-bench
      Auditor:                   FSL Test bench
      Profile:                   /etc/lynis/default.prf
      Log file:                  /var/log/lynis.log
      Report file:               /var/log/lynis-report.dat
      Report version:            1.0
      Plugin directory:          /usr/share/lynis/plugins
      ---------------------------------------------------

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]

      - Checking profile file (/etc/lynis/default.prf)...
      - Program update status...                                  [ SKIPPED ]

    [+] System Tools
    ------------------------------------
      - Scanning available tools...
      - Checking system binaries...
        - Checking /bin...                                        [ FOUND ]
        - Checking /sbin...                                       [ FOUND ]
        - Checking /usr/bin...                                    [ FOUND ]
        - Checking /usr/sbin...                                   [ FOUND ]
        - Checking /usr/local/bin...                              [ FOUND ]
        - Checking /usr/local/sbin...                             [ FOUND ]
        - Checking /usr/local/libexec...                          [ FOUND ]
        - Checking /usr/libexec...                                [ FOUND ]
        - Checking /usr/sfw/bin...                                [ NOT FOUND ]
        - Checking /usr/sfw/sbin...                               [ NOT FOUND ]
        - Checking /usr/sfw/libexec...                            [ NOT FOUND ]
        - Checking /opt/sfw/bin...                                [ NOT FOUND ]
        - Checking /opt/sfw/sbin...                               [ NOT FOUND ]
        - Checking /opt/sfw/libexec...                            [ NOT FOUND ]
        - Checking /usr/xpg4/bin...                               [ NOT FOUND ]
        - Checking /usr/css/bin...                                [ NOT FOUND ]
        - Checking /usr/ucb...                                    [ NOT FOUND ]
        - Checking /usr/X11R6/bin...                              [ NOT FOUND ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Plugins (phase 1)
    ------------------------------------
      - Plugins enabled                                           [ NONE ]

    [+] Boot and services
    ------------------------------------
      - Checking boot loaders
        - Checking presence GRUB...                               [ NOT FOUND ]
        - Checking presence LILO...                               [ NOT FOUND ]
        - Checking boot loader SILO                               [ NOT FOUND ]
        - Checking boot loader YABOOT                             [ NOT FOUND ]
      - Check running services (systemctl)...                     [ DONE ]
            Result: found 31 running services
      - Check enabled services at boot (systemctl)...             [ DONE ]
            Result: found 35 enabled services
      - Check startup files (permissions)...                      [ OK ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Kernel
    ------------------------------------
      - Checking default runlevel...                              [ runlevel 3 ]
      - Checking CPU support (NX/PAE)
        CPU support: PAE and/or NoeXecute supported               [ FOUND ]
      - Checking kernel version and release                       [ DONE ]
      - Checking kernel type                                      [ DONE ]
      - Checking loaded kernel modules                            [ DONE ]
          Found 61 active modules
      - Checking Linux kernel configuration file                  [ FOUND ]
      - Checking default I/O kernel scheduler                     [ FOUND ]
      - Checking core dumps configuration...                      [ DISABLED ]
        - Checking setuid core dumps configuration...             [ DEFAULT ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Memory and processes
    ------------------------------------
      - Checking /proc/meminfo...                                 [ FOUND ]
      - Searching for dead/zombie processes...                    [ OK ]
      - Searching for IO waiting processes...                     [ OK ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Users, Groups and Authentication
    ------------------------------------
      - Search administrator accounts...                          [ OK ]
      - Checking for non-unique UIDs...                           [ OK ]
      - Checking consistency of group files (grpck)...            [ OK ]
      - Checking non unique group ID's...                         [ OK ]
      - Checking non unique group names...                        [ OK ]
      - Checking password file consistency...                     [ OK ]
      - Query system users (non daemons)...                       [ DONE ]
      - Checking NIS+ authentication support                      [ NOT ENABLED ]
      - Checking NIS authentication support                       [ NOT ENABLED ]
      - Checking sudoers file                                     [ FOUND ]
        - Check sudoers file permissions                          [ OK ]
      - Checking PAM password strength tools                      [ OK ]
      - Checking PAM configuration file (pam.conf)                [ NOT FOUND ]
      - Checking PAM configuration files (pam.d)                  [ FOUND ]
      - Checking PAM modules                                      [ FOUND ]
      - Checking user password aging                              [ DISABLED ]
      - Checking Linux single user mode authentication            [ WARNING ]
      - Determining default umask
        - Checking umask (/etc/profile)                           [ UNKNOWN ]
        - Checking umask (/etc/login.defs)                        [ OK ]
        - Checking umask (/etc/init.d/functions)                  [ SUGGESTION ]
      - Checking LDAP authentication support                      [ NOT ENABLED ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Shells
    ------------------------------------
      - Checking shells from /etc/shells...
        Result: found 6 shells (valid shells: 6).

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] File systems
    ------------------------------------
      - Checking mount points
        - Checking /home mount point...                           [ SUGGESTION ]
        - Checking /tmp mount point...                            [ OK ]
      - Checking LVM volume groups...                             [ FOUND ]
        - Checking LVM volumes...                                 [ FOUND ]
      - Checking for old files in /tmp...                         [ OK ]
      - Checking /tmp sticky bit...                               [ OK ]
      - ACL support root file system...                           [ ENABLED ]
      - Checking Locate database...                               [ NOT FOUND ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Storage
    ------------------------------------
      - Checking usb-storage driver (modprobe config)...          [ NOT DISABLED ]
    egrep: /etc/modprobe.d/*: No such file or directory
    egrep: /etc/modprobe.d/*: No such file or directory
      - Checking firewire ohci driver (modprobe config)...        [ NOT DISABLED ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] NFS
    ------------------------------------
      - Query rpc registered programs...                          [ DONE ]
      - Query NFS versions...                                     [ DONE ]
      - Query NFS protocols...                                    [ DONE ]
      - Check running NFS daemon...                               [ NOT FOUND ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Software: name services
    ------------------------------------
      - Checking default DNS search domain...                     [ NONE ]
      - Checking /etc/resolv.conf options...                      [ NONE ]
      - Searching DNS domain name...                              [ UNKNOWN ]
      - Checking nscd status...                                   [ NOT FOUND ]
      - Checking BIND status...                                   [ NOT FOUND ]
      - Checking PowerDNS status...                               [ NOT FOUND ]
      - Checking ypbind status...                                 [ NOT FOUND ]
      - Checking /etc/hosts
        - Checking /etc/hosts (duplicates)                        [ OK ]
        - Checking /etc/hosts (hostname)                          [ OK ]
        - Checking /etc/hosts (localhost)                         [ SUGGESTION ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Ports and packages
    ------------------------------------
      - Searching package managers...
        - Searching RPM package manager...                        [ FOUND ]
          - Querying RPM package manager...
      - Checking YUM package management consistency               [ OK ]
      - Checking package database duplicates...                   [ OK ]
      - Checking package database for problems...                 [ OK ]
      - Checking missing security packages                        [ SKIPPED ]
      - Checking GPG checks (yum.conf)                            [ DISABLED ]
      - Checking package audit tool...                            [ NONE ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Networking
    ------------------------------------
      - Checking configured nameservers...
        - Testing nameservers...
          Nameserver: 10.1.1.1...                                 [ SKIPPED ]
        - Minimal of 2 responsive nameservers...                  [ SKIPPED ]
      - Checking default gateway...                               [ DONE ]
      - Getting listening ports (TCP/TCP)...                      [ DONE ]
          * Found 16 ports
      - Checking promiscuous interfaces...                        [ OK ]
      - Checking waiting connections...                           [ OK ]
      - Checking status DHCP client...                            [ RUNNING ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Printers and Spools
    ------------------------------------
      - Checking cups daemon...                                   [ NOT FOUND ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Software: e-mail and messaging
    ------------------------------------
      - Checking Exim status...                                   [ NOT FOUND ]
      - Checking Postfix status...                                [ RUNNING ]
      - Checking Postfix configuration...                         [ FOUND ]
        - Checking Postfix banner...                              [ WARNING ]
      - Checking Dovecot status...                                [ RUNNING ]
      - Checking Qmail smtpd status...                            [ NOT FOUND ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Software: firewalls
    ------------------------------------
      - Checking iptables kernel module                           [ NOT FOUND ]
      - Checking iptables in config file                          [ FOUND ]
        - Checking for empty ruleset                              [ OK ]
        - Checking for unused rules                               [ WARNING ]
        Status pf                                                 [ NOT FOUND ]
      - Checking host based firewall                              [ ACTIVE ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Software: webserver
    ------------------------------------
      - Checking Apache...                                        [ NOT FOUND ]
      - Checking nginx...                                         [ NOT FOUND ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] SSH Support
    ------------------------------------
      - Checking running SSH daemon...                            [ FOUND ]
        - Searching SSH configuration...                          [ FOUND ]
        - Checking defined SSH options...                         [ DONE ]
        - SSH option: PermitRootLogin...                          [ DEFAULT ]
        - SSH option: Protocol...                                 [ DEFAULT ]
        - SSH option: StrictModes...                              [ DEFAULT ]
        - SSH option: AllowUsers...                               [ NOT FOUND ]
        - SSH option: AllowGroups...                              [ NOT FOUND ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] SNMP Support
    ------------------------------------
      - Checking running SNMP daemon...                           [ FOUND ]
        - Checking SNMP configuration...                          [ FOUND ]
      - Checking SNMP community strings...                        [ WARNING ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Databases
    ------------------------------------
      - MySQL process status...                                   [ NOT FOUND ]
      - PostgreSQL processes status...                            [ NOT FOUND ]
      - Oracle processes status...                                [ NOT FOUND ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] LDAP Services
    ------------------------------------
      - Checking OpenLDAP instance...                             [ NOT FOUND ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Software: PHP
    ------------------------------------
      - Checking PHP...                                           [ FOUND ]
        - Checking PHP disabled functions...                      [ NONE ]
        - Checking register_globals option...                     [ OK ]
        - Checking expose_php option...                           [ ON ]
        - Checking enable_dl option...                            [ OFF ]
        - Checking allow_url_fopen option...                      [ ON ]
        - Checking allow_url_include option...                    [ OFF ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Squid Support
    ------------------------------------
      - Checking running Squid daemon...                          [ NOT FOUND ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Logging and files
    ------------------------------------
      - Checking for a running log daemon...                      [ OK ]
        - Checking Syslog-NG status                               [ NOT FOUND ]
        - Checking Metalog status                                 [ NOT FOUND ]
        - Checking RSyslog status                                 [ NOT FOUND ]
        - Checking RFC 3195 daemon status                         [ NOT FOUND ]
        - Checking klogd                                          [ NOT FOUND ]
        - Checking minilogd instances                             [ NOT FOUND ]
      - Checking logrotate presence                               [ OK ]
      - Checking log directories (static list)                    [ DONE ]
      - Checking open log files                                   [ SKIPPED ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Insecure services
    ------------------------------------
      - Checking inetd status...                                  [ ACTIVE ]
        - Checking inetd.conf...                                  [ NOT FOUND ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Banners and identification
    ------------------------------------
      - /etc/motd...                                              [ FOUND ]
        - /etc/motd permissions...                                [ OK ]
        - /etc/motd contents...                                   [ WEAK ]
      - /etc/issue...                                             [ FOUND ]
        - /etc/issue contents...                                  [ WEAK ]
      - /etc/issue.net...                                         [ FOUND ]
        - /etc/issue.net contents...                              [ WEAK ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Scheduled tasks
    ------------------------------------
      - Checking crontab/cronjob                                  [ DONE ]
      - Checking atd status                                       [ NOT RUNNING ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Accounting
    ------------------------------------
      - Checking accounting information...                        [ NOT FOUND ]
      - Checking sysstat accounting data                          [ NOT FOUND ]
      - Checking auditd                                           [ ENABLED ]
        - Checking audit rules                                    [ SUGGESTION ]
        - Checking audit configuration file                       [ OK ]
        - Checking auditd log file                                [ FOUND ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Time and Synchronization
    ------------------------------------
      - Checking running NTP daemon (ntpd)...                     [ NOT FOUND ]
      - Checking running NTP daemon (timed)...                    [ NOT FOUND ]
      - Checking running NTP daemon (dntpd)...                    [ NOT FOUND ]
      - Checking NTP client in crontab file (/etc/anacrontab)...  [ NOT FOUND ]
      - Checking NTP client in crontab file (/etc/crontab)...     [ NOT FOUND ]
      - Checking NTP client in cron.d files...                    [ NOT FOUND ]
      - Checking for a running NTP daemon or client...            [ WARNING ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Cryptography
    ------------------------------------
      - Checking SSL certificate expiration...                    [ OK ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Virtualization
    ------------------------------------

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Security frameworks
    ------------------------------------
      - Checking presence AppArmor                                [ NOT FOUND ]
      - Checking presence SELinux                                 [ FOUND ]
        - Checking SELinux status                                 [ ENABLED ]
          - Checking current mode and config file                 [ OK ]
            Current SELinux mode: enforcing
      - Checking presence grsecurity                              [ NOT FOUND ]
      - Checking for implemented MAC framework                    [ OK ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Software: file integrity
    ------------------------------------
      - Checking file integrity tools...
        - AFICK...                                                [ NOT FOUND ]
        - AIDE...                                                 [ NOT FOUND ]
        - Osiris...                                               [ NOT FOUND ]
        - Samhain...                                              [ NOT FOUND ]
        - Tripwire...                                             [ NOT FOUND ]
        - OSSEC (syscheck)...                                     [ NOT FOUND ]
      - Checking presence integrity tool...                       [ NOT FOUND ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Software: Malware scanners
    ------------------------------------
      - Checking chkrootkit...                                    [ NOT FOUND ]
      - Checking Rootkit Hunter...                                [ NOT FOUND ]
      - Checking ClamAV scanner...                                [ NOT FOUND ]
      - Checking ClamAV daemon...                                 [ NOT FOUND ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] System Tools
    ------------------------------------
      - Starting file permissions check...
        /etc/lilo.conf                                            [ NOT FOUND ]
        /root/.ssh                                                [ OK ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Home directories
    ------------------------------------
      - Checking shell history files...                           [ OK ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Kernel Hardening
    ------------------------------------
      - Comparing sysctl key pairs with scan profile...
        - kernel.core_uses_pid (exp: 1)                           [ OK ]
        - kernel.ctrl-alt-del (exp: 0)                            [ OK ]
        - kernel.sysrq (exp: 0)                                   [ DIFFERENT ]
        - net.ipv4.conf.all.accept_redirects (exp: 0)             [ DIFFERENT ]
        - net.ipv4.conf.all.accept_source_route (exp: 0)          [ OK ]
        - net.ipv4.conf.all.bootp_relay (exp: 0)                  [ OK ]
        - net.ipv4.conf.all.forwarding (exp: 0)                   [ OK ]
        - net.ipv4.conf.all.log_martians (exp: 1)                 [ DIFFERENT ]
        - net.ipv4.conf.all.mc_forwarding (exp: 0)                [ OK ]
        - net.ipv4.conf.all.proxy_arp (exp: 0)                    [ OK ]
        - net.ipv4.conf.all.rp_filter (exp: 1)                    [ DIFFERENT ]
        - net.ipv4.conf.all.send_redirects (exp: 0)               [ DIFFERENT ]
        - net.ipv4.conf.default.accept_redirects (exp: 0)         [ DIFFERENT ]
        - net.ipv4.conf.default.accept_source_route (exp: 0)      [ OK ]
        - net.ipv4.conf.default.log_martians (exp: 1)             [ DIFFERENT ]
        - net.ipv4.icmp_echo_ignore_broadcasts (exp: 1)           [ OK ]
        - net.ipv4.icmp_ignore_bogus_error_responses (exp: 1)     [ OK ]
        - net.ipv4.tcp_syncookies (exp: 1)                        [ OK ]
        - net.ipv4.tcp_timestamps (exp: 0)                        [ DIFFERENT ]
        - net.ipv6.conf.all.accept_redirects (exp: 0)             [ DIFFERENT ]
        - net.ipv6.conf.all.accept_source_route (exp: 0)          [ OK ]
        - net.ipv6.conf.default.accept_redirects (exp: 0)         [ DIFFERENT ]
        - net.ipv6.conf.default.accept_source_route (exp: 0)      [ OK ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Hardening
    ------------------------------------
        - Installed compiler(s)...                                [ FOUND ]
        - Installed malware scanner...                            [ NOT FOUND ]

    [ Press [ENTER] to continue, or [CTRL]+C to stop ]


    [+] Custom Tests
    ------------------------------------
      - Running custom tests...                                   [ NONE ]

    ================================================================================

      -[ Lynis 1.5.0 Results ]-

      Tests performed: 173   Plugins enabled: 0

      Warnings:
      ----------------------------
      - No password set for single mode [AUTH-9308]
          http://cisofy.com/controls/AUTH-9308/

      - No GPG signing option found in yum.conf [PKGS-7387]
          http://cisofy.com/controls/PKGS-7387/

      - Found mail_name in SMTP banner, and/or mail_name contains 'Postfix' [MAIL-8818]
          http://cisofy.com/controls/MAIL-8818/

      - Found easy guessable SNMP community string [SNMP-3306]
          http://cisofy.com/controls/SNMP-3306/

      - PHP option expose_php is possibly turned on, which can reveal useful information for attackers. [PHP-2372]
          http://cisofy.com/controls/PHP-2372/

      - klogd is not running, which could lead to missing kernel messages in log files [LOGG-2138]
          http://cisofy.com/controls/LOGG-2138/


      Suggestions:
      ----------------------------
      - Run systemctl --full --type=service to see all services
          http://cisofy.com/controls/[22:30:27 Suggestion: Run systemctl --full --type=service to see all services/
      - Run systemctl list-unit-files --type=service to see all services
          http://cisofy.com/controls/[22:30:29 Suggestion: Run systemctl list-unit-files --type=service to see all services/
      - Configure password aging limits to enforce password changing on a regular base [AUTH-9286]
          http://cisofy.com/controls/AUTH-9286/
      - Set password for single user mode to minimize physical access attack surface [AUTH-9308]
          http://cisofy.com/controls/AUTH-9308/
      - To decrease the impact of a full /home file system, place /home on a separated partition [FILE-6310]
          http://cisofy.com/controls/FILE-6310/
      - The database required for 'locate' could not be found. Run 'updatedb' or 'locate.updatedb' to create this file. [FILE-6410]
          http://cisofy.com/controls/FILE-6410/
      - Disable drivers like USB storage when not used, to prevent unauthorized storage or data theft [STRG-1840]
          http://cisofy.com/controls/STRG-1840/
      - Disable drivers like firewire storage when not used, to prevent unauthorized storage or data theft [STRG-1846]
          http://cisofy.com/controls/STRG-1846/
      - Check DNS configuration [NAME-4028]
          http://cisofy.com/controls/NAME-4028/
      - Split resolving between localhost and the hostname of the system [NAME-4406]
          http://cisofy.com/controls/NAME-4406/
      - Install package yum-plugin-security if possible, to maintain security updates easier (yum install yum-plugin-security) [PKGS-7386]
          http://cisofy.com/controls/PKGS-7386/
      - Install a package audit tool to determine vulnerable packages [PKGS-7398]
          http://cisofy.com/controls/PKGS-7398/
      - You are adviced to hide the mail_name (option: smtpd_banner) from your postfix configuration. Use postconf -e or change your main.cf file (/etc/postfix/main.cf) [MAIL-8818]
          http://cisofy.com/controls/MAIL-8818/
      - Check iptables rules to see which rules are currently not used [FIRE-4513]
          http://cisofy.com/controls/FIRE-4513/
      - Harden PHP by disabling risky functions [PHP-2320]
          http://cisofy.com/controls/PHP-2320/
      - Change the expose_php line to: expose_php = Off [PHP-2372]
          http://cisofy.com/controls/PHP-2372/
      - Change the allow_url_fopen line to: allow_url_fopen = Off, to disable downloads via PHP [PHP-2376]
          http://cisofy.com/controls/PHP-2376/
      - Check why klogd is not running [LOGG-2138]
          http://cisofy.com/controls/LOGG-2138/
      - Add legal banner to /etc/motd, to warn unauthorized users [BANN-7122]
          http://cisofy.com/controls/BANN-7122/
      - Add a legal banner to /etc/issue, to warn unauthorized users [BANN-7126]
          http://cisofy.com/controls/BANN-7126/
      - Add legal banner to /etc/issue.net, to warn unauthorized users [BANN-7130]
          http://cisofy.com/controls/BANN-7130/
      - Enable sysstat to collect accounting (no results) [ACCT-9626]
          http://cisofy.com/controls/ACCT-9626/
      - Audit daemon is enabled with an empty ruleset. Disable the daemon or define rules [ACCT-9630]
          http://cisofy.com/controls/ACCT-9630/
      - Use NTP daemon or NTP client to prevent time issues. [TIME-3104]
          http://cisofy.com/controls/TIME-3104/
      - Install a file integrity tool [FINT-4350]
          http://cisofy.com/controls/FINT-4350/
      - One or more sysctl values differ from the scan profile and could be tweaked [KRNL-6000]
          http://cisofy.com/controls/KRNL-6000/
      - Harden the system by removing unneeded compilers. This can decrease the chance of customized trojans, backdoors and rootkits to be compiled and installed [HRDN-7220]
          http://cisofy.com/controls/HRDN-7220/
      - Harden compilers and restrict access to world [HRDN-7222]
          http://cisofy.com/controls/HRDN-7222/
      - Harden the system by installing one or malware scanners to perform periodic file system scans [HRDN-7230]
          http://cisofy.com/controls/HRDN-7230/

      Follow-up:
      ----------------------------
      - Fix findings, see security controls overview and documentation
      - Upload data to Lynis Enterprise for further analysis
      - Create a report and implementation plan

      Enterprise support and plugins available via CISOfy - http://cisofy.com
    ================================================================================
      Hardening index : [60]   [############        ]
    ================================================================================
      Files:
      - Test and debug information      : /var/log/lynis.log
      - Report data                     : /var/log/lynis-report.dat
    ================================================================================
      Tip: Disable all tests which are not relevant or are too strict for the
           purpose of this particular machine. This will remove unwanted suggestions
           and also boost the hardening index. Each test should be properly analyzed
           to see if the related risks can be accepted, before disabling the test.
    ================================================================================
      Lynis 1.5.0
      Copyright 2007-2014 - Michael Boelen, http://cisofy.com
    ================================================================================

