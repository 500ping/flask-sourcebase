from src.dtos.requests.login_request import LoginRequest
from src.dtos.responses.default_response import DefaultResponse


class AuthService:
    def __init__(self) -> None:
        pass

    def login(self, payload: LoginRequest) -> DefaultResponse:
        pass
