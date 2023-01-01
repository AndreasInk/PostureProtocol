import bluetooth

# Get the name of the Bluetooth device
bd_name = "Andreas's AirPods Pro"

# Search for available devices
nearby_devices = bluetooth.discover_devices()

# Find the device with the matching name
bd_addr = None
for addr in nearby_devices:
    if bluetooth.lookup_name(addr) == bd_name:
        bd_addr = addr
        break

if bd_addr is not None:
    # Create a socket and connect to the device
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, 1))

    # Send the "RSSI" command to the device
    sock.send("RSSI")

    # Receive the response from the device
    response = sock.recv(1024)

    # Parse the RSSI value from the response
    rssi = int(response.split(":")[1])

    # Close the socket
    sock.close()

    print(f"RSSI: {rssi}")
else:
    print("Device not found")