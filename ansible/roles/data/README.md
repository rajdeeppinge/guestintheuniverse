# Data Role

This role handles the migrations of posts and setup of the SQLite database for the Guest in the Universe blog.

## Functionality

- **Idempotent database creation** - Only creates if doesn't exist
- **Schema initialization** - Sets up posts table with indexes
- **One-time migration** - Migrates existing markdown posts to database metadata
- **Verification** - Confirms database is ready

## Variables

- `app_dir` - Application directory path
- `app_user` - Application user
- `app_group` - Application group

## Usage

This role runs automatically in the deployment workflow before the app role:

```bash
ansible-playbook -i inventory/hosts.yml playbooks/deploy.yml
```
