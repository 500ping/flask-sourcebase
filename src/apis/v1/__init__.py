from flasgger import swag_from
from flask import Blueprint
from flask_pydantic import validate

from src.apis.v1.auth import api_auth
from src.dtos.responses.default_response import DefaultResponse

api_v1: Blueprint = Blueprint("api_v1", __name__)


@api_v1.route("/health-check", methods=["GET"])
@swag_from(
    {
        "tags": ["Common"],
        "responses": {
            200: {
                "description": "Health check status",
                "schema": {
                    "type": "object",
                    "properties": {
                        "code": {"type": "integer", "example": 200},
                        "message": {"type": "string", "example": "success"},
                        "data": {
                            "type": "object",
                            "properties": {
                                "success": {"type": "boolean", "example": True},
                            },
                        },
                    },
                    "example": {
                        "code": 200,
                        "message": "success",
                        "data": {"success": True},
                    },
                },
            }
        },
    }
)
@validate()
def health_check() -> DefaultResponse:
    return DefaultResponse(data={"success": True})


api_v1.register_blueprint(api_auth, url_prefix="/auth")
