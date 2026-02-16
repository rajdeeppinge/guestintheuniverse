# Release Notes

This file contains release history and changes for Guest in the Universe.

## Version History

### v0.1.0-dev2
- Deploy and manage posts and images separately from application code

### v0.1.0-dev1
First release with application frontend and backend.

**New Features:**
- Home and About pages and workflows
- Posts with markdown support
- Pagination: First/Last page navigation with smart page range display. Shows current +/-1 pages with ellipsis to prevent wrapping
- Added author information to posts and listings
- Automatic reading time estimation for posts
- Added contact email in footer
- Responsive design, simple layout and mobile compatibility
- Clear association between posts and images
- Better support for local images

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
