# Monitoring Role - Grafana Alloy

This Ansible role installs and configures Grafana Alloy for collecting system metrics and sending them to Grafana Cloud.

## Requirements

- Target system: Ubuntu/Debian
- Ansible 2.9+

## Role Variables

### Required Variables (set in vars.yml)

```yaml
# Grafana Cloud endpoint
grafana_remote_write_url: "https://your-grafana-instance.com/api/v1/write"
grafana_username: "your-username"
grafana_password: "your-password"
```

## Usage

### Manual Execution

```bash
ansible-playbook -i ansible/inventory/production.yml ansible/playbooks/monitoring.yml
```

### With Custom Variables

```bash
ansible-playbook -i ansible/inventory/production.yml ansible/playbooks/monitoring.yml \
  -e "grafana_remote_write_url=https://your-instance.com/api/v1/write" \
  -e "grafana_username=your-username" \
  -e "grafana_password=your-password"
```

## What This Role Does

1. **Installs Grafana Alloy**: Adds Grafana repository and installs the latest version
2. **Creates directories**: Sets up configuration and data directories
3. **Deploys configuration**: Uses Jinja2 template to create Alloy configuration
4. **Starts service**: Enables and starts the Alloy systemd service
5. **Collects system metrics**: Configures Alloy to collect system metrics using built-in unix exporter

## Configuration

The Alloy configuration template (`templates/alloy-config.alloy`) includes:

- **Prometheus Remote Write**: Sends metrics to Grafana Cloud
- **System Metrics**: Collects system metrics using Alloy's built-in unix exporter

## Troubleshooting

### Check Alloy Status
```bash
systemctl status alloy
```

### View Alloy Logs
```bash
journalctl -u alloy -f
```

### Test Configuration
```bash
alloy --config.file=/etc/alloy/config.alloy --dry-run
```

### Restart Service
```bash
systemctl restart alloy
```

## Security Notes

- Grafana credentials should be stored securely in your vars.yml
- Configuration file is readable only by root
- Consider using a read-only API key for Grafana Cloud
- Ensure your firewall allows outbound connections to Grafana Cloud
