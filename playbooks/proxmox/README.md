# Proxmox

- Install proxmox (reboot required after first install!)
- Configures network interfaces
- Adds email notifications on Software RAID failures.


## Before running it

- Make sure your public ip + domain name is in /etc/hosts.
- Make sure your public/private ip is configured.

Reload network settings with `ifreload -a`. This doesnt break the vms.

## After running the script

Configure Firewall on the UI!
- Add rule to allow SSH from everywhere.
- Add rule to allow ping from 10.0.0.0/16.
- Add rule to allow 8006 (Proxmox UI) from 10.0.0.0/16.
- Enable firewall on the node.