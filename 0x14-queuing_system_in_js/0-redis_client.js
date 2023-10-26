import redis from 'redis';
const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

process.on('SIGINT', () => {
  client.quit();
});

client.set('testKey', 'Hello, Redis!', (err, reply) => {
  if (err) {
    console.error(`Error setting key: ${err}`);
  } else {
    console.log(`Set key: ${reply}`);
  }

  client.quit();
});
