.. _MQTT: http://mqtt.org/
.. _mosquitto: http://mosquitto.org/

.. _services-misc-mosquitto:

mosquitto
=========
`mosquitto`_ is a MQ Telemetry Transport (`MQTT`_) message broker. The MQTT
protocol provides a lightweight method of carrying out messaging using a
publish/subscribe model. It is useful and suitable for "machine to machine" 
messaging in various way, e. g. for connections with remote locations or just
to collect your data from a microcontroller system.

Subscribing to the topic **fsl/testbench** of the `MQTT`_ broker from your
local machine::

    $ mosquitto_sub -h 10.0.0.65 -d -t fsl/testbench
    Client mosqsub/24366-laptop011 sending CONNECT
    Client mosqsub/24366-laptop011 received CONNACK
    Client mosqsub/24366-laptop011 sending SUBSCRIBE (Mid: 1, Topic: fsl/testbench, QoS: 0)
    Client mosqsub/24366-laptop011 received SUBACK
    Subscribed (mid: 1): 0

The FSL Test Bench is publishing permanently messages. The default string
contains **MQTT message from FSL Test Bench.** and a time stamp.

Manually publishing messages on your FSL Test bench can be done with the topic
**fsl/testbench**. If you want to publish the message directly from your FSL 
Test Bench, use the command mentioned below::

    $ mosquitto_pub -d -t fsl/testbench -m "This is a message from your FSL Test bench"
    Client mosqpub/20531-test-bench sending CONNECT
    Client mosqpub/20531-test-bench received CONNACK
    Client mosqpub/20531-test-bench sending PUBLISH (d0, q0, r0, m1, 'fsl/testbench', ... (42 bytes))
    Client mosqpub/20531-test-bench sending DISCONNECT

If you want to pusblish a message from your local machine, the broker's IP
address is needed additionally.::

    $ mosquitto_pub -h 10.0.0.65 -d -t fsl/testbench -m "This is a message from your FSL Test bench"

You should now get the message from the FSL Test Bench. ::

    Client mosqsub/24366-laptop011 received PUBLISH (d0, q0, r0, m0, 'fsl/testbench', ... (42 bytes))
    This is a message from your FSL Test bench

