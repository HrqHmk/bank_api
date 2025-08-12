from sqlalchemy import Column, String, BIGINT, Float
from src.models.sqlite.settings.base import Base

class IndividualTable(Base):
    __tablename__ = "pessoa_fisica"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    renda_mensal = Column(Float)
    idade = Column(BIGINT)
    nome_completo = Column(String)
    celular = Column(String)
    email = Column(String)
    categoria =Column(String)
    saldo = Column(Float)

    def __repr__(self):
        return f"Pessoa Física [name={self.nome_fantasia}]"
