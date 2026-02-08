# Guest in the Universe - Ansible Deployment

Deploy Guest in the Universe application to server

## Setup

1. **Clone and configure**:
   ```bash
   git clone https://github.com/yourusername/guestintheuniverse_ansible.git
   cd guestintheuniverse_ansible
   cp inventory/hosts.yml.example inventory/hosts.yml
   ```

2. **Configure variables**:
   - See `../config.example.yml` for complete configuration template
   - Copy the YAML section from `../config.example.yml` to `ansible/vars.yml`
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
   # Ansible automatically uses global variables from vars.yml

   # deploy.yml will deploy app
   ansible-playbook -i inventory/hosts.yml playbooks/deploy.yml
   ```

## Test Deployment

- `http://your-domain.com` - Nginx default page
- `http://your-domain.com/test` - Test message
- `http://your-domain.com/health` - Health check

## Security

- **Never commit** `vars.yml` or `inventory/hosts.yml`
- Use `../config.example.yml` as the configuration template
- `.gitignore` prevents accidental commits
- All sensitive data should be in GitHub Secrets for CI/CD
