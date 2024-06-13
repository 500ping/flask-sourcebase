from flask import Blueprint

from src.dtos.requests.login_request import LoginRequest
from src.dtos.responses.default_response import DefaultResponse
from src.services.auth_service import AuthService

api_auth: Blueprint = Blueprint("api_auth", __name__)

auth_service: AuthService = AuthService()


@api_auth.route("/login", methods=["POST"])
def login(payload: LoginRequest) -> DefaultResponse:
    return auth_service.login(payload)
