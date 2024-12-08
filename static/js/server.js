const http = require('http');
const socketIo = require('socket.io');

const server = http.createServer();
const io = socketIo(server);

io.on('connection', (socket) => {
    console.log('New client connected');

    socket.on('updateText', (data) => {
        console.log('Text updated:', data);
        socket.broadcast.emit('textUpdated', data);
    });

    socket.on('disconnect', () => {
        console.log('Client disconnected');
    });
});

server.listen(3000, () => console.log('Socket.IO server running on port 3000'));
