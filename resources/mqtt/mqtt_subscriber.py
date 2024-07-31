import ssl
import paho.mqtt.client as paho
import paho.mqtt.subscribe as subscribe
from paho import mqtt


# callback to print a message once it arrives
def print_msg(client, userdata, message):
    """
        Prints a mqtt message to stdout ( used as callback for subscribe )

        :param client: the client itself
        :param userdata: userdata is set when initiating the client, here it is userdata=None
        :param message: the message with topic and payload
    """
    print("%s : %s" % (message.topic, message.payload))
    #print(type(message.payload))


# use TLS for secure connection with HiveMQ Cloud
sslSettings = ssl.SSLContext(mqtt.client.ssl.PROTOCOL_TLS)

# put in your cluster credentials and hostname
auth = {'username': "phuong.ta", 'password': "PhamDiep1208"}
subscribe.callback(print_msg, "#", hostname="ff561b0054334ef6b26016f2463e72e8.s1.eu.hivemq.cloud", port=8883, auth=auth,
                   tls=sslSettings, protocol=paho.MQTTv31)