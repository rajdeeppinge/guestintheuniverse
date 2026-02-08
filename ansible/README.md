# Guest in the Universe - Ansible Deployment

Deploy Nginx container to Ubuntu/Debian system with Docker.

## Setup

1. **Clone and configure**:
   ```bash
   git clone https://github.com/yourusername/guestintheuniverse_ansible.git
   cd guestintheuniverse_ansible
   cp vars.yml.example vars.yml
   cp inventory/hosts.yml.example inventory/hosts.yml
   ```

2. **Update vars.yml** with your server details:
   ```yaml
   host: "your-server.domain.com"
   user: "your-ssh-username"
   ssh_key: "~/.ssh/your-private-key"
   ```

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

   # nginx-only.yml will only deploy nginx
   ansible-playbook -i inventory/hosts.yml playbooks/nginx-only.yml

   # deploy.yml will deploy app
   ansible-playbook -i inventory/hosts.yml playbooks/deploy.yml
   ```

## Test Deployment

- `http://your-domain.com` - Nginx default page
- `http://your-domain.com/test` - Test message
- `http://your-domain.com/health` - Health check

## Security

- **Never commit** `vars.yml` or `inventory/hosts.yml`
- Use provided `.example` files as templates
- `.gitignore` prevents accidental commits

## Structure

```
guestintheuniverse_ansible/
├── inventory/
│   ├── hosts.yml.example
│   └── hosts.yml (gitignored)
├── playbooks/nginx-only.yml
├── roles/
│   ├── docker/          # Docker installation
│   ├── users/           # User management
│   ├── firewall/        # UFW configuration
│   ├── nginx/           # Nginx configuration setup
│   └── deploy/          # Docker Compose deployment
├── vars.yml.example
├── vars.yml (gitignored)
├── .gitignore
└── README.md
```

## Roles

- **docker**: Docker engine installation
- **users**: Application user/group management  
- **firewall**: UFW configuration and port management
- **nginx**: Creates Nginx configs only
- **deploy**: Creates docker-compose.yml and runs deployment (contains nginx/deployment variables)
