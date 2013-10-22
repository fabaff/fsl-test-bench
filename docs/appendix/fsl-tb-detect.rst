.. -*- mode: rst -*-

.. _appendix-fsl-tb-detect:

.. _nmap: http://nmap.org/
.. _script: https://github.com/fabaff/fsl-test-bench/blob/master/fsl-tb-detect.nse
.. _git repository: https://github.com/fabaff/fsl-test-bench

fsl-tb-detect
=============

The ``fsl-tb-detect`` script makes it possible to check your network for Fedora
Security Lab Test Bench Web interfaces which leads to the conclusion that the 
Fedora Security Lab Test bench is available on those systems. The script is 
pretty simple: It is looking for the string "Fedora Security Lab Test Bench"
in the meta data of any html files provided by a web server.

    local http = require "http"
    local shortport = require "shortport"
    local string = require "string"

    description = [[
    Checks for the Fedora Security Lab Test Bench web interface.
    ]]

    author = "Fabian Affolter"
    license = "Same as Nmap--See http://nmap.org/book/man-legal.html"
    categories = {"discovery", "safe"}

    ---
    -- @usage
    -- nmap --script fsl-detect <host>
    --
    --@output
    -- Nmap scan report for testbench01.lab-ex.security (10.0.0.64)
    -- PORT   STATE SERVICE
    -- 80/tcp open  http
    -- |_fsl-tb-detect: Fedora Security Lab Test bench Web interface FOUND.

    -- Changelog:
    -- 2013-05-09 Fabian Affolter  <fabian@affolter-engineering.ch>:
    --   + initial release

    portrule = shortport.http

    action = function(host, port)
        local resp, title
        resp = http.get( host, port, '/' )
        title = string.match(resp.body, "<[Tt][Ii][Tt][Ll][Ee][^>]*>([^<]*)</[Tt][Ii][Tt][Ll][Ee]>")
        if string.find(title, "Fedora Security Lab Test bench") then
            title = "Fedora Security Lab Test bench Web interface FOUND."
	    else
            title = "Fedora Security Lab Test bench Web interface NOT found."
        end
        return title
    end

Run the script against your network.

    $ sudo nmap --script=./fsl-tb-detect.nse 10.0.0.0/24

    Starting Nmap 6.40 ( http://nmap.org ) at 2013-10-22 09:12 CEST

    Nmap scan report for config01.lax-ex.network (10.0.0.30)
    Host is up (0.0056s latency).
    PORT   STATE SERVICE
    80/tcp open  http
    |_fsl-tb-detect: Fedora Security Lab Test bench Web interface NOT found.
    MAC Address: 54:54:44:47:C6:78 (QEMU Virtual NIC)

    Nmap scan report for testbench01.lab-ex.network (10.0.0.64)
    Host is up (0.0048s latency).
    PORT   STATE SERVICE
    80/tcp open  http
    |_fsl-tb-detect: Fedora Security Lab Test bench Web interface FOUND.
    MAC Address: 54:54:44:21:14:01 (Unknown)

    Nmap scan report for testbench02.lab-ex.network (10.0.0.65)
    Host is up (0.0053s latency).
    PORT   STATE    SERVICE
    80/tcp filtered http
    MAC Address: 54:54:00:D3:D2:02 (Unknown)

    Nmap done: 256 IP addresses (13 hosts up) scanned in 2.06 seconds


The `script`_ can be found in the FSL Test bench `git repository`_.
