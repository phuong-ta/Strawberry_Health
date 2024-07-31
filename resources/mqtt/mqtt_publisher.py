import ssl
from paho import mqtt
import paho.mqtt.client as paho
import paho.mqtt.publish as publish

def publish_msg(cam_id, msg):
    # create a set of 2 test messages that will be published at the same time
    #msgs = [{'topic': "strawberry/cam1", 'payload': "moikka"}, ("strawberry/cam2", "hello"), ("strawberry/cam3", "ciao")]
    msgs = [{'topic': f"strawberry/{cam_id}", 'payload': msg}]

    # use TLS for secure connection with HiveMQ Cloud
    sslSettings = ssl.SSLContext(mqtt.client.ssl.PROTOCOL_TLS)

    # put in your cluster credentials and hostname
    auth = {'username': "phuong.ta", 'password': "PhamDiep1208"}
    publish.multiple(msgs, hostname="ff561b0054334ef6b26016f2463e72e8.s1.eu.hivemq.cloud", port=8883, auth=auth,
                    tls=sslSettings, protocol=paho.MQTTv31)