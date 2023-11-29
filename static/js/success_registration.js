function showNotification() {
    const notificationContainer = document.getElementById('notification-container');
    const notification = document.getElementById('notification');
    const notificationMessage = document.getElementById('notification-message');

    // notificationMessage.innerText = 'You have successfully created account! \n' +
    //     'To confirm your account check your email';
    notification.classList.add('show');

    setTimeout(() => {
        notification.addEventListener('transitionend', function () {
            notification.style.display = 'none';
        }, { once: true });

        notification.classList.remove('show');
    }, 5000);
}

document.getElementById('close-btn').addEventListener('click', function () {
    document.getElementById('notification').classList.remove('show');
    document.getElementById('notification').style.display = "none";
});

showNotification();
