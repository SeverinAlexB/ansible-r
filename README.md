# Ansible

## Prepare developer

- [Install ansible](https://docs.ansible.com/ansible/latest/installation_guide/index.html).
- Install playbook dependencies: `ansible-galaxy install -r requirements.yml`.
- Get the Ansible Vault password and paste it into `.vault_pass`.
- Read the [Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/how-to-manage-multistage-environments-with-ansible#ansible-recommended-strategy-using-groups-and-multiple-inventories) to get to know Ansible.

## Prepare servers

The following tutorials are used to prepare the servers.

- [Initial Redan user - Cloud-init and manual](https://gitlab.redan.ch/redan/devops/ansible/-/wikis/Initial-Redan-user-Cloud-init-&-Manual)
- Disk Encryption for dedicated machines with [Hetzner](https://gitlab.redan.ch/redan/devops/ansible/-/wikis/Dedicated-Server-Disk-encryption---Hetzner) and [OVHCloud](https://gitlab.redan.ch/redan/devops/ansible/-/wikis/Dedicated-Server-Disk-encryption-OVHCloud).

## Run it

Run default stag environment:

```bash
ansible-playbook playbooks/jump_server.yml
```

Run prod environment. MAKE SURE YOU KNOW WHAT YOUR ARE DOING!

```bash
ansible-playbook playbooks/jump_server.yml -i environments/prod
```

### Local environment

The local environment is in gitignore and therefore not checked in on git. It is a environment that you can play around with as you wish. Just create a hosts.yml, add your servers and you are good to go.

### Personal environment


### Secrets

Every environment has its own secrets file at environments/xxx/group_vars/all/secrets.yml.

You can only decrypt the secrets and therefore use the playbooks when you set the `.vault_pass` file in the
project root and write the password in there. The password can be found on [bitwarden.redan.ch](https://bitwarden.redan.ch).


Edit secrets (replace xxx):

```bash
ansible-vault edit environments/xxx/group_vars/all/secrets.yml
```



## Support OS

- Ubuntu 22.04
- Debian 11

Important: Do not use Ubuntu 20.04. SSH has a bug.
