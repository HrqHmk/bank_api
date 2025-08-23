from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.legal_entity_repository import LegalEntityRepository
from src.controllers.legal_entity_withdraw_controller import LegalEntityWithdrawController
from src.views.legal_entity_withdraw_view import LegalEntityWithdrawView

def legal_entity_withdraw_composer():
    model = LegalEntityRepository(db_connection_handler)
    controller = LegalEntityWithdrawController(model)
    view = LegalEntityWithdrawView(controller)

    return view
