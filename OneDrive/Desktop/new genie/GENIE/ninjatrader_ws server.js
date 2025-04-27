const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8765 });

wss.on('connection', function connection(ws) {
  console.log('🔌 NinjaTrader WebSocket connected');

  ws.on('message', function incoming(message) {
    console.log('📩 received:', message);
    // Echo message back to sender
    ws.send(`✅ Message received: ${message}`);
  });

  // Initial welcome message
  ws.send('🧠 Connected to GENIE NinjaTrader WebSocket');
});
