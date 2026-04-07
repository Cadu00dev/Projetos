def test_separar_atividades_por_virgula():
    atividades_digitadas = "estudar,jogar,limpar"
    lista = atividades_digitadas.split(",")
    assert lista == ["estudar", "jogar", "limpar"]

def test_contar_quantidade_de_atividades():
    lista = ["estudar", "jogar", "limpar"]
    quantidade = len(lista)
    assert quantidade == 3

def test_sem_atividades():
    lista = []
    assert len(lista) == 0