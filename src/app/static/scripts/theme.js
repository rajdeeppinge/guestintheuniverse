// Theme management
function initTheme() {
    const savedPreference = localStorage.getItem('theme-preference');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    // Set initial theme - use system preference as default if no saved preference
    let theme;
    let preference;
    
    if (savedPreference) {
        preference = savedPreference;
        theme = savedPreference === 'dark' ? 'dark' : 'light';
    } else {
        // Use system preference as default
        preference = systemPrefersDark ? 'dark' : 'light';
        theme = preference;
        localStorage.setItem('theme-preference', preference);
    }
    
    document.documentElement.setAttribute('data-theme', theme);
    updateThemeButtons(preference);
}

function setTheme(preference) {
    localStorage.setItem('theme-preference', preference);
    
    const theme = preference;
    document.documentElement.setAttribute('data-theme', theme);
    updateThemeButtons(preference);
}

function updateThemeButtons(preference) {
    // Update desktop buttons
    const lightBtn = document.getElementById('theme-light-btn');
    const darkBtn = document.getElementById('theme-dark-btn');
    
    // Update mobile drawer buttons
    const drawerLightBtn = document.getElementById('drawer-theme-light-btn');
    const drawerDarkBtn = document.getElementById('drawer-theme-dark-btn');
    
    // Remove active class from all buttons
    [lightBtn, darkBtn, drawerLightBtn, drawerDarkBtn].forEach(btn => {
        if (btn) btn.classList.remove('active');
    });
    
    // Add active class to selected buttons
    if (preference === 'light') {
        if (lightBtn) lightBtn.classList.add('active');
        if (drawerLightBtn) drawerLightBtn.classList.add('active');
    } else if (preference === 'dark') {
        if (darkBtn) darkBtn.classList.add('active');
        if (drawerDarkBtn) drawerDarkBtn.classList.add('active');
    }
}

// Watch for system theme changes and update if user hasn't set a preference
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
    const savedPreference = localStorage.getItem('theme-preference');
    // Only auto-update if user hasn't manually set a preference
    if (!savedPreference) {
        const theme = e.matches ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', theme);
        updateThemeButtons(theme);
    }
});

// Initialize theme on page load
document.addEventListener('DOMContentLoaded', initTheme);
