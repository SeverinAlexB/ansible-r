# Postgres primary

- Configures postgres so it can be used as a primary for replication.
- Creates a `repli` user that is used for replication.
- Configures 2 slaves.
- Creates databases with users.
- Removes slave config if a slave has been switched to a primary.

Followed tutorial: https://github.com/gabridome/docs/blob/master/c-lightning_with_postgresql_reliability.md

## Variables

- `postgres_repli_password` Password for the replication user.
- `postgres_slave_names` Names of the slave servers. Need to match the actual
slave server names defined in the slave role `postgres_slave_name`. The order is important here, because a query is commited as soon as the first slave responds.
- `postgres_allow_subnet` Default: 0.0.0.0/0. Subnet where the lightning user can connect from.



