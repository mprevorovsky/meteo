import wifi
import socketpool
import ssl
import adafruit_minimqtt.adafruit_minimqtt as MQTT


# Define callback methods which are called when events occur
def mqtt_broker_connected(client, userdata, flags, rc):
    # This function will be called when the client is connected
    # successfully to the broker.
    print(f"Connected to MQTT broker!")


def mqtt_broker_disconnected(client, userdata, rc):
    # This method is called when the client is disconnected
    print("Disconnected from MQTT broker!")


# Define creation and setup of MQTT client
def setup_mqtt_client(mqtt_ip, mqtt_port):
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
    mqtt_client.on_connect = mqtt_broker_connected
    mqtt_client.on_disconnect = mqtt_broker_disconnected
    return mqtt_client
