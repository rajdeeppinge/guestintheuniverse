# Guest in the Universe

A blog and web application exploring the vastness of our universe through technology, philosophy, and digital experiences.

## Quick Start

### Local Development
```bash
cd src
docker compose -f docker-compose.local.yml up --build
```
Access at: http://localhost:5000

See [src/README.md](src/README.md) for detailed local development instructions.

### Production Deployment

**Automated Deployment** (recommended):
- Push changes to master branch
- GitHub Actions automatically triggers based on file changes
- See [.github/workflows/README.md](.github/workflows/README.md) for workflow details

**Manual Deployment**:
- Use GitHub Actions manual dispatch or run Ansible playbooks directly
- See [ansible/README.md](ansible/README.md) for manual deployment instructions

## Architecture

- **Frontend**: Flask web application with responsive design
- **Backend**: Python Flask API with health endpoints
- **Deployment**: Docker containers with Nginx reverse proxy
- **Infrastructure**: Ansible automation for server setup
- **CI/CD**: GitHub Actions with GHCR container registry

## Documentation

- **[src/README.md](src/README.md)** - Application structure and local development guidelines
- **[ansible/README.md](ansible/README.md)** - Manual production deployment and infrastructure setup
- **[config/README.md](config/README.md)** - Configuration templates and setup instructions
- **[.github/workflows/README.md](.github/workflows/README.md)** - Automated CI/CD workflows and automation
- **[RELEASE_NOTES.md](RELEASE_NOTES.md)** - Version history and changelog

## Development Workflow

1. **Local Development**: Work in `src/` directory (see [src/README.md](src/README.md))
2. **Version Management**: Update `APP_VERSION` and `RELEASE_NOTES.md` when ready for release
3. **Push Changes**: Push to master branch
4. **Automated Deployment**: GitHub Actions triggers based on file changes:
   - Infrastructure changes → infrastructure.yml
   - Application changes → app-deployment.yml
   - Content changes → posts-upload.yml
5. **Manual Deployment**: All workflows support manual dispatch via GitHub Actions UI

## Release Process

1. Update `APP_VERSION` with new version number
2. Update `RELEASE_NOTES.md` with release notes for the new version
3. Commit and push changes
4. Create git tag: `git tag v0.4.0 && git push --tags`
5. GitHub Actions automatically creates GitHub Release with release notes

## Configuration

See [config/README.md](config/README.md) for complete configuration templates and setup instructions.

## Technologies

- **Python 3.11** - Application runtime
- **Flask 2.3.3** - Web framework
- **Nginx** - Reverse proxy and static serving
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **Ansible** - Infrastructure automation
- **GitHub Actions** - CI/CD pipeline
- **GitHub Container Registry (GHCR)** - Container image storage
- **Oracle Cloud** - Production infrastructure

## Security

- HTTPS redirection in production
- SSL certificate management
- Container health monitoring
- Firewall configuration via UFW

## Endpoints

- `/` - Main application interface
- `/health` - Health check endpoint
- `/test` - Simple test page

---
