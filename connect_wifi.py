import wifi


def connect_wifi(ssid, password):
    """
    Connect to WiFi network using the supplied cretentials.
    """
    
    print(f"Connecting to {ssid}")
    wifi.radio.connect(ssid, password)
    print(f"Connected to {ssid}!")
