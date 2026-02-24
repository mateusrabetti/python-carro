from models.carro_models import Carro
from db import db
import json
from flask import make_response

def create_carro(carro_data):
    novo_carro = Carro(
        modelo=carro_data['modelo'],
        marca=carro_data['marca'],
        ano=carro_data['ano']
    )
    db.session.add(novo_carro)
    db.session.commit()
    response = make_response(
        json.dumps({
            "mensagem": "carro cadastrado com sucesso",
            "carro": novo_carro.json()
        })
    )
    response.headers["content=type"] = "application/json"
    return response        
