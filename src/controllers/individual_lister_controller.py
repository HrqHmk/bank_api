from typing import List
from src.models.sqlite.entities.individual import IndividualTable
from src.models.sqlite.repositories.individual_repository import IndividualRepository
from src.controllers.interfaces.individual_lister_controller import IndividualListerControllerInterface # pylint: disable=line-too-long

class IndividualListerController(IndividualListerControllerInterface):
    def __init__(self, individual_repository:IndividualRepository)-> None:
        self.__individual_repository = individual_repository
    
    def list(self)-> dict:
        individuals = self.__get_individuals_in_db()
        response = self.__format_response(individuals)

        return response
    
    def __get_individuals_in_db(self)-> List[IndividualTable]:
        individuals = self.__individual_repository.list_individuals()
        return individuals
    
    def __format_response(self, individuals: List[IndividualTable])->dict:
        formatted_response = []
        for individual in individuals:
            formatted_response.append({
                "nome": individual.nome_completo,
                "email": individual.email,
                "celular": individual.celular,
                "categoria": individual.categoria,
                "id": individual.id
            })
        
        return {
            "data": {
                "type": "Individuals",
                "count": len(formatted_response),
                "attributes": formatted_response
            }
        }
