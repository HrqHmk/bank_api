from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.legal_entity_repository import LegalEntityRepository
from src.controllers.legal_entity_controller import LegalEntityInsertController
from src.views.legal_entity_insert_view import LegalEntityInsertView

def legal_entity_insert_composer():
    model = LegalEntityRepository(db_connection_handler)
    controller = LegalEntityInsertController(model)
    view = LegalEntityInsertView(controller)

    return view
