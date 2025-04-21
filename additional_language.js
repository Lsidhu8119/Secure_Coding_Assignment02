const fs = require("fs");
const http = require("http");

const port = 3000;

http.createServer((req, res) => {
  const url = req.url;

  fs.readFile("." + url, (err, data) => {
    if (err) {
      res.writeHead(404);
      return res.end("404 Not Found");
    }
    res.writeHead(200);
    res.write(data);
    return res.end();
  });
}).listen(port);

console.log(`Server running at http://localhost:${port}`);
