# Web servers

Nowadays there are a couple of web servers around for Linux. 'apache', 'nginx',
and 'lighttpd' just to name the most popular. Every type of web server has its
purpose and its unique fingerprint. The following web server are available for 
a Fedora Security Test bench setup:

* [lighttpd](http://www.lighttpd.net/)
* [apache](http://httpd.apache.org/) (not ready)
* [cherokee](http://cherokee-project.com/) (not ready)
* [nginx](http://nginx.org/)
* [tomcat](http://tomcat.apache.org/index.html)
* [droopy](http://gitorious.org/droopy)
* [pywebserve](http://gitorious.org/pywebserve)
* [node.js](http://nodejs.org/)

# Ports assignment
To run all webserver on one machine it's needed that they use different ports.
Below you find a listing with the port the assigned web server.

| Port     | Server                   |
|:--------:|:-------------------------|
| **80**   | lighttpd |
| **8000** | droopy |
| **8008** | cherokee |
| **8080** | tomcat |
| **8800** | apache |
| **8088** | nginx |
| **8880** | pywebserve |
| **8888** | node.js |

# Load balancing
In high traffic environments it's common that webservers are placed behind a
load balancer. This give a different impression of the infrastructure while 
doing reconnaissance.

```bash
                             +----------------+
                         +-->| Webserver 1    |
    +-----------------+  |   |                |
    | Loadbalancer    |--+   +----------------+
 -->|                 |--+
    +-----------------+  |   +----------------+
                         |   | Webserver 2    |
                         +-->|                |
                             +----------------+
```
This will be added soon...
