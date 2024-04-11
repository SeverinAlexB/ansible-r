# Postgres Slave

- Configures postgres so it connects to the primary as a slave.

## Variables

- `postgres_primary_ip` IP address of the primary postgres node.
- `postgres_slave_name` Name of this slave instance. Should be `slave1` or `slave2`.
- `postgres_repli_password` Password for the replication user to connect to the primary.