import pytest

from administracaodeparticipantes.models import Participante
from home import gerador_times


def test_tem_que_falhar():
    with pytest.raises(ZeroDivisionError) as execution:
        result = 1 / 0
    assert 'division by zero' in str(execution.value)


def test_que_montar_time(db):
    ## Dado 24 participantes
    habilidades = {
        'Jogador-1': 1,
        'Jogador-5': 1,
        'Jogador-14': 1,
        'Jogador-17': 1,
        'Jogador-20': 1,
        'Jogador-22': 1,
        'Jogador-24': 1,
        'Jogador-2': 2,
        'Jogador-6': 2,
        'Jogador-18': 2,
        'Jogador-3': 3,
        'Jogador-7': 3,
        'Jogador-10': 3,
        'Jogador-11': 3,
        'Jogador-12': 3,
        'Jogador-16': 3,
        'Jogador-19': 3,
        'Jogador-4': 4,
        'Jogador-8': 4,
        'Jogador-9': 4,
        'Jogador-13': 4,
        'Jogador-15': 4,
        'Jogador-21': 4,
        'Jogador-23': 4,
    }

    for jogador in range(24):
        jogador_nro = jogador + 1
        jogador_tag = f'Jogador-{jogador_nro}'
        Participante.objects.create(
            nome=jogador_tag, sobrenome=str(jogador_nro),
            habilidade=habilidades.get(jogador_tag))

    #Quando montamos times
    jogadores = participantes = Participante.objects.all().values('nome', 'sobrenome', 'habilidade')
    times = gerador_times.montar_time(jogadores, aleatoriedade=42)

    time1, time2, time3, time4 = times

    assert time1 == [
        ('Jogador-1', 1),
        ('Jogador-2', 2),
        ('Jogador-6', 2),
        ('Jogador-16', 3),
        ('Jogador-9', 4),
        ('Jogador-21', 4),
    ]
    assert time2 == [
        ('Jogador-5', 1),
        ('Jogador-22', 1),
        ('Jogador-7', 3),
        ('Jogador-11', 3),
        ('Jogador-19', 3),
        ('Jogador-23', 4),
    ]
    assert time3 == [
        ('Jogador-14', 1),
        ('Jogador-20', 1),
        ('Jogador-3', 3),
        ('Jogador-12', 3),
        ('Jogador-4', 4),
        ('Jogador-13', 4),
    ]
    assert time4 == [
        ('Jogador-17', 1),
        ('Jogador-24', 1),
        ('Jogador-18', 2),
        ('Jogador-10', 3),
        ('Jogador-8', 4),
        ('Jogador-15', 4),
    ]



def test_que_montar_time_com_12(db):
    ## Dado 24 participantes
    habilidades = {
        'Jogador-1': 1,
        'Jogador-2': 2,
        'Jogador-3': 3,
        'Jogador-4': 4,
        'Jogador-5': 1,
        'Jogador-6': 2,
        'Jogador-7': 3,
        'Jogador-8': 4,
        'Jogador-9': 4,
        'Jogador-10': 3,
        'Jogador-11': 3,
        'Jogador-12': 3,
    }


    for jogador in range(12):
        jogador_nro = jogador + 1
        jogador_tag = f'Jogador-{jogador_nro}'
        Participante.objects.create(
            nome=jogador_tag, sobrenome=str(jogador_nro),
            habilidade=habilidades.get(jogador_tag))

    jogadores = Participante.objects.all().values('nome', 'sobrenome', 'habilidade')
    times = gerador_times.montar_time(jogadores, aleatoriedade=42)


    time1, time2 = times

    assert time1 == [
        ('Jogador-1', 1),
        ('Jogador-6', 2),
        ('Jogador-3', 3),
        ('Jogador-10', 3),
        ('Jogador-4', 4),
        ('Jogador-8', 4),
    ]

    assert time2 == [
        ('Jogador-5', 1),
        ('Jogador-2', 2),
        ('Jogador-7', 3),
        ('Jogador-11', 3),
        ('Jogador-12', 3),
        ('Jogador-9', 4),
    ]

