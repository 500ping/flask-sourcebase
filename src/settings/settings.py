from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    debug: bool = True
    time_zone: str = "Asia/Ho_Chi_Minh"

    db_url: str = "mysql+pymysql://test:12345@localhost/testdb"
