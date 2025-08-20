from typing import List
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from src.models.sqlite.repositories.legal_entity_repository import LegalEntityRepository
from src.controllers.interfaces.legal_entity_lister_controller import LegalEntityListerControllerInterface # pylint: disable=line-too-long

class LegalEntityListerController(LegalEntityListerControllerInterface):
    def __init__(self, legal_entity_repository:LegalEntityRepository)-> None:
        self.__legal_entity_repository = legal_entity_repository
    
    def list(self)-> dict:
        legal_entities = self.__get_legal_entities_in_db()
        response = self.__format_response(legal_entities)

        return response
    
    def __get_legal_entities_in_db(self)-> List[LegalEntityTable]:
        legal_entities = self.__legal_entity_repository.list_legal_entity()
        return legal_entities
    
    def __format_response(self, legal_entities: List[LegalEntityTable])->dict:
        formatted_response = []
        for legal_entity in legal_entities:
            formatted_response.append({
                "nome": legal_entity.nome_fantasia,
                "email": legal_entity.email_corporativo,
                "celular": legal_entity.celular,
                "categoria": legal_entity.categoria,
                "id": legal_entity.id
            })
        
        return {
            "data": {
                "type": "Legal Entities",
                "count": len(formatted_response),
                "attributes": formatted_response
            }
        }
