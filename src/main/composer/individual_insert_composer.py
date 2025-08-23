from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.individual_repository import IndividualRepository
from src.controllers.individual_insert_controller import IndividualInsertController
from src.views.individual_insert_view import IndividualInsertView

def individual_insert_composer():
    model = IndividualRepository(db_connection_handler)
    controller = IndividualInsertController(model)
    view = IndividualInsertView(controller)

    return view
