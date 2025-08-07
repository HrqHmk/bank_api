from sqlalchemy import Column, String, BIGINT, Float
from src.models.sqlite.settings.base import Base

class LegalEntityTable(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    faturamento = Column(Float)
    idade = Column(BIGINT)
    nome_fantasia = Column(String)
    celular = Column(String)
    email_corporativo = Column(String)
    categoria =Column(String)
    saldo = Column(Float)

    def __repr__(self):
        return f"Pessoa Juridica [name={self.nome_fantasia}]"
