// Share functionality for posts
function toggleShareDrawer() {
    const drawer = document.getElementById('shareDrawer');
    const shareBtn = document.querySelector('.share-btn');
    
    if (drawer) {
        drawer.classList.toggle('active');
    }
    
    if (shareBtn) {
        shareBtn.classList.toggle('active');
    }
}

async function copyLink() {
    try {
        await navigator.clipboard.writeText(window.location.href);
        showToast();
    } catch (err) {
        console.error('Error copying link:', err);
        alert('Failed to copy link');
    }
}

function showToast() {
    const toast = document.getElementById('toast');
    if (toast) {
        toast.classList.add('show');
        setTimeout(() => {
            toast.classList.remove('show');
        }, 2000);
    }
}

// Close drawer when clicking outside
document.addEventListener('click', function(event) {
    const drawer = document.getElementById('shareDrawer');
    const toggle = document.querySelector('.share-toggle');
    const shareBtn = document.querySelector('.share-btn');
    
    if (drawer) {
        const isClickInsideDrawer = drawer.contains(event.target);
        const isClickInsideToggle = toggle && toggle.contains(event.target);
        const isClickInsideShareBtn = shareBtn && shareBtn.contains(event.target);
        
        if (!isClickInsideDrawer && !isClickInsideToggle && !isClickInsideShareBtn) {
            drawer.classList.remove('active');
            if (shareBtn) {
                shareBtn.classList.remove('active');
            }
        }
    }
});
