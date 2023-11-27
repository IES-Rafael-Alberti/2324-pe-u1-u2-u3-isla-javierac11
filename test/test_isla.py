from src.isla import generar_mapa, posicion_inicial_del_jugador, inicializar_juego

input_pedir_movimientos = []

mapa = [['!', ' ', ' ', ' ', ' '],
       ['!', 'v', ' ', ' ', '!'],
       [' ', ' ', ' ', ' ', ' '],
       ['X', '!', ' ', '<', ' '],
       ['!', '!', ' ', '!', '!']]

def test_generar_mapa():
    assert len(generar_mapa()) == 5
    
def test_posicion_inicial_del_jugador():
    assert posicion_inicial_del_jugador() == (2, 2)
    
def test_inicializar_juego():
    assert len(inicializar_juego()[0]) == 5
    assert inicializar_juego()[1] == (2,2)
    