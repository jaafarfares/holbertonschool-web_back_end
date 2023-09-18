const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;
const database = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.send('This is the list of our students\n');
    const students = await countStudents(database);
    res.send(students.join('\n'));

});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

module.exports = app;
