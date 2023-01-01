class posture:
    # Set the transmission power of the headphones (in dBm)
    txPower = -60

    # Set the path loss exponent (between 2 and 4)
    n = 2.5

    def process_rssi(rssi):
        # Calculate the distance between the headphones and the device using the path loss formula
        distance = 10 ** ((txPower - rssi) / (10 * n))

    # Determine the posture based on the distance
        if distance < 0.5:
            posture = "slouching"
        else:
            posture = "good posture"   

        print("Posture: " + posture)