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
3. **Test Changes**: Push to a development branch (e.g., `feature/github-actions`)
4. **Update Workflow**: Update the branch name in `.github/workflows/build-and-deploy.yml`
5. **Build Images**: Push to the development branch to trigger GitHub Actions workflow for building and pushing images to GHCR
6. **Deploy**: Use Ansible playbooks to pull from GHCR

### Deployment Flow
- **CI/CD**: GitHub Actions builds and pushes to GHCR
- **Production**: Ansible pulls pre-built images from GHCR

##  Endpoints

- `/` - Main application interface
- `/health` - Health check endpoint
- `/test` - Simple test page

##  Configuration

### Ansible Variables
See `ansible/vars.yml.example` for production configuration options.

##  Technologies

- **Python 3.11** - Application runtime
- **Flask 2.3.3** - Web framework
- **Nginx** - Reverse proxy and static serving
- **Docker** - Containerization
- **Ansible** - Infrastructure automation
- **GitHub Actions** - CI/CD pipeline

##  Security

- HTTPS redirection in production
- SSL certificate management
- Container health monitoring
- Firewall configuration via UFW

##  Monitoring

- Container health checks

---

