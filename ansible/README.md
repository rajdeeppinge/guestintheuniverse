# Guest in the Universe - Ansible Deployment

Deploy application to server using Ansible.

## Setup

1. **Configure inventory and variables**:
   - See `../config/` directory for configuration templates
   - Copy `../config/vars.example.yml` to `./vars.yml`
   - Copy `../config/hosts.example.yml` to `inventory/hosts.yml`
   - Update with your actual server details

2. **Manual TLS/SSL Certificate Setup** (recommended for security):
   ```bash
   # On the server, create SSL directory
   sudo mkdir -p /path/to/certs

   # Copy your certificates (replace with your paths)
   scp ~/path/to/certs/cert.pem user@server:/path/to/certs/cert.pem
   scp ~/path/to/certs/key.pem user@server:/path/to/certs/key.pem
   sudo chmod 600 /path/to/certs/*
   ```

   ```yaml
   # Update vars.yml with the path to your certificates on the server
   ssl_cert_path: "/path/to/certs"
   ```

## Deployment

### Infrastructure Configuration
Run once or when infrastructure changes:
```bash
ansible-playbook -i inventory/hosts.yml playbooks/infrastructure.yml
```
Configures: Docker, users, firewall, monitoring

### Application Deployment
Run when app code changes:
```bash
ansible-playbook -i inventory/hosts.yml playbooks/app-deploy.yml
```
Deploys: App containers, nginx configuration

### Content Upload
Run when content changes:
```bash
ansible-playbook -i inventory/hosts.yml playbooks/posts-upload.yml
```
Uploads: Blog posts and markdown content

## Playbooks

- **infrastructure.yml**: Server infrastructure setup (docker, users, firewall, monitoring)
- **app-deploy.yml**: Application deployment (app, nginx, deploy roles)
- **posts-upload.yml**: Content upload (posts and drafts)

## Roles

- **system-update**: System package updates with cache validation
- **docker**: Docker installation and configuration
- **users**: Application user and group management
- **firewall**: UFW firewall configuration
- **monitoring**: Grafana Alloy monitoring setup
- **app**: Application directory setup
- **nginx**: Nginx configuration and templates
- **deploy**: Container deployment and management

## Test

- `http://your-domain.com` - Application
- `http://your-domain.com/health` - Health check

## Security

- Never commit `vars.yml` or `inventory/hosts.yml`
- Use `../config/` directory templates
- All secrets should be in GitHub Secrets for CI/CD
