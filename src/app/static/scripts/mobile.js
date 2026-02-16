// Mobile drawer management
function toggleDrawer() {
    const drawer = document.getElementById('mobileDrawer');
    const overlay = document.getElementById('overlay');
    
    drawer.classList.toggle('open');
    overlay.classList.toggle('show');
    
    // Prevent body scroll when drawer is open
    document.body.style.overflow = drawer.classList.contains('open') ? 'hidden' : '';
}

// Close drawer on escape key
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        const drawer = document.getElementById('mobileDrawer');
        if (drawer.classList.contains('open')) {
            toggleDrawer();
        }
    }
});

// Back to top functionality
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}
