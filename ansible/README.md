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

3. **Deploy**:
   ```bash
   # Infrastructure configuration
   ansible-playbook -i inventory/hosts.yml playbooks/infrastructure.yml

   # Application deployment
   ansible-playbook -i inventory/hosts.yml playbooks/app-deploy.yml

   # Content upload
   ansible-playbook -i inventory/hosts.yml playbooks/posts-upload.yml
   ```

## Playbooks

- **infrastructure.yml**: Server infrastructure setup
- **app-deploy.yml**: Application deployment
- **posts-upload.yml**: Content upload

## Test

- `http://your-domain.com` - Application
- `http://your-domain.com/health` - Health check

## Security

- Never commit `vars.yml` or `inventory/hosts.yml`
- Use `../config/` directory templates
- All secrets should be in GitHub Secrets for CI/CD
