import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('connect', async () => {
  console.log('Redis client connected to the server');

  // Example usage:
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');

  // Close the connection after all operations are done
  client.quit();
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

async function setNewSchool(schoolName, value) {
  const reply = await new Promise((resolve) => {
    client.set(schoolName, value, (err, reply) => {
      console.log('Reply:', reply);
      resolve(reply);
    });
  });

  return reply;
}

async function displaySchoolValue(schoolName) {
  const reply = await getAsync(schoolName);
  console.log(reply);
}

