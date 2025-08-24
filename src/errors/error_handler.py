from src.views.http_types.http_response import HttpResponse
from .errors_type.http_bad_request import HttpBadRequestError
from .errors_type.http_not_found import HttpNotFoundError
from .errors_type.http_unprocessable_entity import HttpUnprocessableEntityError

def handle_errors(error: Exception)-> HttpResponse:
    if isinstance(error, (HttpBadRequestError, HttpNotFoundError, HttpUnprocessableEntityError)):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "details": error.message
                }]
            }
        )
    
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "details": str(error)
            }]
        }
    )
