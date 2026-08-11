// Calculate and set the appropriate container height based on posts per page
document.addEventListener('DOMContentLoaded', function() {
    const postsContainer = document.querySelector('.posts-container');
    const postsElements = document.querySelectorAll('.post-with-image');
    const postsPerPage = 5; // Fixed value to match the backend's per_page setting
    
    if (postsContainer && postsElements.length > 0) {
        // Calculate height based on first post's actual height
        const firstPostHeight = postsElements[0].offsetHeight;
        // Always calculate for full page of posts, even on last page
        const calculatedHeight = (firstPostHeight * postsPerPage) + 50; // Add some buffer
        postsContainer.style.setProperty('--posts-container-height', calculatedHeight + 'px');
    }
});
