document.getElementById('register-btn').addEventListener('click', function() {
    document.getElementById('main-box').classList.add('hidden');
    document.getElementById('register-box').classList.remove('hidden');
});

document.getElementById('register-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const phone = document.getElementById('phone').value;
    const email = document.getElementById('email').value;

    // Here you can handle the form data, e.g., send it to the server
    alert(`Name: ${name}\nAge: ${age}\nPhone: ${phone}\nEmail: ${email}`);

    // Redirect to the home page
    window.location.href = 'home.html';
});
