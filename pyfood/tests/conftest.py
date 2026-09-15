import pytest

@pytest.fixture
def pedido_vazio(): 
    pedido = {
    "endereco_entrega": "Rua das flores, 123",
    "itens": []
    }

    return pedido

@pytest.fixture
def pedido_simples(): 
    pedido = {
        "endereco_entrega": "Rua das flores, 123", 
        "itens": [
            {"nome": "hamburguer", "preco": 25.00},
            {"nome": "refrigerante", "preco": 10.00},
            {"nome": "sorvete", "preco": 12.00}
        ]
    }

    return pedido

@pytest.fixture
def pedido_premium(): 
    pedido = {
        "endereco_entrega": "Rua das flores, 123",
        "itens": [
            {"nome": "hamburguer", "preco": 60.00}, 
            {"nome": "refrigerante", "preco": 12.00}, 
            {"nome": "chicken nuggets", "preco": 20.00}, 
            {"nome": "batata frita com bacon e cheddar", "preco": 30.00}
        ]
    }

    return pedido

@pytest.fixture
def arquivo_log_temporario():
    arquivo = open("log_teste.txt", "w")
    yield arquivo
    arquivo.close()