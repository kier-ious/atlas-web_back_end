// Import the redis library using ES6
import redis from 'redis';

// Create redis client
const client = redis.createClient();

// Handle server connectionn success
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle server connection errors
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});
