from typing import Annotated
from pydantic import BaseModel, constr, ValidationError, Field, EmailStr, StringConstraints
from src.views.http_types.http_request import HttpRequest
from src.errors.errors_type.http_unprocessable_entity import HttpUnprocessableEntityError

def individual_insert_validator(http_request: HttpRequest)-> None:
    class BodyData(BaseModel):
        renda_mensal: float = Field(gt=0, description="Renda deve ser positiva")
        idade: int = Field(ge=18, le=120, description="Idade deve estar entre 18 e 120")
        nome_completo: constr(min_length=3, max_length=100, strip_whitespace=True) # type: ignore
        celular: Annotated[str, StringConstraints(pattern=r"^\+?\d{10,15}$")]  # aceita de 10 a 15 dígitos, com opcional "+" #pylint: disable=C0301 
        email: EmailStr
        categoria: Annotated[str, constr(to_lower=True, min_length=3, max_length=50)]
        saldo: float = Field(ge=0, description="Saldo não pode ser negativo")
    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
