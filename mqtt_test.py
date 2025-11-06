#!/usr/bin/env python3
"""
MQTT Test Script for Smart Bin Dashboard
Simulates ESP8266/ESP32 publishing sensor data to MQTT broker
"""

import paho.mqtt.client as mqtt
import json
import time
import random

# MQTT Configuration
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "smartbin/office1/level"
CLIENT_ID = f"test_publisher_{random.randint(1000, 9999)}"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ Connected to MQTT broker")
    else:
        print(f"❌ Connection failed with code {rc}")

def simulate_sensor_data():
    """Simulate realistic sensor readings"""
    # Fixed data to trigger alert at 80%
    distance = 30  # 80% full
    fill_percentage = 80

    return {
        "distance_cm": round(distance, 1),
        "fill_pct": round(fill_percentage, 1),
        "ip": "192.168.1.100"  # Simulated IP
    }

def main():
    print("🚀 Starting MQTT Test Publisher")
    print(f"📡 Broker: {BROKER}:{PORT}")
    print(f"📝 Topic: {TOPIC}")
    print("-" * 50)

    # Create MQTT client with callback API version
    client = mqtt.Client(client_id=CLIENT_ID, callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect

    try:
        # Connect to broker
        print("🔌 Connecting to broker...")
        client.connect(BROKER, PORT, 60)
        client.loop_start()

        print("📊 Publishing test data...")

        # Generate sensor data
        data = simulate_sensor_data()

        # Convert to JSON
        payload = json.dumps(data)

        # Publish to topic
        client.publish(TOPIC, payload)

        # Print status
        print(f"📤 Published: Distance={data['distance_cm']}cm, Fill={data['fill_pct']}%")

        # Wait a bit for delivery
        time.sleep(1)

    except KeyboardInterrupt:
        print("\n🛑 Stopping publisher...")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        client.loop_stop()
        client.disconnect()
        print("👋 Disconnected from broker")

if __name__ == "__main__":
    main()
