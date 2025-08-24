from src.validators.legal_entity_insert_validator import legal_entity_insert_validator

class MockRequest:
    def __init__(self, body)-> None:
        self.body = body
    
def test_legal_entity_insert_validator():
    request = MockRequest({
        "faturamento": 200.00, 
        "idade": 30,
        "nome_fantasia": "Jhon Doe", 
        "celular": "11999999999", 
        "email_corporativo": "jhondoe@mail.com",
        "categoria": "category test",
        "saldo": 300.00
    })

    legal_entity_insert_validator(request)
