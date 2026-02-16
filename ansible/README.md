# Guest in the Universe - Ansible Deployment

Deploy application to server using Ansible.

## Setup

1. **Configure inventory**:
   ```bash
   git clone https://github.com/yourusername/guestintheuniverse_ansible.git
   cd guestintheuniverse_ansible
   cp inventory/hosts.yml.example inventory/hosts.yml
   ```

2. **Configure variables**:
   - See `../config.example.yml` for complete configuration template
   - Copy the YAML section from `../config.example.yml` to `./vars.yml`
   - Update with your actual server details

3. **Manual TLS/SSL Certificate Setup** (recommended for security):
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

4. **Deploy**:
   ```bash
   ansible-playbook -i inventory/hosts.yml playbooks/deploy.yml
   ```

## Test

- `http://your-domain.com` - Application
- `http://your-domain.com/health` - Health check

## Security

- Never commit `vars.yml` or `inventory/hosts.yml`
- Use `../config.example.yml` as template
- All secrets should be in GitHub Secrets for CI/CD
