document.addEventListener('DOMContentLoaded', () => {

    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // When connected, configure buttons
    socket.on('connect', () => {

        // Each button should emit a "submit vote" event
        document.querySelectorAll('#send').forEach(button => {
            button.onclick = () => {
                const message = button.dataset.vote; // klopt nog niet, user, channel, tijd toevoegen
                socket.emit('send message', {'message': message});
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
function add_post(contents) {

                  // Create new post.
                  const post = document.createElement('div');
                  post.className = 'post';
                  post.innerHTML = contents;

                  // Add post to DOM.
                  document.querySelector('#posts').append(post);
