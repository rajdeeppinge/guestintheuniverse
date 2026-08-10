# Release Notes

This file contains release history and changes for Guest in the Universe.

## Version History

### v0.5.0-dev1
Infrastructure & Resource Optimization (Development)

**Image and version management:**
- Added Docker image retention limits in GitHub Container Registry
- Keep last 3 production versions and delete dev versions for older releases
- Updated release workflow to enforce strict v*.*.* versioning
- Removed manual trigger from release workflow
- Modified app-deployment workflow to only deploy on tagged releases
- Dev versions now build and push images but don't deploy to production
- Fixed build workflow to properly terminate when image already exists
- Added conditional image building based on code changes

**Security and Maintenance:**
- Protected master branch with required reviews and status checks
- Configured repository ruleset to require pull requests for master changes
- Cleanup old branches
- Removed blogger references from repository
- Deleted the blog from blogger

**Documentation:**
- Created DEVELOPMENT.md with step-by-step development process
- Added development workflow conventions and versioning guidelines
- Updated README.md and ROADMAP.md to reference DEVELOPMENT.md

---

### v0.4.0
Infrastructure restructuring and CI/CD optimization

**New Features:**
- Split workflows into infrastructure, app-deployment, and posts-upload
- Path-based triggers for efficient CI/CD execution
- Weekly infrastructure maintenance schedule (Sunday 9 AM UTC)
- Automated GitHub Releases with git tags
- Centralized configuration templates in config/ directory

**Infrastructure:**
- Reusable composite action for Ansible setup
- Optimized workflow configurations with minimal variables per workflow
- Updated Grafana Alloy installation using official documentation
- Improved system-update role for weekly security patching
- Inventory renamed to hosts.yml for consistency

**Documentation:**
- Restructured READMEs for better documentation flow
- Added GitHub Actions workflows documentation
- Enhanced Ansible deployment documentation
- Configuration templates and setup instructions

**Bug Fixes:**
- Fixed composite action structure for GitHub Actions compatibility
- Resolved Grafana Alloy package availability issues
- Fixed workflow failures with proper checkout steps
- Improved idempotency across all Ansible roles

---

### v0.3.0
Object Storage integration, image management improvements and production ready content

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
- Update links to images in object storage
- Fix internal links to other posts

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
