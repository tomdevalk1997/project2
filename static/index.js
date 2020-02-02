document.addEventListener('DOMContentLoaded', function() {

    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    socket.on('connect', () => {
        socket.emit('new_connection', {"message_connection": "New user connected"});

        document.querySelectorAll('#send-message').forEach(button => {
            button.onclick = () => {
                message = document.getElementById("message-input").value;
                if (message.length > 0) {
                    socket.emit('send_message', {"message": message});
                }
            };
        });

        document.querySelectorAll('.channel-link').forEach(a => {
            a.onclick = () => {
                socket.emit('joinroom');
                console.log("Room joined");
                io.sockets.in("room-1").emit('connectToRoom', "You are in room no. 1");
            }
        });

        // // Submit button should emit a "create username" event
        // document.querySelectorAll('#username-submit').onclick = function () {
        //     const username = button.dataset.vote; // klopt nog niet, dataset....
        //     socket.emit('create username', {'username': username});
        // });
    });
    //
    // // When a message is sent...
    // socket.on('message_sent', data => {
    //     document.getElementById('message-input').value = '';
    // });
});
