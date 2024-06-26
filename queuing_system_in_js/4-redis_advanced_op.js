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

const schools = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2
};

for (const [city, value] of Object.entries(schools)) {
  client.hset('HolbertonSchools', city, value, redis.print);
}

client.hgetall('HolbertonSchools', (err, reply) => {
  console.log(reply);
});
