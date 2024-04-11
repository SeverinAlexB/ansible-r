# bitcoind

Downloads bitcoin from bitcoincore.org, installs bitcoind.

Creates and starts bitcoin service on the machine.

This playbook expects the following variables

* `bitcoin_version`: Version (`23.0`)
* `bitcoin_checksum`: expected sha256 checksum of the bitcoin archive
* `bitcoind_network`: Whether it's a `mainnet` or `testnet` node. Default: `testnet`.
* `bitcoind_rpcthreads`: How many threads does bitcoind allow (4 needed per connected CLN node)
* `bitcoind_rpcallowip`: list of ip addresses that are allowed to connect. Set to `['0.0.0.0/0.0.0.0']` for all ips. Default: `['127.0.0.1']`.
* `bitcoind_rpcauth`: list of rpc authorizations (`user:password`) bitcoind accepts
* `install_service`: If the systemd service should be installed (`true`)