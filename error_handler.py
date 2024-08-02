from enum import Enum

class Client_Error(Enum):
    Error_400 = "<Response [400 Bad Request]>"
    Error_404 = "<Response [404 Not Found]>"
    Error_422 = "<Response [422 Unprocessable Entity]>"
    Error_429 = "<Response [429 Too Many Requests]>"
