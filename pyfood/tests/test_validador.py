from app.validador import validar_pedido

def test_validador_pedido_vazio(pedido_vazio):
    assert validar_pedido(pedido_vazio) == False

def test_validador_pedido(pedido_simples):
    assert validar_pedido(pedido_simples) == True

def test_pedido_sem_endereco():
    pedido = {"itens": [{"nome": "hamburguer", "preco": 25.00}]}
    assert validar_pedido(pedido) == False

def test_pedido_endereco_vazio():
    pedido = {
        "endereco_entrega": "",
        "itens": [{"nome": "hamburguer", "preco": 25.00}]
    }
    assert validar_pedido(pedido) == False

def test_pedido_total_baixo():
    pedido = {
        "endereco_entrega": "Rua das flores, 123",
        "itens": [{"nome": "refrigerante", "preco": 8.00}]
    }
    assert validar_pedido(pedido) == False