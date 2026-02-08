# Guest in the Universe

A blog and web application exploring the vastness of our universe through technology, philosophy, and digital experiences.

## Quick Start

### Local Development
```bash
cd src
docker compose up -d
```
Access at: http://localhost:80

### Production Deployment
```bash
cd ansible
cp vars.yml.example vars.yml
# Update vars.yml with your server details
ansible-playbook -i inventory/hosts.yml playbooks/deploy.yml
```

##  Architecture

- **Frontend**: Flask web application with responsive design
- **Backend**: Python Flask API with health endpoints
- **Deployment**: Docker containers with Nginx reverse proxy
- **Infrastructure**: Ansible automation for server setup
- **CI/CD**: GitHub Actions with GHCR container registry

##  Container Images

### Production Images
- Use semantic versioning: `v0.0.0`, `v1.0.0`, etc.

### Development Images
- Use semantic versioning with `-dev` suffix: `v0.0.0-dev1`, `v0.0.0-dev2`, etc.


### Version Files
- `APP_VERSION`: Tracks current version
- `RELEASE_NOTES.md`: Contains release history and changes

### Version Guidelines
- Follow semantic versioning (MAJOR.MINOR.PATCH)
- Increment PATCH for bug fixes and features
- Increment MINOR for new features (backward compatible)
- Increment MAJOR for breaking changes

## Development Workflow

1. **Local Development**: Work in `src/` directory
2. **Version Management**: Update `APP_VERSION` and `RELEASE_NOTES.md`
3. **Test Changes**: Push to `feature/github-actions` branch
4. **Update workflow**: Update `build-and-deploy.yml` workflow with branch name
5. **Update secrets**: Update GitHub secrets with new version if needed
6. **Automated Build**: GitHub Actions builds, validates, and pushes images to GHCR
7. **Automated Deploy**: GitHub Actions automatically deploys to production via Ansible
8. **Monitor**: Check deployment status in GitHub Actions

### Automated CI/CD Pipeline
- **Build**: GitHub Actions builds app and nginx images
- **Validate**: Tests containers locally before pushing
- **Push**: Stores images in GitHub Container Registry (GHCR)
- **Deploy**: Ansible pulls and deploys images to Oracle VM
- **Monitor**: Health checks and deployment verification

### Configuration Required
This project uses both GitHub Secrets and Ansible variables for configuration.

**Setup Instructions:**
1. See `config.example.yml` for complete configuration template
2. Add GitHub Secrets in Repository > Settings > Secrets and variables > Actions
3. Copy Ansible variables to `ansible/vars.yml`
4. Ensure values are consistent between GitHub Secrets and Ansible

**Security Note:** Never commit actual secrets to the repository. Use the template for reference only.

##  Endpoints

- `/` - Main application interface
- `/health` - Health check endpoint
- `/test` - Simple test page

##  Configuration

### Ansible Variables
See `config.example.yml` for complete configuration template and setup instructions.

##  Technologies

- **Python 3.11** - Application runtime
- **Flask 2.3.3** - Web framework
- **Nginx** - Reverse proxy and static serving
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **Ansible** - Infrastructure automation
- **GitHub Actions** - CI/CD pipeline
- **GitHub Container Registry (GHCR)** - Container imagestorage
- **Oracle Cloud** - Production infrastructure

##  Security

- HTTPS redirection in production
- SSL certificate management
- Container health monitoring
- Firewall configuration via UFW

##  Monitoring

- Container health checks

---

