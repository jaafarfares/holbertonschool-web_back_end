// create a small HTTP server using the http module:
const http = require("http");
const host = 'localhost';
const port = 1245;
const requestListener = function (req, res) { 
    res.writeHead(200); 
    res.end("Hello Holberton School!"); 
   }; 
   const server = http.createServer(requestListener); 
   server.listen(port, host, () => { 
    console.log(`Server is running on http://${host}:${port}`); 
   }); 
