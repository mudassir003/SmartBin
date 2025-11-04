# Smart Bin Dashboard

A Progressive Web App (PWA) for real-time monitoring of smart waste bins using MQTT and ultrasonic sensors.

## Features

- **Real-time Monitoring**: Connects to MQTT broker to receive live bin fill levels
- **Visual Dashboard**: Animated gauge showing fill percentage with color-coded alerts
- **PWA Support**: Installable on mobile devices with offline caching
- **Alert System**: Notifications and sound alerts when bin reaches 75% capacity
- **Responsive Design**: Works on desktop and mobile devices

## Technologies Used

- HTML5, CSS3, JavaScript
- Paho MQTT Client for WebSocket connections
- Service Worker for offline functionality
- Web App Manifest for PWA installation

## Deployment

This project is configured for easy deployment on Netlify:

1. Connect your GitHub repository to Netlify
2. Deploy automatically - no build step required
3. The `netlify.toml` and `_redirects` files handle SPA routing

## Local Development

1. Clone the repository
2. Start a local server: `python -m http.server 8000`
3. Open `http://localhost:8000` in your browser

## MQTT Configuration

- Broker: `broker.hivemq.com`
- Port: `8000` (WebSocket)
- Topic: `smartbin/office1/level`
- Payload format: `{"fill_pct": 50, "distance_cm": 120, "ip": "192.168.1.100"}`

## File Structure

```
├── index.html          # Main dashboard
├── manifest.json       # PWA manifest
├── service-worker.js   # Offline caching
├── paho-mqtt.js        # MQTT client library
├── alert.mp3           # Alert sound
├── icons/              # PWA icons
├── netlify.toml        # Netlify configuration
├── _redirects          # SPA routing for Netlify
└── README.md           # This file
```

## License

MIT License
