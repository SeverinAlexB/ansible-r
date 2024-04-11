# Core Lightning

Downloads and installs the following software:

- [core-lightning](https://github.com/ElementsProject/lightning) from Github Releases
- [cln-channel-acceptor](https://github.com/redan-ch/cln-channel-acceptor) from Github releases.
- [cln-super-bitcoind](https://github.com/redan-ch/cln-super-bitcoind/releases/tag/v0.0.2) from Github releases.

Features:

- Plugins are installed nginx style in `.lightning/available-plugins`.
- Activated plugins are symlinked to `.lightning/plugins`.
- Lightning + plugins are configured and the lightning service is only restarted if config changed.
- Installation of binaries is only made if versions changed.

## Variables

**core-lightning**
- `cln_version` Default: 0.12.1. CLN version to download on Github Releases page.
- `cln_checksum` Sha256 Hash taken from the Github Release page.
- `node_alias` Default: undefined-paradiso. Name of the lightning node.
- `node_rgb` Default: 16293B. Color of the lightning node.
- `allow_tor_connections` Default: False.
- `allow_ip_connections`: Default False.
- `db_connection_string` Connection string for the Postgres DB. Format: "postgres://user:pass@localhost:5432/db_name"
- `use_sqlite_db` Default: False. Uses SQLite database.

**cln-super-bitcoind**
- `super_bitcoind_version` Default: 0.0.2. CLN version to download on Github Releases page.
- `super_bitcoind_checksum` Sha256 Hash taken from the Github Release page.
- `bitcoin_nodes` Default: See [here](./vars/main.yml). List of Bitcoin nodes to connect to.

**cln-channel-acceptor**
- `channel_acceptor_version` Default: 0.0.2. Github version tag without the v.
- `channel_acceptor_checksum` Sha256 Hash taken from the Github Release page.
- `allow_public_tor_only_nodes` Default: True. Indicates if the channel acceptor allows public tor channels.
- `min_private_channel_capacity_sat` Default: 50000. Min private channel capacity in satoshi.
- `min_public_channel_capacity_sat` Default: 1000000. Min public channel capacity in satoshi.