from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class OperadoraAtiva(Base):
    __tablename__ = "operadoras_ativas"

    registro_ans = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String(14), nullable=False)
    razao_social = Column(Text, nullable=False)
    nome_fantasia = Column(Text, nullable=True)
    modalidade = Column(Text, nullable=True)
    logradouro = Column(Text, nullable=True)
    numero = Column(String(10), nullable=True)
    complemento = Column(Text, nullable=True)
    bairro = Column(Text, nullable=True)
    cidade = Column(Text, nullable=True)
    uf = Column(String(2), nullable=True)
    cep = Column(String(8), nullable=True)
    ddd = Column(String(3), nullable=True)
    telefone = Column(String(15), nullable=True)
    fax = Column(String(15), nullable=True)
    endereco_eletronico = Column(Text, nullable=True)
    representante = Column(Text, nullable=True)
    cargo_representante = Column(Text, nullable=True)
    regiao_de_comercializacao = Column(Integer, nullable=True)
    data_registro_ans = Column(String(10), nullable=True)
