# Guest in the Universe - Application

Local development and application structure.

## Quick Start

### Local Development
```bash
docker compose -f docker-compose.local.yml up --build
```
Access at: http://localhost:5000


## Application Structure

```
application/
├── app/              # Flask application
│   ├── app.py        # Main application file
│   ├── requirements.txt
│   └── Dockerfile
├── nginx/            # Nginx configuration
│   ├── nginx.conf
│   └── Dockerfile
├── docker-compose.yml          # Production compose
├── docker-compose.local.yml    # Local development compose
└── config.local.yml           # Local configuration
```

## Development Workflow

1. Make changes to application code in `app/`
2. Rebuild and restart: `docker compose -f docker-compose.local.yml up --build`
3. Test at http://localhost:5000
4. Commit changes and push to trigger CI/CD

## Configuration

Local configuration is in `config.local.yml`. This file is for local development only and should not be committed to production.

## Endpoints

- `/` - Main application interface
- `/health` - Health check endpoint
- `/test` - Simple test page
