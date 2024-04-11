# Postgres

- Installs postgres from the postgres repository.
- Sets the `redan` user up as a super user so it works with `psql`.
- Respects a standby node. Doesnt execute create user and more.

## Variables

- `postgres_redan_password` To access the db with pgAdmin, the redan user needs a password.
- `postgres_allow_subnet` Default: 0.0.0.0/0. Subnet where the lightning user can connect from.