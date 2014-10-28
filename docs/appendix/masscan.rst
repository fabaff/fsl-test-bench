.. _appendix-masscan:

masscan
=======
The nmap output below shows the view of the Test bench from the network side. ::

    $ sudo masscan -p0-65535 10.0.0.64

    Starting masscan 1.0.3 (http://bit.ly/14GZzcT) at 2014-10-28 08:45:22 GMT
     -- forced options: -sS -Pn -n --randomize-hosts -v --send-eth
    Initiating SYN Stealth Scan
    Scanning 1 hosts [65536 ports/host]
    Discovered open port 23/tcp on 10.0.0.64                                       
    Discovered open port 25/tcp on 10.0.0.64                                       
    Discovered open port 8880/tcp on 10.0.0.64                                     
    Discovered open port 21/tcp on 10.0.0.64                                       
    Discovered open port 8000/tcp on 10.0.0.64                                     
    Discovered open port 8889/tcp on 10.0.0.64                                     
    Discovered open port 8887/tcp on 10.0.0.64                                     
    Discovered open port 3389/tcp on 10.0.0.64                                     
    Discovered open port 993/tcp on 10.0.0.64                                      
    Discovered open port 22/tcp on 10.0.0.64                                       
    Discovered open port 27017/tcp on 10.0.0.64                                    
    Discovered open port 222/tcp on 10.0.0.64                                      
    Discovered open port 8888/tcp on 10.0.0.64                                     
    Discovered open port 80/tcp on 10.0.0.64                                       
    Discovered open port 110/tcp on 10.0.0.64                                      
    Discovered open port 995/tcp on 10.0.0.64                                      
    Discovered open port 8080/tcp on 10.0.0.64

