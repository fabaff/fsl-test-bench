#!/usr/bin/python
#
# fsl-packages-sync - A helper script to sync the Fedora Security Lab package
# list with the origin list from https://fedorahosted.org/security-spin/
#
# Copyright (c) 2013-2018 Fabian Affolter <fabian@affolter-engineering.ch>
#
# All rights reserved.
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc.,
# 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
import urllib
import operator
import itertools
import datetime
import sys
import os
try:
    import git
except ImportError:
    print "Please install GitPython first -> sudo dnf -y install python3-GitPython"
try:
    import yaml
except ImportError:
    print "Please install PyYAML first -> sudo dnf -y install PyYAML"


urllib.urlretrieve('https://pagure.io/security-lab/raw/master/f/pkglist.yaml', 'pkglist.yaml')
repo = git.Repo(os.getcwd())

def playbook_sync():
    """
    Generates a Ansible playbook for the installation of the Fedora Security
    Lab packages.
    """
    file = open('pkglist.yaml', 'r') 
    pkgslist = yaml.safe_load(file)
    file.close()

    part1 = """# This playbook install all packages for the Fedora Security Lab.
#
# Copyright (c) 2013-2018 Fabian Affolter <fabian@affolter-engineering.ch>
#
# Licensed under CC BY 3.0. All rights reserved. 
#
# Synced at %s
#
---
- hosts: fsl_hosts
  user: root
  tasks:
  - name: install $item
    action: yum pkg=$item state=installed
    with_items:\n""" % (datetime.date.today())

    # Split list of packages into eincluded and excluded packages
    sorted_pkgslist = sorted(pkgslist, key=operator.itemgetter('pkg'))

    # Write the playbook files
    fileOut = open('fsl.yml','w')
    fileOut.write(part1)
    for pkg in sorted_pkgslist:
        fileOut.write('       - %s\n' %  pkg['pkg'])
    fileOut.close()

    # Commit the changed file to the repository
    repo.git.add('fsl.yml')
    repo.git.commit(m="Synced playbook with origin from https://pagure.io/security-lab")
    repo.git.push()

    # Remove the pkglist.yaml file
    os.remove('pkglist.yaml')

if __name__ == '__main__':
    playbook_sync()
