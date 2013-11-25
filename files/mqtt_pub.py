#!/usr/bin/python
#
# mqtt_pub.py - A simple script to send MQTT message.
#
# Copyright (c) 2013 Fabian Affolter <fabian@affolter-engineering.ch>
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
import datetime
import time
import random
import mosquitto

# Defaults value
message = "MQTT message from FSL Test Bench. Sent at "
topic = "fsl/testbench"

# Create a client for mosquitto
client = mosquitto.Mosquitto("python-client")
client.connect("127.0.0.1")

def sendMessage(topic, message):
    client.publish(topic, message, 1)

def main():
    while client.loop() == 0:
        # Wait for a random number of seconds
        r_int = random.randint(1, 30)
        time.sleep(r_int)
        # Get a timestamp
        timestamp = datetime.datetime.now()
        # Publish a message
        sendMessage(topic, (message + "%s" % timestamp))

if __name__ == "__main__":
    main()
