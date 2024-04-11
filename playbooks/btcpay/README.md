# BTCPay

Installs/updates BTCPay Server. Needs to be executed with variable regarding `btcpay_host`:

```
ansible-playbook playbooks/btcpay.yml -i environments/local --extra-vars "btcpay_host=btcpay.redan.ch"
```

## Prerequisites

Make sure the `A-Record` (and potentially `AAAA-Record`) for domain given in the 
`btcpay_hosts` variable is pointing to the IP of the server.

## Variables

* `btcpay_host` (required)  
Domain the server is running on