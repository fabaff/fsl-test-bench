# Testing
This document describe some basic steps to check if the Fedora Security Lab Test
bench is properly setup and working.

## Ansible
A simple test to check if Ansible is ready to work. Execute the command 
mentined below from the management system. 

```bash
$ sudo ansible [IP address of the FSL Test bench] -m setup
```
If you get an authentication failure like the one shown below

```bash
10.0.0.64 | FAILED => FAILED: Authentication failed.
```
Means this that the SSH key is not present in the *authorized_keys* file of
your future Fedora Security Lab Test bench. 

From the managed node:
```bash
ssh root@[IP address of your management system] 'cat ~/.ssh/id_rsa.pub' | cat - >> ~/.ssh/authorized_keys
```
From the management system:
```bash
sudo ssh-copy-id -i /root/.ssh/id_rsa.pub root@[IP address of your management system]
```
Assuming that you already have an SSH key on your server.
```bash
sudo ssh-keygen -t rsa
```
## Logging
The system log (aka */var/log/messages*) is viewable on the web interface of
the Fedora Security Lab Test bench. To check if the web interface is working
proberly, send a message to the logging system. 

Open two terminals and connect over SSH with the Fedora Security Lab Test 
bench. In one terminal execute the command from below to display the lastest
log entries:

```bash
sudo journalctl -f
```
In the second terminal, send a message: 

```bash
$ logger This is a test entry. To test the FSL Test bench log viewer.
```
The entry from above should now be visible in your browser's textarea of the
System Log (http://[IP address of the FSL test bench]/log-system/) page.
