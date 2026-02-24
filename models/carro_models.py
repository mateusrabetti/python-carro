from db import db

class carro(db.model):
    __tablename__= "carros"

    id = db.column(db.integer, primary_key=True)
    modelo = db.column(db.String(80), nullable=False)
    marca = db.column(db.String(80), nullable=False)
    ano = db.column(db.Integer, nullable=False)

    def json(self):
        return{
            'id': self.id,
            'modelo': self.modelo,
            'marca': self.marca,
            'ano': self.ano
        }