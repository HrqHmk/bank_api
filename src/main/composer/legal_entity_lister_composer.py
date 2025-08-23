from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.legal_entity_repository import LegalEntityRepository
from src.controllers.legal_entity_lister_controller import LegalEntityListerController
from src.views.legal_entity_lister_view import LegalEntityListerView

def legal_entity_lister_composer():
    model = LegalEntityRepository(db_connection_handler)
    controller = LegalEntityListerController(model)
    view = LegalEntityListerView(controller)

    return view
