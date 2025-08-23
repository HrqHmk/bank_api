from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.individual_repository import IndividualRepository
from src.controllers.individual_lister_controller import IndividualListerController
from src.views.individual_lister_view import IndividualListerView

def individual_lister_composer():
    model = IndividualRepository(db_connection_handler)
    controller = IndividualListerController(model)
    view = IndividualListerView(controller)

    return view
