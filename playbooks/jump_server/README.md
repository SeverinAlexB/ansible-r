# jump_server

Configures a jump server. The jump server user is `jump`. It can be used to jump to every other server
in the network but not to login.

## User keys

The file [user_keys.pub](files/user_keys.pub) contains all pubkeys of users that are allowed to login.

## SSH usage

Use the jump server to access a cloud server:

```bash
ssh -J jump@jump1.redan.ch redan@10.0.1.3
```

To access a server in the internal network, you need to add the following config to `.ssh/config`:

```txt
Host myServerName
  User redan
  Hostname 10.*.*.*
  ProxyJump jump@jump1.redan.ch
```

## VPN
Use [sshuttle](https://sshuttle.readthedocs.io/en/stable/overview.html) to vpn into the private network.

```bash
sshuttle -r jump@jump1.redan.ch 10.0.0.0/16
```