# Common

Standard operations that we run on every server.

- Update packages.
- Add redan user.
- Add our ssh keys to redan user.
- Disable root login.
- Harden SSH.
- Install fail2ban.
- Enable ufw and allow ssh.
- Harden a lot of things according to https://madaidans-insecurities.github.io/guides/linux-hardening.html.
- Restrict `su` command to redan user only.
- Applies some grub boot config. REBOOT REQUIRED on first apply!

## Parameters

- `sshd_listen_publicly` Default: false. True if sshd should accept connections from the internet or just from 10.0.0.0/16.
- `qemu_guest_agent` Default: false.
- `private_ip` Private IP address. If `sshd_listen_publicly` is false, it will listen only in this internal interface.

## SSH logs

You can [check](https://serverfault.com/questions/339355/how-to-findout-which-key-was-being-used-to-login-for-an-ssh-session) who logged into SSH with the logs.