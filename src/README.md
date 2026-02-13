# Local Development Setup

## Quick Start

1. **Copy configuration**:
   ```bash
   cp config.example.yml config.local.yml
   # Edit config.local.yml as needed. Skip Nginx and SSL settings for local dev.
   ```

2. **Start local development**:
   ```bash
   docker-compose -f docker-compose.local.yml up --build
   ```

3. **Access app**:
   - **App**: http://localhost:5000
   - **Health Check**: http://localhost:5000/api/v1/health
   - **API Stats**: http://localhost:5000/api/v1/stats


## Development Features

- **Live Reload**: Code changes auto-reload Flask
- **Debug Mode**: Flask debug enabled
- **Volume Mount**: Local code mounted in container
- **Simple Setup**: No SSL or nginx required for local dev


## Testing Endpoints

- **Main App**: http://localhost:5000
- **Health Check**: `/api/v1/health` returns JSON
- **API Stats**: `/api/v1/stats` shows app info


## Production Deployment

When ready for production, push to master branch and let GitHub Actions handle the deployment.


## Docker Version Note

If you get Docker Compose version errors, use the legacy command:
```bash
# For older Docker versions
docker-compose -f docker-compose.local.yml up --build
```
