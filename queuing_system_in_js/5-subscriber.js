// Import the redis library using ES6
import redis from 'redis';

// Create redis client
const subscriber = redis.createClient();

// Handle server connectionn success
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle server connection errors
subscriber.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

subscriber.subscribe('holberton school channel');

subscriber.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
