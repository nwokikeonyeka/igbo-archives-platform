// Push Notifications Management for Igbo Archives
// Handles Web Push notification subscriptions using the Push API

function urlBase64ToUint8Array(base64String) {
    const padding = '='.repeat((4 - base64String.length % 4) % 4);
    const base64 = (base64String + padding)
        .replace(/\-/g, '+')
        .replace(/_/g, '/');
    const rawData = window.atob(base64);
    const outputArray = new Uint8Array(rawData.length);
    for (let i = 0; i < rawData.length; ++i) {
        outputArray[i] = rawData.charCodeAt(i);
    }
    return outputArray;
}

async function subscribeToPushNotifications() {
    if (!('serviceWorker' in navigator) || !('PushManager' in window)) {
        console.log('Push notifications not supported');
        return;
    }
    
    try {
        const permission = await Notification.requestPermission();
        if (permission !== 'granted') {
            console.log('Permission not granted for notifications');
            return;
        }
        
        const registration = await navigator.serviceWorker.ready;
        
        // Get VAPID public key from backend (will be set via environment variable)
        // For now, subscriptions will be created when VAPID keys are configured
        const vapidPublicKey = document.querySelector('meta[name="vapid-public-key"]')?.content;
        
        if (!vapidPublicKey) {
            console.log('VAPID public key not configured - skipping push subscription');
            return;
        }
        
        const subscription = await registration.pushManager.subscribe({
            userVisibleOnly: true,
            applicationServerKey: urlBase64ToUint8Array(vapidPublicKey)
        });
        
        // Send subscription to backend
        const response = await fetch('/api/push-subscribe/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify(subscription)
        });
        
        if (response.ok) {
            console.log('Push notification subscription successful');
        } else {
            console.error('Failed to save subscription:', await response.text());
        }
    } catch (error) {
        console.error('Error subscribing to push notifications:', error);
    }
}

async function unsubscribeFromPushNotifications() {
    try {
        const registration = await navigator.serviceWorker.ready;
        const subscription = await registration.pushManager.getSubscription();
        
        if (subscription) {
            await subscription.unsubscribe();
            
            await fetch('/api/push-unsubscribe/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            });
            
            console.log('Unsubscribed from push notifications');
        }
    } catch (error) {
        console.error('Error unsubscribing:', error);
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Service Worker Registration
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/serviceworker.js')
            .then(registration => {
                console.log('ServiceWorker registered');
                // Optionally enable push notifications automatically for logged-in users
                // subscribeToPushNotifications();
            })
            .catch(err => console.log('ServiceWorker registration failed:', err));
    });
}

// Export functions for use in templates
window.subscribeToPush = subscribeToPushNotifications;
window.unsubscribeFromPush = unsubscribeFromPushNotifications;
