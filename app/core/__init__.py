from os import environ as env

from .configs import AdditionalConfigs, Configs, LogginConfig, PostgresConfig


def load_configs() -> Configs:
    return Configs(
        postgres=PostgresConfig(
            host=env["POSTGRES_HOST"],
            port=int(env["POSTGRES_PORT"]),
            user=env["POSTGRES_USER"],
            password=env["POSTGRES_PASSWORD"],
            db_name=env["POSTGRES_DB"],
            pool_size=int(env["DB_POOL_SIZE"]),
            max_overflow=int(env["DB_MAX_OVERFLOW"]),
        ),
        logs=LogginConfig(
            log_level=env["LOG_LEVEL"],
            log_file=env["LOG_FILE"],
            log_encoding=env["LOG_ENCODING"],
        ),
        additional=AdditionalConfigs(
            origins=env["ALLOWED_IPS"],
        ),
    )
