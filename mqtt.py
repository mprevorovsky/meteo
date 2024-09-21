import wifi
import socketpool
import ssl
import adafruit_minimqtt.adafruit_minimqtt as MQTT


def _mqtt_broker_connected(client, userdata, flags, rc):
    """
    Called when the client is connected successfully to the broker. 
    """

    print(f"Connected to MQTT broker!")


def _mqtt_broker_disconnected(client, userdata, rc):
    """
    Called when the client is disconnected from MQTT broker.
    """

    print("Disconnected from MQTT broker!")


def setup_mqtt_client(mqtt_ip, mqtt_port):
    """
    Create and set up an MQTT client
    """
    
    # Create a socket pool
    pool = socketpool.SocketPool(wifi.radio)
    ssl_context = ssl.create_default_context()
    
    # Set up a MiniMQTT Client
    mqtt_client = MQTT.MQTT(
        broker=mqtt_ip,
        port=mqtt_port,
        socket_pool=pool,
        ssl_context=ssl_context,
        )
    
    # Setup the callback methods
    mqtt_client.on_connect = _mqtt_broker_connected
    mqtt_client.on_disconnect = _mqtt_broker_disconnected

    return mqtt_client


def compose_mqtt_message():
    """

    """

    message = 0

    return message


def send_mqtt_message(mqtt_client, feed, message):
    """
    Publish MQTT message to the specified feed.
    """
    
    print("Sending message to MQTT broker...")
    mqtt_client.publish(feed, message, qos = 1)
    print("Message sent!")
