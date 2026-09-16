from app.pagamento import finalizar_compra

def test_deve_verificar_fraude_antes_de_cobrar(pedido_simples, mocker):
    mock_gateway = mocker.Mock()
    resultado = finalizar_compra(pedido_simples, mock_gateway)

    roteiro_esperado = [
        mocker.call.verificar_fraude(pedido_simples),
        mocker.call.cobrar(pedido_simples),
    ]
    mock_gateway.assert_has_calls(roteiro_esperado, any_order=False)
    assert resultado == "Compra aprovada"
