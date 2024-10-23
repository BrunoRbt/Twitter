document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    const tweetForm = document.getElementById('tweet-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            const response = await fetch('/api/token/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });

            const data = await response.json();
            localStorage.setItem('token', data.access);
            window.location.href = 'index.html';
        });
    }

    if (registerForm) {
        registerForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            await fetch('/api/register/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, email, password }),
            });

            window.location.href = 'login.html';
        });
    }

    if (tweetForm) {
        tweetForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const content = document.getElementById('content').value;
            const token = localStorage.getItem('token');

            await fetch('/api/tweets/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`,
                },
                body: JSON.stringify({ content }),
            });

            window.location.href = 'index.html';
        });
    }

    if (document.getElementById('feed')) {
        const token = localStorage.getItem('token');

        fetch('/api/tweets/', {
            headers: {
                'Authorization': `Bearer ${token}`,
            },
        })
        .then(response => response.json())
        .then(data => {
            const feed = document.getElementById('feed');
            data.forEach(tweet => {
                const tweetElement = document.createElement('div');
                tweetElement.textContent = `${tweet.user.username}: ${tweet.content}`;
                feed.appendChild(tweetElement);
            });
        });
    }
});