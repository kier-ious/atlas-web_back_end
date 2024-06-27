// Import the redis library using ES6
import redis from 'redis';

// Create redis client
const publisher = redis.createClient();

// Handle server connectionn success
publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle server connection errors
publisher.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

// subscriber.subscribe('holberton school channel');

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish('holberton school channel', message);
  }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
