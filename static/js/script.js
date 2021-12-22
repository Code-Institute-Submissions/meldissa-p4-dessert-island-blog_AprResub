// Please note code was used from the Code Institute I Think Therefore I Blog tutorial to help create this project
// Timeout function for alert messages
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);
