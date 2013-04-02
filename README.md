# Fedora Security Lab Test bench - Ansible Contrib Repository

The Fedora Security Lab Test bench provides a save environment for
security auditing and testing and can be used for teaching security
testing methodologies. At the moment the focus lies on web applications.
All application are running on top of a current Fedora installation with
a ​Lighttpd webserver and a ​MySQL server. 

The Fedora Security Lab Test bench includes:

* Vulnerable web applications (DVWA, bWAPP, SQLI Labs, and SQLol)
* Shells (PHP Shell, ​b374k, ​Ani-Shell, and ​WSO PHP Shell)
* ​Helper tools (PHP Shell detector, ​linfo, and ​phpmyadmin) 

All applications are directly accessible from a bootstrap-based website. 

The FSL Test bench repository contains a subset of playbooks from the 
[**fedora-ansible** git repository](https://github.com/fabaff/fedora-ansible) maintained by [Fabian Affolter](http://fabian-affolter.ch). 

If you have just found Ansible or the Fedora Security Lab, you should start here:

 * [Fedora Security Lab](https://fedorahosted.org/security-spin/)
 * [Ansible project](https://github.com/ansible/ansible)

More details can be found at the [Fedora Security Lab Test bench](https://fedorahosted.org/security-spin/wiki/Test%20bench) page and the [Test bench](https://fedorahosted.org/security-spin/wiki/Test%20bench%20setup) setup page.

## Prerequisites

The setup of Ansible is explained in the on the [Ansible Getting Started](http://ansible.cc/docs/gettingstarted.html) page. Here is only the setup of the managed nodes covered. For every system you want to 
manage, you need to have the client's SSH key in the *authorized_keys* file of
the management system and Python.

Make sure that [Python](http://www.python.org/) is installed. If not, install
the Python package.

```bash
yum -y install python
```
Add the SSH key to the *authorized_keys* file.

```bash
ssh root@10.0.0.11 'cat ~/.ssh/id_rsa.pub' | cat - >> ~/.ssh/authorized_keys
```

## Structure

At the moment the structure of the repository looks like this:

```bash
.
├── files ----------- Template files
├── handlers -------- Handlers for services
├── maintenance ----- Complete playbooks
├── maintenance.yml - Regular tasks to perform on a running system
├── README.md ------- This files
├── tasks ----------- A collection of tasks
├── setup.yml ------- Collected tasks for a fresh installed system
└── variables ------- Storage files for variables
```

## Warning
The file *variables/sensitive-variables.yml* contains most application
passwords. If you don't want to run with default password, edit this file
according your needs and keep it save. 

## Licensing
All playbook content is assumed to be Creative Commons 3.0 Attribution licensed. 
Non-commerical or No-derivatives CC extensions are not acceptable, to encourage
easy use by all users, regardless of purpose.
