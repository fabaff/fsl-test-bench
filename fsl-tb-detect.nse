local http = require "http"
local shortport = require "shortport"
local string = require "string"

description = [[
Checks for the FSL Test Bench web interface.
]]

author = "Fabian Affolter"
license = "Same as Nmap--See http://nmap.org/book/man-legal.html"
categories = {"discovery", "safe"}

---
-- @usage
-- nmap --script fsl-tb-detect <host>
--
--@output
-- Nmap scan report for testbench01.lab-ex.security (10.0.0.64)
-- PORT   STATE SERVICE
-- 80/tcp open  http
-- |_fsl-tb-detect: Fedora Security Lab Test bench Web interface FOUND.

-- Changelog:
-- 2013-05-09 Fabian Affolter <fabian@affolter-engineering.ch>:
--   + initial release
-- 2014-02-22 Fabian Affolter <fabian@affolter-engineering.ch>:
--   + update @usage

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
