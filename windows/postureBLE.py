import pywinbluetooth

# Get the name of the Bluetooth device
bd_name = "MyDevice"

# Create a BluetoothDeviceQuery object and search for available devices
device_query = pywinbluetooth.BluetoothDeviceQuery()
device_query.name = bd_name
devices = device_query.find_devices()

# Find the device with the matching name
device = None
for dev in devices:
    if dev.name == bd_name:
        device = dev
        break

if device is not None:
    # Create a BluetoothLEDevice object and connect to the device
    device = pywinbluetooth.BluetoothLEDevice(device.address)
    device.connect()

    # Create a BluetoothSignalStrengthFilter object and start the RSSI reading
    signal_strength_filter = device.create_signal_strength_filter()
    signal_strength_filter.start_reading_rssi()

    # Read the RSSI value
    rssi = signal_strength_filter.read_rssi()

    # Stop the RSSI reading and close the device
    signal_strength_filter.stop_reading_rssi()
    device.close()

    print(f"RSSI: {rssi}")
else:
    print("Device not found")
