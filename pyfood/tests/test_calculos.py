import pytest
from app.calculos import calcular_total_com_desconto, dividir_conta

def test_calcular_valor_sem_desconto(pedido_simples):
    assert calcular_total_com_desconto(pedido_simples) == 47.0

def test_calcular_valor_com_desconto(pedido_premium):
    assert calcular_total_com_desconto(pedido_premium) == 109.8

def test_escreve_no_log(arquivo_log_temporario):
    arquivo_log_temporario.write("pedido processado")

def test_deve_falhar_ao_dividir_por_zero(pedido_simples):
    with pytest.raises(ZeroDivisionError):
        dividir_conta(pedido_simples, 0)