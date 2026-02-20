# Release Notes

This file contains release history and changes for Guest in the Universe.

## Version History

### v0.3.0-dev2
Production ready content
- Update links to images in object storage
- Fix internal links to other posts


### v0.3.0-dev1
Object Storage integration and image management improvements.

**New Features:**
- Object Storage integration for image serving
- Automated image URL updates in all posts
- Nginx proxy configuration for Object Storage
- Validation workflow enhancements for image endpoints
- Removed local image dependencies from deployment

**Infrastructure:**
- Object Storage namespace, bucket, and region configuration
- Dynamic nginx proxy for image endpoints
- GitHub secrets integration for Object Storage credentials
- Container registry optimization

**Bug Fixes:**
- Fixed nested Markdown image formats
- Corrected image path references
- Improved validation testing for image endpoints

---

### v0.2.0
Major UX overhaul with mobile-first design, enhanced navigation system, dark mode, and API-first architecture.

**Key Features:**
- **Mobile-First Design**: Drawer navigation with hamburger menu and mobile-optimized layouts
- **Dark Mode System**: Complete light/dark theme with system preference detection
- **Dual Floating Navigation**: Back to Top/Back to Home buttons with intelligent responsive positioning
- **API-First Architecture**: Dynamic content loading

**Navigation Improvements:**
- Smart button placement: Left sidebar (desktop) → Bottom-right (mobile/tablet)
- Clear icons and tooltips to eliminate navigation confusion
- Touch-optimized sizing with blog-consistent theming
- Always-accessible design replacing hidden scroll-based buttons

**Layout & Design:**
- Header/footer width adjusted to content on variable width displays
- Responsive padding system for optimal readability
- Theme selector with horizontal toggle design

**Code Architecture:**
- Modular CSS/JS structure with proper separation of concerns
- Reusable HTML partials and externalized styles
- Dynamic content delivery from markdown files
- Eliminated hardcoded content from templates

---

### v0.1.0
Initial release with application frontend and backend.

**New Features:**
- Home and About pages and workflows
- Posts with markdown support
- Pagination: First/Last page navigation with smart page range display. Shows current +/-1 pages with ellipsis to prevent wrapping
- Added author information to posts and listings
- Automatic reading time estimation for posts
- Added contact email in the footer
- Responsive design, simple layout and mobile compatibility
- Clear association between posts and images
- Support for local images

---

### v0.0.0
Initial infrastructure release with complete CI/CD pipeline and deployment automation.

**Features:**
- Automated container image building and validation
- Combined build and deploy workflow with proper Ansible integration
- Production-ready deployment from master branch
- GitHub Container Registry (GHCR) integration
- Ansible playbooks for production deployment
- Local development environment setup
- Semantic versioning and release tracking

**Infrastructure:**
- Docker containerization with app and nginx images
- Automated deployment via GitHub Actions
- Secrets management for secure deployment
- Health checks and validation pipeline

**Development Tools:**
- Version tracking with APP_VERSION
- Release notes documentation
- Local development environment with Docker Compose
