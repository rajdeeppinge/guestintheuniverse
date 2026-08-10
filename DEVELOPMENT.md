# Development Process

This document outlines the step-by-step development process used in the Guest in the Universe project.

## Feature Development Process

### 1. Create Feature Branch
```bash
git checkout -b feature/feature-name
```
Use descriptive feature-based branch names (e.g., `feature/ghcr-image-retention`)

### 2. Update Version Information
- Update `APP_VERSION` file with development version (e.g., `v0.5.0-dev1`)
- Add corresponding entry to `RELEASE_NOTES.md` at the top of version history

### 3. Update Workflow Triggers
- Update relevant workflow files to include the feature branch in trigger conditions
- Example: Update `app-deployment.yml` to trigger on `branches: [ master, feature/feature-name ]`

### 4. Implement Changes
- Make the required code changes
- Update any related configuration files
- Ensure all changes follow project conventions

### 5. Test Locally
- Test application changes locally using `docker compose -f docker-compose.local.yml up --build`
- Infrastructure changes cannot be tested locally (requires production environment)
- Verify functionality before pushing to remote

### 6. Test and Commit
- Commit changes with descriptive messages
- Push to trigger workflow for testing
- Verify workflow runs successfully

### 7. Merge Dev Version to Master
- Create pull request to master branch for the dev version
- Remove feature branch from workflow triggers before merging
- Merge to master (this builds and pushes images but doesn't deploy to production)
- The dev version is now in master and images are available in GHCR for testing
- Note: Deployment to production only happens on tagged releases

### 8. Additional Development Iterations
- If more development is needed, repeat steps 1-7 with incremental dev version (e.g., `v0.5.0-dev2`)
- Each dev version is merged to master as it's completed
- Previous dev versions are already available in master for subsequent iterations
- Note: Master always contains the latest working code, but releases are controlled by tags

### 9. Create Production Release
- When ready for production release, update `APP_VERSION` to stable version (e.g., `v0.5.0`)
- Update `RELEASE_NOTES.md` with final production release notes
- Commit these changes to master
- Create git tag: `git tag v0.5.0 && git push origin v0.5.0`
- This triggers the release workflow and creates the official GitHub Release

## Versioning Convention

All versions follow strict semantic versioning with `v` prefix: `v*.*.*`

- **Production releases**: `v0.1.0`, `v0.2.0`, `v0.3.0`
- **Development versions**: `v0.5.0-dev1`, `v0.5.0-dev2`

The `v` prefix is mandatory for all version tags and image tags.
