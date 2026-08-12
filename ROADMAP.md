# Roadmap

This document outlines the planned development roadmap for Guest in the Universe.

## Version Planning

### v0.6.0 - Content & Language Features
**Focus:** High-impact features that work with current resources

**SEO and Content Features:**
- [x] Add thumbnails for posts
- [x] Add share functionality (client-side, no DB needed)
- [x] Add RSS feed
- [x] Add sitemap.xml
- [x] Implement SEO optimization
- [x] Add LICENSE file

**Language Features:**
- [ ] Add Devanagari script support and development flow

**Tools Section:**
- [x] Add dedicated Tools section with unit converter
- [x] Create reusable unit calculator component (embeddable in posts)
- [x] Update existing unit converter post to use embedded calculator

---

### v0.7.0 - Infrastructure Scaling & Multilingual Support
**Focus:** Upgrade resources to support data-heavy features and multilingual content

**Infrastructure:**
- [ ] Add 2nd and 3rd instance for full dev and prod setup
- [ ] Upgrade to larger OCI instance (more CPU/RAM for DB and caching)
- [ ] Implement environment-specific configurations
- [ ] Add staging environment
- [ ] Evaluate and implement /var/log/nginx mounting strategy
- [ ] Implement logrotate for container logs
- [ ] Restructure and cleanup src directory
- [ ] Implement pre-commit hooks
- [ ] Setup local development database

**Data Architecture:**
- [ ] Add database support (PostgreSQL)
- [ ] Implement posts with IDs for better management
- [ ] Design database schema for future features
- [ ] Implement database migration strategy
- [ ] Add backup strategy for posts/data

**Multilingual Support:**
- [ ] Implement multilingual content support (requires database)
- [ ] Add language switching UI
- [ ] Implement URL routing for multiple languages

**Documentation:**
- [ ] Complete documentation

---

### v0.8.0 - User Engagement Features
**Focus:** Interactive features (requires DB from v0.7.0)

**User Authentication:**
- [ ] User registration/login
- [ ] User profiles
- [ ] Session management
- [ ] OAuth integration (Google, GitHub)

**Features:**
- [ ] Add comments system
- [ ] Add like functionality

**Content Management:**
- [ ] Add admin interface for content
- [ ] Implement draft/publish workflow
- [ ] Add tag/category system

---

### v0.9.0 - AI Integration
**Focus:** AI features (requires compute resources from v0.7.0)

**AI Features:**
- [ ] Display AI summary in posts
- [ ] Add AI audio podcast generation for posts
- [ ] Add AI video podcast generation (animated conversation)
- [ ] Add workflow to generate and upload images from AI image generation tool (Canva API)

**AI Integration:**
- [ ] Add agents.md for AI agent configuration
- [ ] Implement Skills and hooks for AI world integration
- [ ] Design AI content generation pipeline

**Performance:**
- [ ] Implement caching strategy (Redis)
- [ ] Add CDN configuration
- [ ] Implement image optimization pipeline

---

### v0.10.0 - Security & hardening and quality assurance
**Focus:** Production hardening and quality assurance

**Security:**
- [ ] Add SAST/DAST scanning in CI/CD
- [ ] Implement dependency vulnerability scanning
- [ ] Add rate limiting on API endpoints
- [ ] Configure security headers
- [ ] Add privacy policy (if collecting user data)
- [ ] Implement GDPR compliance (if applicable)

**Testing:**
- [ ] Add unit tests for Flask routes
- [ ] Add integration tests for workflows
- [ ] Add E2E testing with Playwright

---

### v0.11.0 - Monitoring & Reliability
**Focus:** Production visibility and reliability

**Monitoring/Observability:**
- [ ] Send logs to Loki and integrate with Grafana Cloud
- [ ] Setup alerting on system metrics and application log metrics
- [ ] Implement external service uptime checks
- [ ] Add performance monitoring dashboards

**Reliability:**
- [ ] Implement disaster recovery plan
- [ ] Add health check improvements
- [ ] Implement graceful degradation
- [ ] Implement blue-green deployment strategy

---

### v0.12.0 - Content Discovery & UX
**Focus:** Enhanced user experience and content discoverability

**Content Discovery:**
- [ ] Add search functionality
- [ ] Add basic usage analytics
- [ ] Add popular posts tracking

**User Experience:**
- [ ] Accessibility improvements
- [ ] Mobile responsiveness enhancements
- [ ] Dark mode refinements

---

### v1.0.0 - Production Release
**Focus:** Stable production-ready release

**Final Polish:**
- [ ] Comprehensive testing and bug fixes
- [ ] Performance optimization
- [ ] Documentation completion
- [ ] Stable API contract
- [ ] Production deployment validation

---

## Notes

This roadmap is a living document and will be updated as priorities change. Focus is on building features that align with the project's vision of exploring the universe through technology, philosophy, and digital experiences.
