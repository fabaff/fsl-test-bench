# Fedora Security Lab Test bench
The Fedora Security Lab Test bench provides a save environment for
security auditing and testing and can be used for teaching security
testing methodologies. At the moment the focus lies on web applications.
All application are running on top of a current Fedora installation with
a ​Lighttpd webserver and a ​MySQL server. 

The Fedora Security Lab Test bench includes:

* Vulnerable web applications (DVWA, bWAPP, SQLI Labs, and SQLol)
* PHP shells (PHP Shell, ​b374k, and ​DNA Shell)
* Low-interaction honeypots
* ​Helper tools (Log viewer, CGIs, ​linfo, and ​phpmyadmin) 

All applications are directly accessible from a [bootstrap](http://twitter.github.io/bootstrap/)-based website. 

The FSL Test bench repository contains a subset of playbooks from the 
[**fedora-ansible** git repository](https://github.com/fabaff/fedora-ansible) 
maintained by [Fabian Affolter](http://fabian-affolter.ch). 

If you have just found Ansible or the Fedora Security Lab, you should start here:

 * [Fedora Security Lab](https://fedorahosted.org/security-spin/)

More details can be found at the [Fedora Security Lab Test bench](https://fedorahosted.org/security-spin/wiki/Test%20bench) page and the [Test bench](https://fedorahosted.org/security-spin/wiki/Test%20bench%20setup) setup page.

## Prerequisites
The setup of Ansible is explained on the
[Ansible Getting Started](http://ansible.cc/docs/gettingstarted.html) page.
Here is only the setup of the managed nodes and special details for the
management system covered. For every system you want to manage, you need to
have the client's SSH key in the *authorized_keys* file of the managed system
and Python.

### Packages
Make sure that [Python](http://www.python.org/) is installed. If not, install
the Python package on the managed node(s). If you have performed a minimal
Fedora installation Python is available.

```bash
yum -y install python
```
The playbooks are using DNF as package management software instead of yum.


### SSH key
Add the SSH key to the *authorized_keys* file. Assuming you are logged-in with
SSH on your 

```bash
sudo ssh-copy-id -i /root/.ssh/id_rsa.pub root@[IP address of your managed note]
```
### /etc/ansible/hosts
The file */etc/ansible/hosts* shall contain all hosts to be setup up.

- **fsl-tb**: Default group name for machine which uses the all-in-one playbook
- **fsl-tb-vpn**: Default group name for machine which acts as VPN servers
- **fsl-tb-master**: Hosts for FSL Test bench guests when using virtualization
- **fsl_hosts**: Host to install the Fedora Security Lab package set

### Variables
After cloning this git repository, edit the [variables/sensitive-variables.yml](https://github.com/fabaff/fsl-test-bench/blob/master/variables/sensitive-variables.yml) file if
you don't want to use *password* as default password.

## Documentation
The documentation is [here](http://fsl-test-bench.affolter-engineering.ch/) available.

## Structure
At the moment the structure of the repository looks like this:

```bash
.
├── all-in-one.yml ------- Fedora Security Lab Test bench on a single machine 
├── docs ----------------- Documentation
├── files ---------------- Template files
│   └── kickstart -------- kickstart files for the installation
├── fsl-packages-sync.py - Python script to sync with FSL package list
├── fsl.yml -------------- Package list for setup a Fedora Security Lab
├── handlers ------------- Handlers for services
├── INSTALL.md ----------- Installation guide
├── local-setup.yml ------ Local Fedora Security Test bench
├── openvpn-server.yml --- Fedora Security Lab VPN server
├── README.md ------------ This files
├── tasks ---------------- A collection of tasks
│   ├── apps ------------- Vulnerable web applications
│   ├── helpers ---------- Helper tools
│   ├── honeypots -------- Low-interaction honeypots
│   └── shells ----------- PHP shells
└── variables ------------ Storage files for variables
```
## Warning
The file *variables/sensitive-variables.yml* contains most application
passwords. If you don't want to run with default password, edit this file
according your needs and keep it save. 

## Licensing
All playbook content is assumed to be Creative Commons 3.0 Attribution licensed. 
Non-commerical or No-derivatives CC extensions are not acceptable, to encourage
easy use by all users, regardless of purpose.
