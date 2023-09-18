// create a small HTTP server using the http module:
const http = require("http");
const host = 'localhost';
const port = 1245;
const app = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  });
   const server = http.createServer(app); 
   server.listen(port, host, () => { 
    console.log(`Server is running on http://${host}:${port}`); 
   }); 

   module.exports = app;
