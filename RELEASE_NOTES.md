# Release Notes

This file contains release history and changes for Guest in the Universe.

## Version History

### v0.0.0-dev5
- Add fully automated deployment workflow using GitHub actions and secrets management

### v0.0.0-dev4
- Handle GHCR authentication during server deployment

### v0.0.0-dev3
- Combine validation and push steps for container images to maintain consistent versioning

### v0.0.0-dev2
- Add validation for app and nginx images
- Remove container image build logic from ansible flow
- Add logic to fetch images from registry for deployment

### v0.0.0-dev1
- Add local development environment
- Add ansible playbooks for production deployment
- Add semantic versioning and release notes
- Add version tracking with APP_VERSION
- Add RELEASE_NOTES.md for tracking changes
- Add GitHub Actions with GHCR integration
