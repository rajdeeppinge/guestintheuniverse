# Configuration Examples

This directory contains example configuration files for setting up the project.

## Files

- **secrets.example.yml**: GitHub Secrets configuration template
- **vars.example.yml**: Ansible variables template (copy to `ansible/vars.yml`)
- **hosts.example.yml**: Ansible inventory template (copy to `ansible/inventory/hosts.yml`)

## Setup Instructions

### 1. GitHub Secrets Setup
1. Go to GitHub Repository > Settings > Secrets and variables > Actions
2. Reference `secrets.example.yml` for required secrets
3. Add actual values (not the placeholder examples)

### 2. Ansible Variables Setup
1. Copy `vars.example.yml` to `ansible/vars.yml`
2. Replace placeholder values with your actual configuration
3. Ensure values match your GitHub Secrets where applicable

### 3. Ansible Inventory Setup
1. Copy `hosts.example.yml` to `ansible/inventory/hosts.yml`
2. Update with your server details

## Security Notes

- **Never commit actual secrets** to the repository
- **GITHUB_TOKEN** is automatically provided by GitHub Actions
- **SSH key** should be the private key, not the public key
- **Ports** should be numbers without quotes in GitHub Secrets interface
- **Consistency** - Ensure GitHub Secrets and Ansible vars use matching values
