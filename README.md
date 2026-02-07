# Guest in the Universe - Production Blog Stack

Production-ready blog platform built with Flask, Docker, and Ansible.

## Quick Start

### Prerequisites
- Cloud provider account
- GitHub repository with Actions enabled
- Docker and Ansible installed locally

### Setup

1. Clone and configure:
   ```bash
   git clone <this-repository>
   cd guestintheuniverse
   cp vars.yml.example vars.yml
   cp inventory/production.yml.example inventory/production.yml
   ```

2. Update configuration:
   - Edit `vars.yml` with your server details
   - Edit `inventory/production.yml` with your server info

3. Local testing:
   ```bash
   cd local-dev
   docker-compose up --build
   ```

4. Deploy to production:
   ```bash
   ansible-playbook -i inventory/production.yml playbooks/deploy.yml
   ```

## Repository Structure

```
guestintheuniverse/
├── ansible/                    # Infrastructure automation
├── local-dev/                 # Local development setup
├── .github/workflows/         # CI/CD pipelines
└── vars.yml                   # Configuration variables
```

## Technology Stack

- **Frontend**: Flask with Jinja2 templates
- **Infrastructure**: Cloud provider
- **Containerization**: Docker with Docker Compose
- **Automation**: Ansible for deployment
- **CI/CD**: GitHub Actions with container registry

## Development

### Local Development
Use the existing local-dev setup for testing:
```bash
cd local-dev
docker-compose up --build
```

Access the application at:
- **App**: http://localhost:5000
- **Nginx**: http://localhost:80
- **Health**: http://localhost:5000/health

## Features

### Current Features
- Basic Flask blog application
- Docker containerization
- Nginx reverse proxy
- Ansible deployment automation
- GitHub Actions CI/CD
- SSL/HTTPS support

### Future Enhancements
- Posts migration
- Database integration
- AI-enhanced search
- Advanced admin interface

## Security

- SSL/TLS encryption
- Container security best practices
- Secret management via GitHub Secrets
