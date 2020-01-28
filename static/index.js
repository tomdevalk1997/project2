document.addEventListener('DOMContentLoaded', () => {

    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // When connected, configure buttons
    socket.on('connect', () => {

        // Send button should emit a "send message" event
        document.querySelectorAll('#send-message').forEach(button => {
            button.onclick = () => {
                alert("Button clicked, message being sent");
                const message = document.getElementById("message-input"); // klopt nog niet, user, channel, tijd toevoegen, dataset....
                // const user = button.dataset.vote;
                // const channel = button.dataset.vote;
                socket.emit('send message', {'message': message});
            };
        });

        // Submit button should emit a "create username" event
        document.querySelectorAll('#username-submit').forEach(button => {
            button.onclick = () => {
                const username = button.dataset.vote; // klopt nog niet, dataset....
                socket.emit('create username', {'username': username});
            };
        });
    });

    // When a new vote is announced, add to the unordered list
    socket.on('message sent', data => {
        document.querySelector('#yes').innerHTML = data.yes;
        document.querySelector('#no').innerHTML = data.no;
        document.querySelector('#maybe').innerHTML = data.maybe;
    });
});
//    function add_post(contents) {

                  // Create new post.
                  // const post = document.createElement('div');
                  // post.className = 'post';
                  // post.innerHTML = contents;
                  //
                  // // Add post to DOM.
                  // document.querySelector('#posts').append(post);
