# Release Notes

This file contains release history and changes for Guest in the Universe.

## Version History

### v0.0.0-dev3
- Combine validation and push steps for container images to maintain consistent versioning

### v0.0.0-dev2
- Added validation for app and nginx images
- Removed container image build logic from ansible flow
- Added logic to fetch images from registry for deployment

### v0.0.0-dev1
- Added local development environment
- Added ansible playbooks for production deployment
- Added semantic versioning and release notes
    - Added version tracking with APP_VERSION
    - Added RELEASE_NOTES.md for tracking changes
- Added GitHub Actions with GHCR integration
