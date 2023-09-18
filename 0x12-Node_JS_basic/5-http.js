const http = require('http');
const fs = require('fs');
const path = require('path');

const hostname = 'localhost';
const port = 1245;
const databaseFileName = process.argv[2] || 'database.csv'; 

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    readStudentsFromFile(databaseFileName)
      .then((studentData) => {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end(`This is the list of our students\n${studentData}`);
      })
      .catch((error) => {
        res.statusCode = 500;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Internal Server Error');
        console.error(error);
      });
  } else {
    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Not Found');
  }
});

app.listen(port, hostname, () => {
  console.log(`Server is running at http://${hostname}:${port}/`);
});

function readStudentsFromFile(filename) {
  return new Promise((resolve, reject) => {
    const filePath = path.join(__dirname, filename);
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(err);
        return;
      }
      const students = data.trim().split('\n').slice(1);
      const studentInfo = students.map((student) => {
        const [firstName, lastName, age, field] = student.split(',');
        return `Number of students in ${field}: 1. List: ${firstName}`;
      });
      resolve(studentInfo.join('\n'));
    });
  });
}

module.exports = app;
