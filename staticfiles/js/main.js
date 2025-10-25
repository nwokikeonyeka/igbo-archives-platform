document.addEventListener('DOMContentLoaded', function() {
    const darkModeToggle = document.querySelector('.night-mode-toggle');
    const body = document.body;
    
    const darkMode = localStorage.getItem('darkMode');
    if (darkMode === 'enabled') {
        body.classList.add('dark-mode');
        if (darkModeToggle) {
            darkModeToggle.textContent = '☀️';
        }
    }
    
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', function() {
            body.classList.toggle('dark-mode');
            if (body.classList.contains('dark-mode')) {
                localStorage.setItem('darkMode', 'enabled');
                darkModeToggle.textContent = '☀️';
            } else {
                localStorage.setItem('darkMode', 'disabled');
                darkModeToggle.textContent = '🌙';
            }
        });
    }
    
    let deferredPrompt;
    const installButton = document.querySelector('.pwa-install-button');
    
    window.addEventListener('beforeinstallprompt', (e) => {
        e.preventDefault();
        deferredPrompt = e;
        if (installButton) {
            installButton.style.display = 'block';
        }
    });
    
    if (installButton) {
        installButton.addEventListener('click', async () => {
            if (deferredPrompt) {
                deferredPrompt.prompt();
                const { outcome } = await deferredPrompt.userChoice;
                console.log(`User response to the install prompt: ${outcome}`);
                deferredPrompt = null;
                installButton.style.display = 'none';
            }
        });
    }
    
    window.addEventListener('appinstalled', () => {
        console.log('PWA was installed');
        if (installButton) {
            installButton.style.display = 'none';
        }
    });
});

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        alert('Link copied to clipboard!');
    }, function(err) {
        console.error('Could not copy text: ', err);
    });
}

function toggleView(view) {
    const container = document.querySelector('.archive-container');
    if (!container) return;
    
    if (view === 'grid') {
        container.classList.remove('archive-list');
        container.classList.add('archive-grid');
    } else {
        container.classList.remove('archive-grid');
        container.classList.add('archive-list');
    }
    
    document.querySelectorAll('.view-toggle button').forEach(btn => {
        btn.classList.remove('active');
    });
    event.target.classList.add('active');
}
