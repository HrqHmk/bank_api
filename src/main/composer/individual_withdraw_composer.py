from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.individual_repository import IndividualRepository
from src.controllers.individual_withdraw_controller import IndividualWithdrawController
from src.views.individual_withdraw_view import IndividualWithdrawView

def individual_withdraw_composer():
    model = IndividualRepository(db_connection_handler)
    controller = IndividualWithdrawController(model)
    view = IndividualWithdrawView(controller)

    return view
