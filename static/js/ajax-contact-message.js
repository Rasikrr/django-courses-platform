


document.addEventListener('DOMContentLoaded', function () {
    console.log("WORKING");
    let form = document.getElementById('contactForm');

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      let formData = new FormData(form);
      console.log(formData)
      let xhr = new XMLHttpRequest();
      xhr.open('POST', '/contact/', true);  // Specify the URL for form submission
      xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');  // Indicate that it's an AJAX request
      xhr.responseType = 'json';
      xhr.send(formData);
      xhr.onload = function () {
          if (xhr.status === 200) {
              showNotification(xhr.response.message);
              console.log(123);
          } else {
              console.error('Error in AJAX request');
              // Handle error response
              alert('Error: ' + xhr.response.message);  // You can customize this part
          }
      }


      xhr.onerror = function () {
          console.error('Request failed');
          // Handle other errors
      }
  });

  function showNotification(message) {
        const notificationContainer = document.getElementById('notification-container');
        const notification = document.getElementById('notification');
        const notificationMessage = document.getElementById('notification-message');

        notificationMessage.innerText = message;
        notification.style.display = "flex";
        notification.classList.add('show');

        setTimeout(() => {
            notification.addEventListener('transitionend', function () {
                notification.style.display = 'none';
            }, { once: true });

            notification.classList.remove('show');
        }, 5000);
    }
});

document.getElementById('close-btn').addEventListener('click', function () {
    document.getElementById('notification').classList.remove('show');
    document.getElementById('notification').style.display = "none";
});
