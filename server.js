var http = require('http');

http.createServer(function(req, res) {
	console.log('incoming request being handled');
	res.end();
}).listen(8080);
console.log('listening on port 8080');
