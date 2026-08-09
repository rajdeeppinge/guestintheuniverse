# GitHub Actions Workflows

This directory contains CI/CD workflows for automated deployment.


## Actions

### ansible-setup
- **Purpose**: Shared Ansible setup for all workflows
- **Features**: Python setup, Ansible installation, configuration generation
- **Used by**: infrastructure.yml, app-deployment.yml, posts-upload.yml


## Workflows

### infrastructure.yml
- **Trigger**: Changes to infrastructure roles (docker, users, firewall, monitoring) or weekly schedule
- **Schedule**: Every Sunday at 9 AM UTC for system updates
- **Purpose**: Configure server infrastructure and system updates
- **Manual Trigger**: Available via workflow_dispatch

### app-deployment.yml
- **Trigger**: Changes to source code, app deployment roles, or version files
- **Purpose**: Build, validate, and deploy application containers
- **Manual Trigger**: Available via workflow_dispatch

### posts-upload.yml
- **Trigger**: Changes to posts or drafts directories
- **Purpose**: Upload markdown content to server without full redeployment
- **Manual Trigger**: Available via workflow_dispatch


## Path-Based Triggers

Each workflow uses path filters to run only when relevant files change:
- Infrastructure changes → infrastructure.yml
- Application changes → app-deployment.yml
- Content changes → posts-upload.yml


## Requirements

All workflows require:
- GitHub Secrets configured (HOST, USER, SSH_KEY, etc.)
- Master branch deployment (manual triggers available)
- Ansible inventory and variables setup (automated via ansible-setup.yml)
