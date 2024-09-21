import os
import ssl
import time

import socketpool
import wifi

import adafruit_minimqtt.adafruit_minimqtt as MQTT

print(f"Connecting to {os.getenv('CIRCUITPY_WIFI_SSID')}")
wifi.radio.connect(os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD"))
print(f"Connected to {os.getenv('CIRCUITPY_WIFI_SSID')}!")

### Feeds ###

# Setup a feed named 'temperature' for publishing to a feed
temperature_feed = "greenhouse/temperature"

# Setup a feed named 'onoff' for subscribing to changes
onoff_feed = "greenhouse/onoff"

### Code ###


# Define callback methods which are called when events occur
def connected(client, userdata, flags, rc):
    # This function will be called when the client is connected
    # successfully to the broker.
    print(f"Connected to Mosquitto! Listening for topic changes on {onoff_feed}")
    # Subscribe to all changes on the onoff_feed.
    client.subscribe(onoff_feed)


def disconnected(client, userdata, rc):
    # This method is called when the client is disconnected
    print("Disconnected from Mosquitto!")


def message(client, topic, message):
    # This method is called when a topic the client is subscribed to
    # has a new message.
    print(f"New message on topic {topic}: {message}")


# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)
ssl_context = ssl.create_default_context()

# If you need to use certificate/key pair authentication (e.g. X.509), you can load them in the
# ssl context by uncommenting the lines below and adding the following keys to your settings.toml:
# "device_cert_path" - Path to the Device Certificate
# "device_key_path" - Path to the RSA Private Key
# ssl_context.load_cert_chain(
#     certfile=os.getenv("device_cert_path"), keyfile=os.getenv("device_key_path")
# )

# Set up a MiniMQTT Client
mqtt_client = MQTT.MQTT(
    broker="192.168.1.112",
    port=1883,
    #username=aio_username,
    #password=aio_key,
    socket_pool=pool,
    ssl_context=ssl_context,
)

# Setup the callback methods above
mqtt_client.on_connect = connected
mqtt_client.on_disconnect = disconnected
mqtt_client.on_message = message

# Connect the client to the MQTT broker.
print("Connecting to Mosquitto...")
mqtt_client.connect()

temperature_val = 0
while True:
    # Poll the message queue
    mqtt_client.loop(timeout=1)

    # Send a new message
    print(f"Sending temperature value: {temperature_val}...")
    mqtt_client.publish(temperature_feed, temperature_val)
    print("Sent!")
    temperature_val += 1
    time.sleep(5)
