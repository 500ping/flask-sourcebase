from pydantic_settings import BaseSettings


class StgSettings(BaseSettings):
    debug: bool = False
    time_zone: str = "Europe/Berlin"

    db_url: str = "mysql+pymysql://test:12345@localhost/testdb"
