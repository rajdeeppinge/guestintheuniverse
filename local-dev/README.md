# Local Development Setup

## Quick Start

1. **Create SSL directory** (for testing):
   ```bash
   mkdir -p local-dev/ssl
   # You can skip SSL for local testing or add dummy certs
   ```

2. **Start local development**:
   ```bash
   cd /home/shodh/software_engineering/guestintheuniverse_ansible
   mkdir -p local-dev/ssl
   docker-compose -f local-dev/docker-compose.yml up --build
   ```

3. **Access app**:
   - **App**: http://localhost:5000
   - **Nginx**: http://localhost:80
   - **Health**: http://localhost:5000/health

## Development Features

- **Live Reload**: Code changes auto-reload Flask
- **Debug Mode**: Flask debug enabled
- **Volume Mount**: Local code mounted in container
- **No SSL**: HTTP only for local testing

## Directory Structure
```
local-dev/
├── docker-compose.yml
├── nginx.conf
├── ssl/           # Add certs here if needed
└── ../app/           # App code from parent directory
```

## Testing Endpoints

- **Main App**: Beautiful UI with stats
- **Health Check**: `/health` returns JSON
- **API Stats**: `/api/stats` shows app info
- **Nginx Test**: `/test` shows simple message

## Production Deployment

When ready for production, use:
```bash
ansible-playbook -i inventory/hosts.yml playbooks/app-only.yml
```

## Docker Version Note

If you get Docker Compose version errors, use the legacy command:
```bash
# For older Docker versions
docker-compose -f local-dev/docker-compose.yml up --build
