// Import the redis library using ES6
import redis from 'redis';
import { promisify } from 'util';

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

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  const value = await getAsync(schoolName);
  console.log(value);
}

// Function to set a new school name and value
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
