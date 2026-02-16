# Guest in the Universe - Application Structure

Technical documentation for the Flask application structure, components, and development details.

## Directory Structure

```
src/app/
├── static/
│   ├── styles/          # CSS modules (base, header, components, mobile, post, index)
│   └── scripts/         # JavaScript modules (theme, mobile, main)
├── templates/
│   ├── partials/        # Reusable HTML components (header, footer)
│   └── pages/           # Page templates (base, index, about, post)
├── content/             # Static markdown content (about, posts)
├── routes/              # Flask route handlers (main, api)
|── app.py              # Main Flask application
```

## Frontend Architecture

### CSS Organization
- **Modular Structure**: Each CSS file handles specific components
- **CSS Variables**: Centralized theming in base.css
- **Responsive Design**: Mobile-first approach with progressive enhancement
- **Component-Based**: Reusable styles for buttons, forms, navigation

### JavaScript Modules
- **theme.js**: Manages light/dark theme switching and system preference detection
- **mobile.js**: Handles mobile drawer navigation and floating buttons
- **main.js**: Application initialization and event listeners

## Navigation System

### Floating Buttons
- **Back to Top**: Smooth scroll to page top
- **Back to Home**: Navigate to homepage
- **Responsive Positioning**:
  - Desktop: Left sidebar vertical layout
  - Tablet/Mobile: Bottom-right horizontal layout

### Mobile Navigation
- **Drawer Menu**: Slide-out navigation with overlay
- **Hamburger Button**: Toggle menu visibility
- **Keyboard Support**: ESC key to close drawer

## Theme System

### CSS Variables
```css
:root {
    --bg-color: #ffffff;
    --text-color: #333333;
    --link-color: #3498db;
    --link-hover: #2980b9;
}

[data-theme="dark"] {
    --bg-color: #1a1a1a;
    --text-color: #e0e0e0;
}
```

### Theme Management
- **System Preference**: Auto-detects OS theme preference
- **Manual Toggle**: User can override system preference
- **Persistent Storage**: Saves theme choice in localStorage

## Responsive Design

### Breakpoints
- **Desktop**: >1024px (6rem padding, left sidebar nav)
- **Tablet**: <=1024px (4rem padding, bottom-right nav)
- **Mobile**: <=768px (1rem padding, bottom-right nav)

### Layout Optimization
- **Content Width**: Max 1200px for optimal reading
- **Flexible Grid**: Responsive post layouts
- **Touch Targets**: Minimum 44px for mobile accessibility

## Development

### Local Setup
See ../README.md for local development setup instructions.

---

*For deployment and infrastructure details, see the main project README.*
