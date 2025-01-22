from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PostgresConfig:
    host: str = "localhost"
    port: int = 5432
    user: str = "user"
    password: str = "my_password"
    db_name: str = "my_database"
    pool_size: int = 10
    max_overflow: int = 10

    @property
    def db_uri(self) -> str:
        return f"postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"


@dataclass
class LogginConfig:
    log_level: str = "INFO"
    log_file: str = "app.log"
    log_encoding: str = "utf-8"


@dataclass
class AdditionalConfigs:
    origins: str = "http://localhost:8000,http://127.0.0.1:8000"

    @property
    def list_of_origins(self) -> list[str]:
        return self.origins.split(",")


@dataclass
class Configs:
    postgres: PostgresConfig
    logs: LogginConfig
    additional: AdditionalConfigs
