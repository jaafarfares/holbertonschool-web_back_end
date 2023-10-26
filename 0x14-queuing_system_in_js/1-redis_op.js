import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
  // Example usage:
  displaySchoolValue('Holberton', () => {
    setNewSchool('HolbertonSanFrancisco', '100', () => {
      displaySchoolValue('HolbertonSanFrancisco', () => {
        // Close the connection after all operations are done
        client.quit();
      });
    });
  });
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value, callback) {
  client.set(schoolName, value, (err, reply) => {
    console.log('Reply:', reply);
    callback();
  });
}

function displaySchoolValue(schoolName, callback) {
  client.get(schoolName, (err, reply) => {
    console.log(reply);
    callback();
  });
}
